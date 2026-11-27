"""Keep the dbt and dlt MotherDuck database normalization in sync."""

from __future__ import annotations

import re
from pathlib import Path

import pytest
from jinja2 import Template

from pipelines.runner import normalize_motherduck_database

REPO_ROOT = Path(__file__).resolve().parents[3]
PROFILE_PATH = REPO_ROOT / "dbt" / "profiles.yml"


def _profile_expression() -> str:
    text = PROFILE_PATH.read_text()
    match = re.search(r'path: "md:\{\{(.+?)\}\}"', text, re.DOTALL)
    assert match, "MotherDuck path expression not found in dbt/profiles.yml"
    return match.group(1).strip()


@pytest.mark.parametrize(
    "value",
    [
        None,
        "",
        "personal",
        "md:personal",
        "md://personal",
        "md:/personal",
        "  personal  ",
        "  md://personal  ",
        "md:foo",
    ],
)
def test_dbt_profile_normalization_matches_runner(value: str | None) -> None:
    def env_var(_name: str, default: str | None = None) -> str | None:
        return default if value is None else value

    rendered = Template("{{ " + _profile_expression() + " }}").render(env_var=env_var)

    assert rendered == normalize_motherduck_database(value)
