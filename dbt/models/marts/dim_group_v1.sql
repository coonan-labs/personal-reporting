-- ============================================================================
-- MART LAYER: Group Dimension
-- ============================================================================
-- Purpose: One row per HubSpot company, which in this dataset represents a
--          personal group or community rather than a business organisation.
--          SCD type 1. Includes a sentinel row for people without a group.
--
-- Source: stg_hubspot__companies
-- Output: One row per group (plus an UNKNOWN sentinel row)
-- ============================================================================

with
-- Import CTEs: one per upstream model, selected as-is
stg_hubspot__companies as (

    select
        company_id,
        company_name,
        company_tier,
        -- Deletion flag from the HubSpot archived sweep (issue #43).
        -- Deleted companies are kept in the dimension, flagged, so existing
        -- facts still resolve to a group.
        is_deleted
    from {{ ref('stg_hubspot__companies') }}

),

-- Transform CTEs: build the UNKNOWN sentinel and the final output
sentinel as (

    select
        'UNKNOWN_GROUP' as group_key,
        cast(null as string) as group_id,
        'Unknown group' as group_name,
        cast(null as bigint) as group_tier,
        false as is_deleted

),

final as (

    select
        {{ dbt_utils.generate_surrogate_key(['company_id']) }} as group_key,
        company_id as group_id,
        company_name as group_name,
        cast(company_tier as bigint) as group_tier,
        is_deleted
    from stg_hubspot__companies
    union all
    select * from sentinel

)

select * from final
