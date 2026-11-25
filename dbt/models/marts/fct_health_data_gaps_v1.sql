-- ============================================================================
-- MART LAYER: Health Data Gaps
-- ============================================================================
-- Purpose: Identify calendar dates with missing steps and/or sleep data, so
--          sync gaps are visible instead of silent. One row per calendar date
--          in the observed window, with flags for each source and the gap type.
--
--          Steps can be excluded from gap detection with the
--          health_gaps_include_steps variable (currently false while step data
--          is not syncing, see #134). Steps data is still reported for context
--          when excluded; only the gap determination ignores it.
--
--          A date only counts as a gap for a source once that source has
--          started reporting (its first observed date); earlier dates are
--          not flagged for the not-yet-started source.
--
-- Sources: dim_date, core_daily_steps, core_sleep_sessions
-- Output: One row per calendar date in the observed window
-- ============================================================================

{% set yesterday = run_started_at - modules.datetime.timedelta(days=1) %}
{% set window_end_date = yesterday.strftime('%Y-%m-%d') %}

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
        -- is not a gap for that source (see date_coverage below).
        (select min(daily_steps.activity_date) from daily_steps) as steps_start_date,
        (select min(daily_sleep.activity_date) from daily_sleep) as sleep_start_date
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
        {% if var('health_gaps_include_steps', false) %}
        case
            when steps_expected and not has_steps and sleep_expected and not has_sleep then 'both'
            when steps_expected and not has_steps then 'steps'
            when sleep_expected and not has_sleep then 'sleep'
            else 'none'
        end as gap_type
        {% else %}
        case
            when sleep_expected and not has_sleep then 'sleep'
            else 'none'
        end as gap_type
        {% endif %}
    from
        date_coverage

),

final as (

    select
        cast(activity_date as date) as activity_date,
        has_steps,
        has_sleep,
        cast(step_count as bigint) as step_count,
        cast(sleep_minutes as numeric(38, 9)) as sleep_minutes,
        gap_type <> 'none' as is_gap,
        gap_type
    from
        gap_flags

)

select * from final
