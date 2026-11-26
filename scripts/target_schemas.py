"""Print DBT_SCHEMA/RAW_SCHEMA assignments for a supported target.

CI uses this to derive schemas from ``pipelines.targets.TARGET_SCHEMAS``
instead of duplicating the mapping in workflow YAML. BigQuery targets are
excluded; only Databricks (``*-db``) and MotherDuck (``*-md``) targets are
accepted.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

from pipelines.targets import get_target_schemas  # noqa: E402

ALLOWED_SUFFIXES = ("-md", "-db")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("target", help="Databricks (*-db) or MotherDuck (*-md) target")
    args = parser.parse_args(argv)

    if not args.target.endswith(ALLOWED_SUFFIXES):
        raise SystemExit(
            f"Unsupported target {args.target!r}; choose a Databricks (*-db) "
            "or MotherDuck (*-md) target"
        )

    try:
        dbt_schema, raw_schema = get_target_schemas(args.target)
    except ValueError as exc:
        raise SystemExit(str(exc)) from exc

    print(f"DBT_SCHEMA={dbt_schema}")
    print(f"RAW_SCHEMA={raw_schema}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
