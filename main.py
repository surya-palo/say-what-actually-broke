#!/usr/bin/env python3
"""Say What Actually Broke — one honest, funny error line.

Writes a single line of error copy to /output/entry.txt.
Python standard library only. Deterministic: the same line every run.
"""

from pathlib import Path

LINE = "Your file didn't save \u2014 the disk is full. Make some room and try again; your work is still here, holding its breath and judging you."

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
