#!/usr/bin/env python3
"""Two Lines to Your Past Self.

Writes a two-line warning to entry.txt: line 1 warns the writer's past
self about one specific moment in a single sentence; line 2 says in one
sentence why that moment mattered and what changed because of it.
Pure Python standard library only.
"""

import os

LINE_1 = "Don't say \"I'm fine\" when the doctor asks how the headaches have been on the morning of March 3rd."
LINE_2 = "That lie delays your treatment by a year, and that stolen year is the one your daughter takes her first steps in."

TEXT = LINE_1 + "\n" + LINE_2 + "\n"


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
