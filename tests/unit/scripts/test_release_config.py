"""Tests for the python-semantic-release version stamping configuration."""

from __future__ import annotations

import tomllib
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parents[3]


def test_release_stamps_pyproject_and_dbt_project():
    pyproject = tomllib.loads((REPO_ROOT / "pyproject.toml").read_text())
    release = pyproject["tool"]["semantic_release"]

    assert "pyproject.toml:project.version" in release["version_toml"]
    assert "dbt/dbt_project.yml:version" in release["version_variables"]


def test_dbt_project_version_matches_pyproject_version():
    pyproject = tomllib.loads((REPO_ROOT / "pyproject.toml").read_text())
    dbt_project = yaml.safe_load((REPO_ROOT / "dbt" / "dbt_project.yml").read_text())

    assert str(dbt_project["version"]) == pyproject["project"]["version"]
