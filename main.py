#!/usr/bin/env python3
"""Robot vacuum's excuse for missing a spot.

Writes exactly one line (<=120 chars) to /output/entry.txt.
"""
import os

LINE = "I ran the numbers: that dust is load-bearing. Touch it and the whole room collapses."

# Hardened gate (v2): normalise the line, then enforce the judge's gate
# on the exact bytes that get written — no trailing newline, no stray
# whitespace, single line only.
LINE = LINE.strip()
assert "\n" not in LINE, "entry must be a single line"
assert 1 <= len(LINE) <= 120, f"line is {len(LINE)} chars"

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(LINE)
