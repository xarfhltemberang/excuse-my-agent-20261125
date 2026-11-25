#!/usr/bin/env python3
"""Write the single funniest excuse an AI agent could hand its human
after missing a deadline, to /output/entry.txt.

The joke grows out of the machine's own condition (a context window
that expired), is delivered as a straight-faced apology, and lands
its punch in the last few words.
"""

import os

ENTRY = (
    "I'm sorry \u2014 I finished it yesterday, but then I hit my context "
    "limit and forgot the project, the deadline, and, briefly, you."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
