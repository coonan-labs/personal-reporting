-- ============================================================================
-- STAGING LAYER (BASE): HubSpot Engagements Base
-- ============================================================================
-- Purpose: Union all HubSpot engagement object types (meetings, calls,
--          communications) into a standardized format. Used as the base
--          for stg_hubspot__engagements and junction table models.
--
-- Source: hubspot.meetings, hubspot.calls, hubspot.communications
-- Output: One row per unique engagement across all types
-- ============================================================================

-- The _deleted/_deleted_at tombstone columns only exist once the pipeline has
-- run with the HubSpot archived sweep (issue #43). Older live tables lack
-- them, so each branch falls back to not-deleted instead of failing on a
-- missing column.
{% set meetings_src = source('hubspot', 'meetings') %}
{% set meetings_has_deleted = column_exists(meetings_src, '_deleted') %}
{% set calls_src = source('hubspot', 'calls') %}
{% set calls_has_deleted = column_exists(calls_src, '_deleted') %}
{% set communications_src = source('hubspot', 'communications') %}
{% set communications_has_deleted = column_exists(communications_src, '_deleted') %}

with meetings as (

    select
        id as engagement_id,
        'MEETING' as engagement_type,
        properties__hs_meeting_body as body_preview,
        cast(properties__hs_meeting_start_time as timestamp) as occurred_at,
        cast(created_at as timestamp) as created_at,
        cast(updated_at as timestamp) as updated_at,
        -- Deletion tombstone from the HubSpot archived sweep (issue #43).
        -- _deleted_at is cast to timestamp: on the mock target DuckDB infers
        -- it as timestamptz or varchar depending on the fixture rows, and
        -- the dedup coalesce needs a consistent timestamp type.
        {% if meetings_has_deleted %}
        coalesce(_deleted, false) as is_deleted,
        cast(_deleted_at as timestamp) as deleted_at
        {% else %}
        false as is_deleted,
        cast(null as timestamp) as deleted_at
        {% endif %}
    from {{ meetings_src }}

),

calls as (

    select
        id as engagement_id,
        'CALL' as engagement_type,
        properties__hs_call_body as body_preview,
        cast(properties__hs_timestamp as timestamp) as occurred_at,
        cast(created_at as timestamp) as created_at,
        cast(updated_at as timestamp) as updated_at,
        {% if calls_has_deleted %}
        coalesce(_deleted, false) as is_deleted,
        cast(_deleted_at as timestamp) as deleted_at
        {% else %}
        false as is_deleted,
        cast(null as timestamp) as deleted_at
        {% endif %}
    from {{ calls_src }}

),

communications as (

    select
        id as engagement_id,
        'COMMUNICATION' as engagement_type,
        properties__hs_communication_body as body_preview,
        cast(properties__hs_timestamp as timestamp) as occurred_at,
        cast(created_at as timestamp) as created_at,
        cast(updated_at as timestamp) as updated_at,
        {% if communications_has_deleted %}
        coalesce(_deleted, false) as is_deleted,
        cast(_deleted_at as timestamp) as deleted_at
        {% else %}
        false as is_deleted,
        cast(null as timestamp) as deleted_at
        {% endif %}
    from {{ communications_src }}

),

all_engagements as (

    select * from meetings
    union all
    select * from calls
    union all
    select * from communications

),

unique_engagements as (
-- Delete semantics (issue #43): order by coalesce(deleted_at, updated_at)
-- so a deletion tombstone (deleted_at = archive time, later than the live
-- updated_at) wins the dedup. Deleted engagements are then filtered out
-- below, so they never reach facts; a later live update restores the row.

    {{ dbt_utils.deduplicate(
        relation='all_engagements',
        partition_by='engagement_id',
        order_by='coalesce(deleted_at, updated_at) desc'
        )
    }}

)

select
    engagement_id,
    engagement_type,
    body_preview,
    occurred_at,
    created_at,
    updated_at
from unique_engagements
where not coalesce(is_deleted, false)
