"""Tests for Conventional Commit message validation."""

from __future__ import annotations

import io

import pytest

from scripts.check_conventional_commits import find_invalid_messages, main, validate_message


@pytest.mark.parametrize(
    "message",
    [
        "feat: add release workflow",
        "fix(dbt): align contract types",
        "chore(deps): bump actions/checkout",
        "feat(api)!: remove legacy endpoint",
        "revert: feat: add release workflow",
        "Merge pull request #172 from coonan-labs/feature",
        "Merge branch 'main' into feature",
        "Merge tag 'v1.2.3' into main",
        "chore(release): 1.2.3",
        "chore(release): 1.2.3-rc.1",
        "chore(release): 1.2.3+build.7",
    ],
)
def test_validate_message_accepts_conventional_and_merge_commits(message):
    assert validate_message(message) is None


@pytest.mark.parametrize(
    "message",
    [
        "",
        "Update documentation",
        "feature: missing valid type",
        "feat add missing colon",
        "feat:",
        "feat(): empty scope",
    ],
)
def test_validate_message_rejects_non_conventional_commits(message):
    assert validate_message(message) is not None


def test_find_invalid_messages_reports_each_invalid_message():
    errors = find_invalid_messages(["feat: ok", "not conventional", "fix: ok"])

    assert len(errors) == 1
    assert "not conventional" in errors[0]


def test_main_accepts_repeated_message_arguments(capsys):
    assert main(["--message", "feat: ok", "--message", "fix(ci): ok"]) == 0
    assert capsys.readouterr().err == ""


def test_main_reads_messages_from_stdin(monkeypatch, capsys):
    monkeypatch.setattr("sys.stdin", io.StringIO("feat: ok\nnot conventional\n"))

    assert main(["--stdin"]) == 1
    assert "not conventional" in capsys.readouterr().err
