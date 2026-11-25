{{ config(severity = 'warn') }}

-- Warn when any gap date falls in the last 30 days. Expected gaps (device not
-- worn) stay visible without failing the build.
{% set cutoff_date = run_started_at - modules.datetime.timedelta(days=30) %}
{% set recent_cutoff = cutoff_date.strftime('%Y-%m-%d') %}

select
    activity_date,
    gap_type
from
    {{ ref('fct_health_data_gaps', v=1) }}
where
    is_gap
    and activity_date >= cast('{{ recent_cutoff }}' as date)
