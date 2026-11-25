#!/usr/bin/env python3
"""Write the chosen fortune-cookie line to entry.txt.

The program takes no input and reads nothing from the network, the
environment beyond the output directory, or any other file. It writes
exactly one line, with no trailing newline, so the output file holds
precisely the fortune and nothing else.
"""

import os
from pathlib import Path

ENTRY = "Your future is bright, confident, and hallucinated."

# The gate requires UTF-8 text of 1 to 200 characters, not only
# whitespace, on a single line. Fail loudly rather than write an
# entry the gate would refuse.
assert ENTRY and not ENTRY.isspace(), "fortune must not be blank"
assert "\n" not in ENTRY and "\r" not in ENTRY, "fortune must be one line"
assert 1 <= len(ENTRY) <= 200, "fortune must be 1-200 characters"
ENTRY.encode("utf-8")


def main() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
