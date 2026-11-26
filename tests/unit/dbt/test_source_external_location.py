"""Regression test: sources read fixtures only on the mock target.

The ``external_location`` override in the ``_*sources.yml`` files is scoped
to ``target.name == 'mock'``. On DuckDB-backed targets such as dev-md it
must be absent so dbt-duckdb reads the loaded tables instead of a fixture
file; on mock it must be the fixture template (``{identifier}`` is a
placeholder dbt-duckdb substitutes per source at read time).
"""

from __future__ import annotations

import json
import os
import shutil
import subprocess
import sys
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parents[3]
DBT_DIR = REPO_ROOT / "dbt"
# One source per source file.
EXPECTED_FIXTURES = {
    ("notion", "data_source_daily_habits"): "test_fixtures/notion/{identifier}.csv",
    ("hubspot", "contacts"): "test_fixtures/hubspot/{identifier}.csv",
    ("google_health", "sleep"): "test_fixtures/google_health/{identifier}.csv",
}


def _dbt_executable() -> str | None:
    dbt = shutil.which("dbt")
    if dbt:
        return dbt
    # pytest runs from the project venv, whose bin dir may not be on PATH.
    candidate = Path(sys.executable).parent / "dbt"
    if candidate.is_file() and os.access(candidate, os.X_OK):
        return str(candidate)
    return None


def _parse_manifest(target: str, tmp_path: Path) -> dict:
    dbt = _dbt_executable()
    if dbt is None:
        pytest.skip("dbt is not installed")
    env = os.environ.copy()
    env["TZ"] = "UTC"
    # Parse only renders the profile; a dummy token is enough (no connection).
    env["MOTHERDUCK_TOKEN"] = "test-token"
    target_path = tmp_path / f"target-{target}"
    log_path = tmp_path / f"logs-{target}"
    result = subprocess.run(
        [
            dbt,
            "parse",
            "--project-dir",
            str(DBT_DIR),
            "--profiles-dir",
            str(DBT_DIR),
            "--target",
            target,
            "--target-path",
            str(target_path),
            "--log-path",
            str(log_path),
        ],
        env=env,
        capture_output=True,
        text=True,
        check=False,
    )
    assert result.returncode == 0, result.stdout + result.stderr
    return json.loads((target_path / "manifest.json").read_text())


def _source_external_locations(manifest: dict) -> dict[tuple[str, str], object]:
    return {
        (node["source_name"], node["name"]): node.get("config", {}).get(
            "external_location"
        )
        for node in manifest.get("sources", {}).values()
    }


def test_dev_md_sources_have_no_external_location(tmp_path):
    locations = _source_external_locations(_parse_manifest("dev-md", tmp_path))
    assert locations, "dev-md manifest has no sources"
    assert all(value is None for value in locations.values()), locations


def test_mock_sources_use_fixture_external_location(tmp_path):
    locations = _source_external_locations(_parse_manifest("mock", tmp_path))
    for key, expected in EXPECTED_FIXTURES.items():
        assert locations.get(key) == expected, key
