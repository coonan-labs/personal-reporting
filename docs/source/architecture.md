# Architecture and Data Flow

High-level architecture:

Notion / HubSpot / Google Health APIs
    ↓ (dlt pipelines → MotherDuck raw schema; Databricks retained for transition)
dbt Staging (views) → dbt Intermediate → dbt Marts (tables)
    ↓ MetricFlow semantic layer

## Components

- dlt: extraction and direct-loading into MotherDuck. Keeps incremental state and supports full refreshes; Databricks remains a transition/rollback destination.
- dbt: transformations layered into staging, intermediate, and marts. Seeds and macros enable local dev.
- MotherDuck: primary data warehouse; dbt transforms and marts run against the `*-md` targets. Databricks Unity Catalog remains a transition/rollback destination, and BigQuery targets remain a rollback path. DuckDB is used for the local `mock` target.
- GitHub Actions: scheduling and orchestration for weekly runs.

## Operational guidance

- Ingest first, then run dbt transforms (workflows configured to enforce this order).
- Use `mise run dbt-build` to validate transformations against the default `dev-md` (MotherDuck) target, or set `DBT_TARGET` to a `*-db` target for Databricks.
- Use `mise run dbt-build-mock` for local testing with CSV fixtures in DuckDB.
- Maintain group_connect_cadence.csv as the single source of truth for group tier cadence targets.

## Where to look in the repo

- dlt pipelines: `pipelines/`
- dbt project: `dbt/`
- CI: `.github/workflows/`
- Agentic workflows: `.github/aw/` and `.github/workflows/*.lock.yml`
