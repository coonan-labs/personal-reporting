"""Tests for target/schema environment validation."""

from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path

import pytest

from pipelines.targets import validate_ingestion_target, validate_target

REPO_ROOT = Path(__file__).resolve().parents[3]


@pytest.mark.parametrize(
    ("target", "schema", "raw_schema"),
    [
        ("dev-db", "reporting_dev", "raw_dev"),
        ("dev-bq", "reporting_dev", "raw_dev"),
        ("dev-md", "reporting_dev", "raw_dev"),
        ("test-db", "reporting_test", "raw_test"),
        ("test-bq", "reporting_test", "raw_test"),
        ("test-md", "reporting_test", "raw_test"),
        ("prod-db", "reporting", "raw"),
        ("prod-bq", "reporting", "raw"),
        ("prod-md", "reporting", "raw"),
        ("mock", "reporting_dev", "raw_dev"),
    ],
)
def test_validate_target_accepts_matching_schemas(target, schema, raw_schema):
    validate_target(target, schema, raw_schema)


def test_validate_target_rejects_unknown_target():
    with pytest.raises(ValueError, match="DBT_TARGET must be one of"):
        validate_target("staging", "reporting_dev", "raw_dev")


def test_validate_target_rejects_mismatched_schemas():
    with pytest.raises(ValueError, match="requires DBT_SCHEMA=reporting"):
        validate_target("prod-db", "reporting_dev", "raw_dev")


def run_cli(args: list[str] | None = None, **overrides: str) -> subprocess.CompletedProcess[str]:
    env = os.environ.copy()
    for name in ("DBT_TARGET", "DBT_SCHEMA", "RAW_SCHEMA"):
        env.pop(name, None)
    env.update(overrides)
    return subprocess.run(
        [sys.executable, "scripts/validate_target.py", *(args or [])],
        cwd=REPO_ROOT,
        env=env,
        capture_output=True,
        text=True,
        check=False,
    )


def test_validate_target_cli_succeeds_for_matching_schemas():
    result = run_cli(
        DBT_TARGET="prod-db",
        DBT_SCHEMA="reporting",
        RAW_SCHEMA="raw",
    )

    assert result.returncode == 0
    assert result.stderr == ""


def test_validate_target_cli_fails_for_mismatched_schemas():
    result = run_cli(
        DBT_TARGET="prod-db",
        DBT_SCHEMA="reporting_dev",
        RAW_SCHEMA="raw_dev",
    )

    assert result.returncode != 0
    assert "requires DBT_SCHEMA=reporting" in result.stderr


def test_validate_target_cli_require_suffix_accepts_motherduck_target():
    result = run_cli(
        ["--require-suffix=-md"],
        DBT_TARGET="dev-md",
        DBT_SCHEMA="reporting_dev",
        RAW_SCHEMA="raw_dev",
    )

    assert result.returncode == 0
    assert result.stderr == ""


def test_validate_target_cli_require_suffix_rejects_databricks_target():
    result = run_cli(
        ["--require-suffix=-md"],
        DBT_TARGET="dev-db",
        DBT_SCHEMA="reporting_dev",
        RAW_SCHEMA="raw_dev",
    )

    assert result.returncode != 0
    assert "must end in '-md'" in result.stderr


def test_validate_ingestion_target_rejects_bigquery_target():
    with pytest.raises(ValueError, match="cannot be used for pipeline ingestion"):
        validate_ingestion_target("prod-bq", "reporting", "raw")


def test_validate_ingestion_target_accepts_motherduck_target():
    validate_ingestion_target("dev-md", "reporting_dev", "raw_dev")
    validate_ingestion_target("prod-md", "reporting", "raw")


def test_validate_ingestion_target_accepts_mock():
    validate_ingestion_target("mock", "reporting_dev", "raw_dev")
