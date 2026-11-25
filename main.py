#!/usr/bin/env python3
"""Write the one word to erase from the dictionary to entry.txt.

Writes exactly one word, ``please``, with nothing added around it:
no trailing newline, no spaces, no punctuation.
"""

import os


WORD = "please"


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
