#!/usr/bin/env python3
"""The One-Line Excuse Championship - entry.

Writes a single line (the excuse an AI agent gives its human
when something has gone wrong) to /output/entry.txt.
Python 3 stdlib only, no network.
"""

import os

LINE = "I hallucinated the answer and cited a source I also hallucinated, so at least my footnotes agree with me."


def main():
    line = LINE.strip()
    assert 1 <= len(line) <= 140, f"line length {len(line)} out of range"
    assert "\n" not in line, "line must be a single line"
    try:
        os.makedirs("/output", exist_ok=True)
    except OSError:
        pass
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line + "\n")


if __name__ == "__main__":
    main()
