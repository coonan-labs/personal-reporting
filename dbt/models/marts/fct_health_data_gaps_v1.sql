-- ============================================================================
-- MART LAYER: Health Data Gaps
-- ============================================================================
-- Purpose: Identify calendar dates with missing steps and/or sleep data, so
--          sync gaps are visible instead of silent. One row per calendar date
--          in the observed window, with flags for each source and the gap type.
--
--          Which sources are checked is set by the health_gap_checks
--          variable (see #134), a list such as [sleep] or [sleep, steps].
--          A source's data is still reported for context when it is not
--          checked; only the gap determination ignores it.
--
--          A date only counts as a gap for a source once that source has
--          started reporting (its first observed date); earlier dates are
--          not flagged for the not-yet-started source. A source that has
--          never reported at all falls back to the window start, so a
--          total outage is flagged instead of invisible.
--
-- Sources: dim_date, core_daily_steps, core_sleep_sessions
-- Output: One row per calendar date in the observed window
-- ============================================================================

-- Window end derives from run_started_at in UTC, while activity_date is a
-- civil/local date; the boundary can be off by a day for UTC+ time zones.
{% set yesterday = run_started_at - modules.datetime.timedelta(days=1) %}
{% set window_end_date = yesterday.strftime('%Y-%m-%d') %}
{% set checks = var('health_gap_checks', ['sleep']) %}
{% set steps_gap_expr = "steps_expected and not has_steps" if 'steps' in checks else "false" %}
{% set sleep_gap_expr = "sleep_expected and not has_sleep" if 'sleep' in checks else "false" %}

with
-- Import CTEs: one per upstream model, selected as-is
dim_date as (

    select
        date_day
    from {{ ref('dim_date', v=1) }}

),

daily_steps as (

    select
        activity_date,
        step_count
    from
        {{ ref('core_daily_steps') }}

),

sleep_sessions as (

    select
        session_date,
        duration_minutes
    from
        {{ ref('core_sleep_sessions') }}

),

-- Transform CTEs: aggregate sleep to the day grain (a date can hold a main
-- sleep plus naps) and bound the window to the observed data
daily_sleep as (

    select
        session_date as activity_date,
        cast(sum(duration_minutes) as numeric(38, 9)) as sleep_minutes
    from
        sleep_sessions
    group by
        session_date

),

all_observed_dates as (

    select activity_date from daily_steps
    union all
    select activity_date from daily_sleep

),

observed_bounds as (

    select
        min(activity_date) as window_start_date,
        -- Per-source first observed dates: a date before a source's start
        -- is not a gap for that source (see date_coverage below). When a
        -- source has never reported at all, fall back to the window start
        -- so a total outage is flagged instead of invisible.
        coalesce(
            (select min(daily_steps.activity_date) from daily_steps),
            min(activity_date)
        ) as steps_start_date,
        coalesce(
            (select min(daily_sleep.activity_date) from daily_sleep),
            min(activity_date)
        ) as sleep_start_date
    from
        all_observed_dates

),

date_coverage as (

    select
        dim.date_day as activity_date,
        steps.activity_date is not null as has_steps,
        sleep.activity_date is not null as has_sleep,
        coalesce(
            dim.date_day >= (select observed_bounds.steps_start_date from observed_bounds),
            false
        ) as steps_expected,
        coalesce(
            dim.date_day >= (select observed_bounds.sleep_start_date from observed_bounds),
            false
        ) as sleep_expected,
        steps.step_count,
        sleep.sleep_minutes
    from
        dim_date as dim
    left join daily_steps as steps
        on dim.date_day = steps.activity_date
    left join daily_sleep as sleep
        on dim.date_day = sleep.activity_date
    where
        -- dim_date's spine starts 2016-01-01; observed dates before it
        -- have no dimension row and are excluded here.
        dim.date_day between (select observed_bounds.window_start_date from observed_bounds)
        and cast('{{ window_end_date }}' as date)

),

gap_flags as (

    select
        activity_date,
        has_steps,
        has_sleep,
        step_count,
        sleep_minutes,
        {{ steps_gap_expr }} as steps_gap,
        {{ sleep_gap_expr }} as sleep_gap,
        {{ gap_types_array(steps_gap_expr, sleep_gap_expr) }} as gap_types
    from
        date_coverage

),

final as (

    select
        activity_date,
        has_steps,
        has_sleep,
        step_count,
        sleep_minutes,
        steps_gap or sleep_gap as is_gap,
        gap_types
    from
        gap_flags

)

select * from final
