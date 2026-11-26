{{
    config(
        enabled = (target.name == 'mock'),
        description = 'Fixture block 2025-02-14..18 flagged as expected.'
    )
}}

-- Singular test: the fixture block 2025-02-14..2025-02-18 must be flagged
-- exactly as expected. To expand the block, add a row to test_cases below
-- (and the matching fixture rows). Each case is (activity_date, expected
-- gap types with steps checked, expected gap types with steps unchecked),
-- so the test passes in both check modes:
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
    ('2025-02-14', '[]', '[]'),
    ('2025-02-15', "['sleep']", "['sleep']"),
    ('2025-02-16', "['steps']", '[]'),
    ('2025-02-17', "['steps', 'sleep']", "['sleep']"),
    ('2025-02-18', '[]', '[]'),
] %}
{% set include_steps = 'steps' in var('health_gap_checks', ['sleep']) %}

with expected as (

    {% for activity_date, gap_types_on, gap_types_off in test_cases %}
    select
        cast('{{ activity_date }}' as date) as activity_date,
        {{ gap_types_on if include_steps else gap_types_off }}
            as expected_gap_types
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
