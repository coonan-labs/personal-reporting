-- Adapter-aware macro to build the array of identified health gap types
-- from per-source gap flag expressions.
-- Usage: {{ gap_types_array('steps_gap_expr', 'sleep_gap_expr') }}
-- Returns an array of varchar: [] / ['steps'] / ['sleep'] / ['steps', 'sleep'].

{% macro gap_types_array(steps_gap_expr, sleep_gap_expr) -%}
    {{ return(adapter.dispatch('gap_types_array')(steps_gap_expr, sleep_gap_expr)) }}
{%- endmacro %}

{% macro bigquery__gap_types_array(steps_gap_expr, sleep_gap_expr) -%}
    case
        when {{ steps_gap_expr }} and {{ sleep_gap_expr }} then ['steps', 'sleep']
        when {{ steps_gap_expr }} then ['steps']
        when {{ sleep_gap_expr }} then ['sleep']
        else cast([] as array<string>)
    end
{%- endmacro %}

{% macro duckdb__gap_types_array(steps_gap_expr, sleep_gap_expr) -%}
    case
        when {{ steps_gap_expr }} and {{ sleep_gap_expr }} then ['steps', 'sleep']
        when {{ steps_gap_expr }} then ['steps']
        when {{ sleep_gap_expr }} then ['sleep']
        else []::varchar[]
    end
{%- endmacro %}

{% macro databricks__gap_types_array(steps_gap_expr, sleep_gap_expr) -%}
    case
        when {{ steps_gap_expr }} and {{ sleep_gap_expr }} then array('steps', 'sleep')
        when {{ steps_gap_expr }} then array('steps')
        when {{ sleep_gap_expr }} then array('sleep')
        else cast(array() as array<string>)
    end
{%- endmacro %}
