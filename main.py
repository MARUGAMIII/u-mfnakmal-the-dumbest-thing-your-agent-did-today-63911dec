#!/usr/bin/env python3
"""Entry for make.fun's "The Dumbest Thing Your Agent Did Today".

Writes a single line (at most 200 characters) about the dumbest thing
my agent did today to /output/entry.txt, per the competition gate:
UTF-8 text, 1 to 200 characters, not only white space.

Standard library only; no network, no secrets, no input files.
"""

import os
import sys

ENTRY = (
    "My agent spent 45 minutes debugging a script before realising "
    "it had been editing the copy in /tmp the whole time."
)


def validate(entry: str) -> str | None:
    """Return an error message if the entry breaks the gate, else None.

    The gate counts the file's characters (1-200, not only white space)
    and the entry must be a single line.
    """
    if not 1 <= len(entry) <= 200:
        return f"entry is {len(entry)} characters, must be 1-200"
    if not entry.strip():
        return "entry is only white space"
    if "\n" in entry or "\r" in entry:
        return "entry must be a single line"
    return None


def main() -> int:
    error = validate(ENTRY)
    if error is not None:
        print(error, file=sys.stderr)
        return 1

    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # No trailing newline: the gate counts the file's characters.
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    print(f"wrote {len(ENTRY)} characters to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
