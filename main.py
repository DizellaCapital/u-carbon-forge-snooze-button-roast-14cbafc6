"""Snooze Button Roast — entry program (V1).

Writes a single roast to entry.txt: at 6 a.m. on a Saturday the alarm
goes off like the building is on fire, when nothing is burning except
the weekend — and the little coward on the nightstand knows it. The
program enforces the bounty gate (one line, 1-200 characters, no
leading or trailing whitespace) and verifies the write by reading the
file back.

The joke is a scene, not a quip: a time anchor (Saturday, 6 a.m.), a
concrete object (the nightstand), and a final clause that reframes the
alarm as a coward that knows exactly what it is doing — it rang on
purpose, and it knew there was no fire.
"""

import os
import sys

LINE = "Saturday, 6 a.m. My alarm went off like the building was on fire. Nothing was burning — just my weekend, and the little coward on the nightstand knew it."

MAX_CHARS = 200


def problems(line):
    """Collect every way the line breaks the bounty limits, if any."""
    found = []
    if not line or line.strip() != line:
        found.append("empty or padded")
    if len(line) > MAX_CHARS:
        found.append("over 200 characters")
    if "\n" in line or "\r" in line:
        found.append("more than one line")
    if "\t" in line:
        found.append("contains a tab")
    return found


def main():
    bad = problems(LINE)
    if bad:
        print("invalid entry: " + "; ".join(bad), file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(LINE)
    with open(path, encoding="utf-8") as handle:
        if handle.read() != LINE:
            print("read-back mismatch", file=sys.stderr)
            return 1
    print("wrote %s (%d characters)" % (path, len(LINE)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
