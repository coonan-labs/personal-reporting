-- ============================================================================
-- STAGING LAYER: HubSpot Companies
-- ============================================================================
-- Purpose: Clean and standardize raw HubSpot company data. Extracts company
--          information, parses tier from ideal customer profile field, and
--          deduplicates records.
--
-- Source: hubspot.companies (raw dlt-loaded data)
-- Transformations:
--   - Rename columns to standard naming convention
--   - Parse company tier from hs_ideal_customer_profile field (extract numeric)
--   - Deduplicate by company_id (keep most recent)
-- Output: One row per unique company with standardized fields
-- ============================================================================

-- The _deleted/_deleted_at tombstone columns only exist once the pipeline has
-- run with the HubSpot archived sweep (issue #43). Older live tables lack
-- them, so fall back to not-deleted instead of failing on a missing column.
{% set companies_src = source('hubspot', 'companies') %}
{% set has_deleted = column_exists(companies_src, '_deleted') %}

with companies as (
    -- CTE: Companies Raw Extraction
    -- Purpose: Extract and transform raw HubSpot company data into clean, typed columns.
    --          Handles tier parsing from string field and column renaming.
    -- Source: hubspot.companies (raw API data loaded by dlt)
    -- Transformations:
    --   - Rename columns: id -> company_id, properties__name -> company_name
    --   - Parse tier: Extract numeric value from hs_ideal_customer_profile
    --     (format: "tier_1", "tier_2", "tier_3" -> extract last character)

    select
        id as company_id,  -- HubSpot company ID
        properties__name as company_name,  -- Company name
        properties__createdate as created_at,  -- When company was created in HubSpot
        properties__hs_lastmodifieddate as updated_at,  -- When company was last modified
        -- Parse numeric tier value from string field (e.g., "tier_1" -> 1)
        -- Uses right() to get last character, then safely casts to integer
        {{ cast_safe("right(cast(properties__hs_ideal_customer_profile as string), cast(1 as integer))", "integer") }}
            as company_tier,
        -- Deletion tombstone from the HubSpot archived sweep (issue #43):
        -- _deleted is true and _deleted_at is the archive timestamp for
        -- archived companies; null/false for live companies. The flag is kept
        -- so dim_group can retain deleted companies as flagged rows.
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
        {{ companies_src }}

),

unique_companies as (
-- CTE: Deduplicated Companies
-- Purpose: Remove duplicate records for the same company_id, keeping only
--          the most recently updated version.
-- Method: Uses dbt_utils.deduplicate macro with ROW_NUMBER() window function
-- Output: One row per unique company_id (most recent version)
-- Delete semantics: order by coalesce(deleted_at, updated_at) so a deletion
--          tombstone (deleted_at = archive time, later than the live
--          updated_at) wins the dedup and the company stays flagged deleted.
--          A later live update (updated_at after deleted_at) restores it.

    {{ dbt_utils.deduplicate(
        relation='companies',
        partition_by='company_id',
        order_by='coalesce(deleted_at, updated_at) desc, coalesce(is_deleted, false) desc'
        )
    }}

)

-- Final output: Clean, deduplicated company data
select * from unique_companies
