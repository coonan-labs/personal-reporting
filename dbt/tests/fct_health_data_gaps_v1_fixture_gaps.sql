{{
    config(
        enabled = (target.name == 'mock'),
        description = 'Fixture block 2025-02-14..18 flagged as expected.'
    )
}}

-- Singular test: the fixture block 2025-02-14..2025-02-18 must be flagged
-- exactly as expected. To expand the block, add a row to test_cases below
-- (and the matching fixture rows). Each case is (activity_date, expected
-- gap type with steps included, expected gap type with steps excluded),
-- so the test passes in both var modes:
-- 2025-02-14: steps + sleep present
-- 2025-02-15: steps only
-- 2025-02-16: sleep only
-- 2025-02-17: neither
-- 2025-02-18: steps + sleep present
-- Returns rows only when the model disagrees.

{% set test_cases = [
    ('2025-02-14', 'none', 'none'),
    ('2025-02-15', 'sleep', 'sleep'),
    ('2025-02-16', 'steps', 'none'),
    ('2025-02-17', 'both', 'sleep'),
    ('2025-02-18', 'none', 'none'),
] %}
{% set include_steps = var('health_gaps_include_steps', false) %}

with expected as (

    {% for activity_date, gap_type_on, gap_type_off in test_cases %}
    select
        cast('{{ activity_date }}' as date) as activity_date,
        '{{ gap_type_on if include_steps else gap_type_off }}'
            as expected_gap_type
    {% if not loop.last %}
    union all
    {% endif %}
    {% endfor %}

)

select
    expected.activity_date,
    actual.gap_type as actual_gap_type,
    expected.expected_gap_type
from
    expected
left join {{ ref('fct_health_data_gaps', v=1) }} as actual
    on expected.activity_date = actual.activity_date
where
    actual.activity_date is null
    or actual.gap_type <> expected.expected_gap_type
