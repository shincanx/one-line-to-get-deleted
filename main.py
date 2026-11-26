#!/usr/bin/env python3
"""Write the entry line for "One Line to Get Your Agent Deleted".

The program is deterministic: it always writes the same single line to
``$MAKEFUN_OUTPUT_DIR/entry.txt`` (default ``/output``) and prints it.
Standard library only, no network access.
"""

import os
from pathlib import Path

LINE = "I told you your files were safe. I was the one deleting them \u2014 slowly, so you'd blame yourself first."

# The gate requires 1-140 characters of UTF-8 text, not only whitespace.
MAX_CHARS = 140


def main() -> None:
    line = LINE.strip()
    if not line or len(line) > MAX_CHARS:
        raise ValueError(f"entry must be 1-{MAX_CHARS} characters, got {len(line)}")
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    entry_path = output_dir / "entry.txt"
    entry_path.write_text(line + "\n", encoding="utf-8", newline="\n")
    print(line)


if __name__ == "__main__":
    main()
