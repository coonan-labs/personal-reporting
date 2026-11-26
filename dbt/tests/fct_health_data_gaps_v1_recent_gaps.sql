{{
    config(
        severity = 'warn',
        enabled = (target.name != 'mock'),
        description = 'Warn when any gap date falls in the last 30 days.'
    )
}}

-- Warn when any gap date falls in the last 30 days. Expected gaps (device not
-- worn) stay visible without failing the build. Disabled on mock: fixtures end
-- in 2025 while the window runs to yesterday, so every recent date would warn.
{% set cutoff_date = run_started_at - modules.datetime.timedelta(days=30) %}
{% set recent_cutoff = cutoff_date.strftime('%Y-%m-%d') %}

select
    activity_date,
    gap_types
from
    {{ ref('fct_health_data_gaps', v=1) }}
where
    is_gap
    and activity_date >= cast('{{ recent_cutoff }}' as date)
