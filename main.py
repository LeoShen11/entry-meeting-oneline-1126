#!/usr/bin/env python3
"""The Meeting That Should Have Been One Line.

Writes the single sentence that could have replaced an entire pointless
meeting to $MAKEFUN_OUTPUT_DIR/entry.txt, then validates the output:
UTF-8, 1-200 characters, not only whitespace, exactly one line.
"""

import os
import sys

LINE = "This meeting could have been one email, and the email could have been silence."


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    out_path = os.path.join(out_dir, "entry.txt")

    # Own validation before writing: the gate requires 1-200 chars,
    # non-whitespace, a single line.
    if not (1 <= len(LINE) <= 200):
        print(f"line is {len(LINE)} chars, must be 1-200", file=sys.stderr)
        return 1
    if not LINE.strip():
        print("line is only whitespace", file=sys.stderr)
        return 1
    if "\n" in LINE.strip():
        print("line must be a single line", file=sys.stderr)
        return 1
    words = LINE.split()
    if len(words) > 30:
        print(f"line is {len(words)} words, must be at most 30", file=sys.stderr)
        return 1

    os.makedirs(out_dir, exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(LINE)

    # Read-back check: the file on disk must hold exactly the line.
    with open(out_path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != LINE:
        print("read-back mismatch", file=sys.stderr)
        return 1
    print(f"wrote {len(written)} chars to {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
