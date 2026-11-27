-- ============================================================================
-- STAGING LAYER: HubSpot Contacts
-- ============================================================================
-- Purpose: Clean and standardize raw HubSpot contact data. Extracts contact
--          information, handles company associations, and deduplicates records.
--
-- Source: hubspot.contacts (raw dlt-loaded data)
-- Transformations:
--   - Rename columns to standard naming convention
--   - Extract company association via associatedcompanyid
--   - Deduplicate by contact_id (keep most recent)
-- Output: One row per unique contact with standardized fields
-- ============================================================================

-- The _deleted/_deleted_at tombstone columns only exist once the pipeline has
-- run with the HubSpot archived sweep (issue #43). Older live tables lack
-- them, so fall back to not-deleted instead of failing on a missing column.
{% set contacts_src = source('hubspot', 'contacts') %}
{% set has_deleted = column_exists(contacts_src, '_deleted') %}

with contacts as (
    -- CTE: Contacts Raw Extraction
    -- Purpose: Extract and transform raw HubSpot contact data into clean, typed columns.
    --          Handles column renaming and company association extraction.
    -- Source: hubspot.contacts (raw API data loaded by dlt)
    -- Transformations:
    --   - Rename columns: id -> contact_id, properties__firstname -> first_name, etc.
    --   - Extract company association: properties__associatedcompanyid -> company_id

    select
        id as contact_id,  -- HubSpot contact ID
        nullif(cast(properties__associatedcompanyid as string), '') as company_id,  -- Associated company ID (empty string -> null)
        properties__email as email,  -- Contact email address
        properties__firstname as first_name,  -- Contact's first name
        properties__lastname as last_name,  -- Contact's last name
        properties__createdate as created_at,  -- When contact was created in HubSpot
        properties__lastmodifieddate as updated_at,  -- When contact was last modified
        -- Deletion tombstone from the HubSpot archived sweep (issue #43):
        -- _deleted is true and _deleted_at is the archive timestamp for
        -- archived contacts; null/false for live contacts. The flag is kept
        -- so dim_person can retain deleted contacts as flagged rows.
        -- _deleted_at is cast to timestamp: on the mock target DuckDB infers
        -- it as timestamptz or varchar depending on the fixture rows, and
        -- the dedup coalesce needs a consistent timestamp type.
        -- When the source table predates the archived sweep it has neither
        -- column, so default to not-deleted.
        {% if has_deleted %}
        coalesce(_deleted, false) as is_deleted,
        cast(_deleted_at as timestamp) as deleted_at
        {% else %}
        false as is_deleted,
        cast(null as timestamp) as deleted_at
        {% endif %}
    from
        {{ contacts_src }}

),

unique_contacts as (
-- CTE: Deduplicated Contacts
-- Purpose: Remove duplicate records for the same contact_id, keeping only
--          the most recently updated version.
-- Method: Uses dbt_utils.deduplicate macro with ROW_NUMBER() window function
-- Output: One row per unique contact_id (most recent version)
-- Delete semantics: order by coalesce(deleted_at, updated_at) so a deletion
--          tombstone (deleted_at = archive time, later than the live
--          updated_at) wins the dedup and the contact stays flagged deleted.
--          A later live update (updated_at after deleted_at) restores it.

    {{ dbt_utils.deduplicate(
        relation='contacts',
        partition_by='contact_id',
        order_by='coalesce(deleted_at, updated_at) desc, coalesce(is_deleted, false) desc'
        )
    }}

)

-- Final output: Clean, deduplicated contact data
select * from unique_contacts
