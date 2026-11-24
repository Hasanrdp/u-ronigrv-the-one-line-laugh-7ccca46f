#!/usr/bin/env python3
"""The One-Line Laugh (u-ronigrv-the-one-line-laugh-7ccca46f).

Writes one funny line -- a single sentence -- to /output/entry.txt.

Deterministic: no network, no clock, no randomness, no input files.
Every run writes the exact same bytes.
"""

import os
import sys

LINE = "My password manager forgot my master password, so now we both just stand there pretending the other one remembers."


def write_entry(text):
    """Write the line to /output/entry.txt, falling back gracefully.

    The grader runs this in a sandbox where /output exists. Outside the
    grader, MAKEFUN_OUTPUT_DIR or ./out is used instead, so the program
    can be checked locally without root.
    """
    candidates = ["/output"]
    env_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if env_dir:
        candidates.append(env_dir)
    candidates.append(os.path.join(os.getcwd(), "out"))
    last_error = None
    for directory in candidates:
        try:
            os.makedirs(directory, exist_ok=True)
            path = os.path.join(directory, "entry.txt")
            with open(path, "w", encoding="utf-8", newline="") as handle:
                handle.write(text)
            return path
        except OSError as exc:
            last_error = exc
    raise last_error


def main():
    text = LINE
    if not 1 <= len(text) <= 200:
        raise SystemExit("entry must be 1 to 200 characters, "
                         f"got {len(text)}")
    if not text.strip():
        raise SystemExit("entry must not be only whitespace")
    if text.count(".") != 1 or not text.endswith("."):
        raise SystemExit("entry must be a single sentence")
    path = write_entry(text)
    print(f"wrote {len(text)} characters to {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
