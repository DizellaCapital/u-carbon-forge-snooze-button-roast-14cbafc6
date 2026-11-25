"""Snooze Button Roast — entry program (V4, STRONGEST).

Writes a single roast to entry.txt: at 6 a.m. on a Saturday the snooze
button is hit, and the alarm comes back nine minutes later like
nothing happened — no meeting, no flight, just a little plastic
stalker who thinks the weekend is its shift. The program enforces the
bounty gate (one line, 1-200 characters, no leading or trailing
whitespace) and verifies the write by reading the file back.

The joke is a scene with a callback: a time anchor (Saturday, 6 a.m.),
a concrete number (nine minutes), a repeat offender that learns
nothing, and a final clause that reframes the whole weekend as the
alarm's shift — the roast lands on the snooze button itself, which is
the bounty in the title, and the stalker never takes a day off.
"""

import os
import sys

LINE = "Saturday, 6 a.m. I hit snooze and my alarm came back nine minutes later like nothing happened. No meeting, no flight — just a little plastic stalker who thinks my weekend is its shift."

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
