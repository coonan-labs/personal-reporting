"""Publish the latest snapshot of a MotherDuck database to a share.

MotherDuck shares are point-in-time snapshots: consumers only see data as
of the share's last update. Run this after a prod-md load so share
consumers see the new data without recreating their database from the
share URL.

Requires ``MOTHERDUCK_TOKEN`` in the environment (injected by ``op run``
in CI from the prod 1Password environment). The token must belong to the
account that owns the share — the CI service account.
"""

from __future__ import annotations

import argparse
import os
import re
import sys

import duckdb

DEFAULT_DATABASE = "personal"
DEFAULT_SHARE = "personal-share"
_NAME_RE = re.compile(r"^[A-Za-z0-9_-]+$")


def update_share(*, database: str, share: str, token: str) -> None:
    """Attach to ``database`` as its owner and publish ``share``."""
    for label, value in (("database", database), ("share", share)):
        if not _NAME_RE.match(value):
            raise SystemExit(f"Invalid {label} name {value!r}: use letters, digits, '-' or '_'")

    con = duckdb.connect()
    try:
        # LOAD autoinstalls the extension. SET must precede the attach,
        # and the token is bound as a parameter so it never appears in a
        # SQL string (and so cannot leak into logs or error messages).
        # This is the same statement sequence dlt's MotherDuck
        # destination uses.
        con.execute("LOAD motherduck")
        con.execute("SET motherduck_token=?", [token])
        con.execute(f"ATTACH 'md:{database}' AS \"{database}\"")
        con.execute(f'USE "{database}"')
        con.execute(f'UPDATE SHARE "{share}"')
    finally:
        con.close()


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--database",
        default=os.environ.get("DESTINATION__MOTHERDUCK__CREDENTIALS__DATABASE", DEFAULT_DATABASE),
        help="MotherDuck database the share is from (default: %(default)s)",
    )
    parser.add_argument(
        "--share",
        default=DEFAULT_SHARE,
        help="Share name to update (default: %(default)s)",
    )
    args = parser.parse_args(argv)

    token = os.environ.get("MOTHERDUCK_TOKEN")
    if not token:
        print("MOTHERDUCK_TOKEN is not set", file=sys.stderr)
        return 1

    update_share(database=args.database, share=args.share, token=token)
    print(f"Updated share {args.share} for database {args.database}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
