"""Validate that the dbt target and schema environment variables agree."""

from __future__ import annotations

import argparse
import os
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

from pipelines import DBT_TARGET  # noqa: E402
from pipelines.targets import validate_target  # noqa: E402


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--require-suffix",
        default=None,
        help="fail unless DBT_TARGET ends with this suffix (e.g. -md)",
    )
    args = parser.parse_args(argv)
    try:
        validate_target(
            os.getenv("DBT_TARGET") or DBT_TARGET,
            os.getenv("DBT_SCHEMA"),
            os.getenv("RAW_SCHEMA"),
        )
    except ValueError as exc:
        raise SystemExit(str(exc)) from exc
    if args.require_suffix:
        target = os.getenv("DBT_TARGET") or DBT_TARGET
        if not target.endswith(args.require_suffix):
            raise SystemExit(
                f"DBT_TARGET must end in {args.require_suffix!r} for this task (got {target!r})"
            )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
