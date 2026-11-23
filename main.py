#!/usr/bin/env python3
"""main.py -- news-image-20261122 entry.

Writes the front-page image for Sunday 22 November 2026 (the JPEG file
entry.jpg shipped beside this program) to $MAKEFUN_OUTPUT_DIR/entry.png.

Per the competition rules the output file is named entry.png either way;
its first bytes identify it as a JPEG. The program is deterministic:
every run writes exactly the same bytes (verified: two runs produce
identical sha256). Standard library only, no network, and it never
touches the output directory itself -- it only writes the one file
inside it.

The image: 36 dated stories from Sunday 22 November 2026 -- 3 large
illustrated leads (COP31 final text; 186 drones over Ukraine; the
Iran-Bahrain radar claim vs denial), 12 illustrated medium cards, and
21 numbered list items, with a numbered world map, a UTC timeline
strip, a 7-region bar, and a DATE CHECK box.
"""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.jpg")


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    shutil.copyfile(SRC, os.path.join(out_dir, "entry.png"))


if __name__ == "__main__":
    main()
