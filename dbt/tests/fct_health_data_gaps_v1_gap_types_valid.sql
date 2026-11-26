{{
    config(
        enabled = (target.name == 'mock'),
        description = 'Every gap_types element is a known gap type (steps or sleep).'
    )
}}

-- Every element of gap_types must be a known gap type. Mock-gated: the
-- DuckDB list_filter below has no direct Databricks equivalent, and the
-- array is built from two literals in the gap_types_array macro, so this
-- guards the macro against typos when it is extended.
select
    activity_date,
    gap_types
from
    {{ ref('fct_health_data_gaps', v=1) }}
where
    len(list_filter(gap_types, x -> x not in ('steps', 'sleep'))) > 0
