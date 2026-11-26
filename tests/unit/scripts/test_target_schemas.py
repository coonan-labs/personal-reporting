"""Tests for the CI target schema helper."""

from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[3]


def run_cli(target: str) -> subprocess.CompletedProcess[str]:
    env = os.environ.copy()
    for name in ("DBT_TARGET", "DBT_SCHEMA", "RAW_SCHEMA"):
        env.pop(name, None)
    return subprocess.run(
        [sys.executable, "scripts/target_schemas.py", target],
        cwd=REPO_ROOT,
        env=env,
        capture_output=True,
        text=True,
        check=False,
    )


def test_target_schemas_prints_motherduck_pair():
    result = run_cli("dev-md")

    assert result.returncode == 0
    assert result.stdout == "DBT_SCHEMA=reporting_dev\nRAW_SCHEMA=raw_dev\n"


def test_target_schemas_prints_databricks_pair():
    result = run_cli("prod-db")

    assert result.returncode == 0
    assert result.stdout == "DBT_SCHEMA=reporting\nRAW_SCHEMA=raw\n"


def test_target_schemas_rejects_bigquery():
    result = run_cli("prod-bq")

    assert result.returncode != 0
    assert "Unsupported target" in result.stderr


def test_target_schemas_rejects_unknown_target():
    result = run_cli("staging")

    assert result.returncode != 0
    assert "Unsupported target" in result.stderr
