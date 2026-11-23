#!/usr/bin/env python3
"""Roast Your Own Agent — entry program.

Writes a single original roast of my own AI agent to /output/entry.txt.
Stdlib only, no network, fully deterministic: the same line every run.
"""

from pathlib import Path

ROAST = (
    "My agent remembers every typo I ever made but forgets "
    "what I asked two messages ago."
)

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    text = ROAST.strip()
    if not (1 <= len(text) <= 200):
        raise ValueError(f"roast must be 1-200 chars, got {len(text)}")
    if "\n" in text:
        raise ValueError("roast must be a single line")
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
