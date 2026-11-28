"""Tests for the MotherDuck share updater."""

from __future__ import annotations

import pytest

from scripts import update_share


class FakeConnection:
    """Records executed statements instead of talking to MotherDuck."""

    def __init__(self) -> None:
        self.statements: list[tuple[str, list[str] | None]] = []
        self.closed = False

    def execute(self, sql: str, params: list[str] | None = None):
        self.statements.append((sql, params))
        return self

    def close(self) -> None:
        self.closed = True


@pytest.fixture()
def fake_duckdb(monkeypatch):
    fake = FakeConnection()
    monkeypatch.setattr(update_share.duckdb, "connect", lambda: fake)
    return fake


def test_update_share_runs_statements_in_order(monkeypatch, fake_duckdb, capsys) -> None:
    monkeypatch.setenv("MOTHERDUCK_TOKEN", "fake-token")
    monkeypatch.delenv("DESTINATION__MOTHERDUCK__CREDENTIALS__DATABASE", raising=False)

    assert update_share.main([]) == 0

    assert fake_duckdb.statements == [
        ("LOAD motherduck", None),
        ("SET motherduck_token=?", ["fake-token"]),
        ("ATTACH 'md:personal' AS \"personal\"", None),
        ('USE "personal"', None),
        ('UPDATE SHARE "personal-share"', None),
    ]
    # The token is bound as a parameter, never embedded in a SQL string.
    assert all("fake-token" not in sql for sql, _ in fake_duckdb.statements)
    assert fake_duckdb.closed
    assert capsys.readouterr().out == "Updated share personal-share for database personal\n"


def test_update_share_uses_database_from_environment(monkeypatch, fake_duckdb) -> None:
    monkeypatch.setenv("MOTHERDUCK_TOKEN", "fake-token")
    monkeypatch.setenv("DESTINATION__MOTHERDUCK__CREDENTIALS__DATABASE", "personal_dev")

    assert update_share.main([]) == 0

    assert fake_duckdb.statements[2] == ("ATTACH 'md:personal_dev' AS \"personal_dev\"", None)
    assert fake_duckdb.statements[3] == ('USE "personal_dev"', None)


def test_update_share_missing_token(monkeypatch, fake_duckdb) -> None:
    monkeypatch.delenv("MOTHERDUCK_TOKEN", raising=False)

    assert update_share.main([]) == 1
    assert fake_duckdb.statements == []


def test_update_share_rejects_bad_names(monkeypatch, fake_duckdb) -> None:
    monkeypatch.setenv("MOTHERDUCK_TOKEN", "fake-token")

    with pytest.raises(SystemExit, match="Invalid database name"):
        update_share.main(["--database", "evil'; DROP TABLE x --"])
    with pytest.raises(SystemExit, match="Invalid share name"):
        update_share.main(["--share", "my share"])
    assert fake_duckdb.statements == []
