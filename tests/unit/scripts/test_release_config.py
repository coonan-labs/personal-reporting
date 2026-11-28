"""Tests for the python-semantic-release version stamping configuration."""

from __future__ import annotations

import shutil
import tomllib
from pathlib import Path

import yaml
from semantic_release.version.declaration import (
    PatternVersionDeclaration,
    TomlVersionDeclaration,
)
from semantic_release.version.version import Version

from scripts.check_conventional_commits import CONVENTIONAL_TYPES

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


def test_uv_lock_project_version_matches_pyproject_version():
    pyproject = tomllib.loads((REPO_ROOT / "pyproject.toml").read_text())
    lock = tomllib.loads((REPO_ROOT / "uv.lock").read_text())
    project_package = next(
        package for package in lock["package"] if package["name"] == pyproject["project"]["name"]
    )

    assert project_package["version"] == pyproject["project"]["version"]


def test_release_refreshes_the_lockfile():
    pyproject = tomllib.loads((REPO_ROOT / "pyproject.toml").read_text())
    release = pyproject["tool"]["semantic_release"]

    assert release["build_command"] == "uv lock"
    assert "uv.lock" in release["assets"]


def test_conventional_types_match_semantic_release_parser():
    pyproject = tomllib.loads((REPO_ROOT / "pyproject.toml").read_text())
    allowed_tags = pyproject["tool"]["semantic_release"]["commit_parser_options"]["allowed_tags"]

    assert sorted(allowed_tags) == sorted(CONVENTIONAL_TYPES)


def test_semantic_release_stamps_both_version_files(tmp_path, monkeypatch):
    pyproject = tomllib.loads((REPO_ROOT / "pyproject.toml").read_text())
    release = pyproject["tool"]["semantic_release"]
    new_version = Version.parse("9.8.7")

    (tmp_path / "dbt").mkdir()
    shutil.copy(
        REPO_ROOT / "dbt" / "dbt_project.yml",
        tmp_path / "dbt" / "dbt_project.yml",
    )
    shutil.copy(REPO_ROOT / "pyproject.toml", tmp_path / "pyproject.toml")
    monkeypatch.chdir(tmp_path)

    for definition in release["version_toml"]:
        declaration = TomlVersionDeclaration.from_string_definition(definition)
        assert declaration.update_file_w_version(new_version) is not None

    for definition in release["version_variables"]:
        declaration = PatternVersionDeclaration.from_string_definition(
            definition, release["tag_format"]
        )
        assert declaration.update_file_w_version(new_version) is not None

    stamped_pyproject = tomllib.loads((tmp_path / "pyproject.toml").read_text())
    assert stamped_pyproject["project"]["version"] == "9.8.7"

    stamped_dbt = yaml.safe_load((tmp_path / "dbt" / "dbt_project.yml").read_text())
    assert str(stamped_dbt["version"]) == "9.8.7"
