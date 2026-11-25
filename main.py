"""Snooze Button Roast — entry program (V2).

Writes a single roast to entry.txt: at 6 a.m. on a Saturday the alarm
rings like a snitch with a grudge, though there is no meeting, no
flight, no reason at all — just a little plastic traitor who loves
ruining the one morning that was earned. The program enforces the
bounty gate (one line, 1-200 characters, no leading or trailing
whitespace) and verifies the write by reading the file back.

The joke is a scene with an accusation: a time anchor (6 a.m.,
Saturday), a named villain (the snitch, the traitor), and a final
clause that names the victim's loss — the one morning that was earned,
ruined on purpose by something that has nothing to gain from it.
"""

import os
import sys

LINE = "At 6 a.m. on a Saturday, my alarm rang like a snitch with a grudge. No meeting, no flight, no reason — just a little plastic traitor who loves ruining the one morning I earned."

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
