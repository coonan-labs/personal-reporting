"""Validate commit messages against the Conventional Commits specification."""

from __future__ import annotations

import argparse
import re
import sys
from collections.abc import Iterable

CONVENTIONAL_TYPES = (
    "build",
    "chore",
    "ci",
    "docs",
    "feat",
    "fix",
    "perf",
    "refactor",
    "revert",
    "style",
    "test",
)

CONVENTIONAL_COMMIT_RE = re.compile(
    r"^(?P<type>" + "|".join(CONVENTIONAL_TYPES) + r")"
    r"(?:\((?P<scope>[A-Za-z0-9][A-Za-z0-9._/-]*)\))?"
    r"(?P<breaking>!)?: (?P<description>\S.*)$"
)
MERGE_COMMIT_RE = re.compile(r"^Merge (?:branch|pull request|remote-tracking branch) ")
RELEASE_COMMIT_RE = re.compile(r"^chore\(release\): \d+\.\d+\.\d+")


def validate_message(message: str) -> str | None:
    """Return an error message when ``message`` is not a Conventional Commit."""
    subject = message.strip().splitlines()[0] if message.strip() else ""
    if not subject:
        return "commit message is empty"
    if MERGE_COMMIT_RE.match(subject) or RELEASE_COMMIT_RE.match(subject):
        return None
    if CONVENTIONAL_COMMIT_RE.match(subject):
        return None
    return (
        f"{subject!r} is not a Conventional Commit; expected "
        "'<type>(<scope>): <description>' with type one of " + ", ".join(CONVENTIONAL_TYPES)
    )


def find_invalid_messages(messages: Iterable[str]) -> list[str]:
    """Return validation errors for every invalid message in ``messages``."""
    errors: list[str] = []
    for message in messages:
        if error := validate_message(message):
            errors.append(error)
    return errors


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--message",
        action="append",
        default=[],
        help="commit message to validate (repeatable)",
    )
    parser.add_argument(
        "--stdin",
        action="store_true",
        help="also read one commit subject per line from stdin",
    )
    args = parser.parse_args(argv)

    messages = list(args.message)
    if args.stdin:
        messages.extend(line for line in sys.stdin.read().splitlines() if line.strip())

    errors = find_invalid_messages(messages)
    if not errors:
        return 0
    for error in errors:
        print(f"error: {error}", file=sys.stderr)
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
