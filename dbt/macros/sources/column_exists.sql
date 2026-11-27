-- Check whether a column exists in a relation at compile time.
-- Used to tolerate schema evolution: a column added by a newer pipeline run
-- may not exist in older loaded tables yet (e.g. _deleted/_deleted_at from
-- the HubSpot archived sweep only appear once the pipeline has run with the
-- sweep). When the column is absent, models fall back to a not-deleted
-- default instead of failing on a missing column.
-- Usage: {{ column_exists(source('hubspot', 'contacts'), '_deleted') }}
--
{% macro column_exists(relation, column_name) -%}
    {% set cols = adapter.get_columns_in_relation(relation) %}
    {% set names = cols | map(attribute='name') | list %}
    {{ return(column_name in names) }}
{%- endmacro %}
