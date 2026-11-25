"""Snooze Button Roast — entry program (V3).

Writes a single roast to entry.txt: at 6 a.m. on a Saturday the alarm
screams like there is a flight to catch, when there is nowhere to be —
it has watched the same sleep-in every Saturday for a year, and it
rings anyway, proud of itself. The program enforces the bounty gate
(one line, 1-200 characters, no leading or trailing whitespace) and
verifies the write by reading the file back.

The joke is a scene with a witness: a time anchor (Saturday, 6 a.m.),
a false emergency (a flight to catch), a year of evidence that the
alarm has watched, and a final clause that gives the alarm a motive —
it is proud of itself for ringing, and it will be proud again next
Saturday.
"""

import os
import sys

LINE = "Saturday, 6 a.m. My alarm screamed like I had a flight to catch. I had nowhere to be. It knew — it has watched me sleep in every Saturday for a year — and it rang anyway, proud of itself."

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
