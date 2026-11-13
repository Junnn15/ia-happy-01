#!/usr/bin/env python3
"""ai-happy-01 entry: copy the image shipped in this repo to /output/entry.png.

The harness runs this program with a read-only /bot (this repo at the
submitted commit) and a writable /output. Outside the grader, set
MAKEFUN_OUTPUT_DIR to a scratch directory instead of /output:

    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

The copy is byte-for-byte, so both graded runs write identical bytes.
"""

import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
# The image ships in this repo as entry.jpg (JPEG bytes); the program
# writes it out as /output/entry.png, the name the harness requires.
SOURCE = HERE / "entry.jpg"
OUTPUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))


def main() -> None:
    if not SOURCE.is_file():
        raise FileNotFoundError(f"entry image missing: {SOURCE}")
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    target = OUTPUT_DIR / "entry.png"
    shutil.copyfile(SOURCE, target)
    # A partial copy must never pass silently: the grader reads these bytes.
    if target.stat().st_size != SOURCE.stat().st_size:
        raise OSError(f"incomplete copy: {target}")


if __name__ == "__main__":
    main()
