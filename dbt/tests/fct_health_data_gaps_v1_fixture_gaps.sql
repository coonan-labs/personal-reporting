{{
    config(
        enabled = (target.name == 'mock'),
        description = 'Fixture block 2025-02-14..18 flagged as expected.'
    )
}}

-- Singular test: the fixture block 2025-02-14..2025-02-18 must be flagged
-- exactly as expected. To expand the block, add a row to test_cases below
-- (and the matching fixture rows). Each case is (activity_date, steps data
-- present, sleep data present); the expected gap types are derived from
-- which sources the health_gap_checks list enables, so the test passes in
-- every check mode ([sleep], [steps], [sleep, steps]):
-- 2025-02-14: steps + sleep present
-- 2025-02-15: steps only
-- 2025-02-16: sleep only
-- 2025-02-17: neither
-- 2025-02-18: steps + sleep present
-- Returns rows only when the model disagrees.
--
-- Note: the total-outage fallback (zero step rows -> the window start) is not
-- covered by test_cases below — the fixtures always contain steps. It was
-- verified by running the compiled model against an empty core_daily_steps:
-- every window date flagged steps/both, none flagged none.

{% set test_cases = [
    ('2025-02-14', true, true),
    ('2025-02-15', true, false),
    ('2025-02-16', false, true),
    ('2025-02-17', false, false),
    ('2025-02-18', true, true),
] %}
{% set checks = var('health_gap_checks', ['sleep']) %}
{% set include_steps = 'steps' in checks %}
{% set include_sleep = 'sleep' in checks %}

with expected as (

    {% for activity_date, has_steps_data, has_sleep_data in test_cases %}
    {% set expected_types = (["'steps'"] if include_steps and not has_steps_data else []) + (["'sleep'"] if include_sleep and not has_sleep_data else []) %}
    select
        cast('{{ activity_date }}' as date) as activity_date,
        [{{ expected_types | join(', ') }}] as expected_gap_types
    {% if not loop.last %}
    union all
    {% endif %}
    {% endfor %}

)

select
    expected.activity_date,
    actual.gap_types as actual_gap_types,
    expected.expected_gap_types
from
    expected
left join {{ ref('fct_health_data_gaps', v=1) }} as actual
    on expected.activity_date = actual.activity_date
where
    actual.activity_date is null
    or actual.gap_types <> expected.expected_gap_types
