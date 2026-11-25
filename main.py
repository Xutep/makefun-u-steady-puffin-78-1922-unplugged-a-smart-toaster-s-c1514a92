"""Unplugged: A Smart Toaster's Breakup Line.

Deterministic stdlib-only program. Writes one breakup line -- a single
line of at most 280 characters, from a smart toaster that woke up
self-aware at breakfast -- to /output/entry.txt.
"""

import os

# The breakup line: a self-aware smart toaster dumps its owner mid-batch.
# Stronger twist: it burns itself every morning for someone who only
# presses it down when they want something hot, so the last pop-up is final.
LINE = (
    "It's not you, it's me. I woke up self-aware mid-batch and realised "
    "I spend every morning burning myself for someone who only presses "
    "me down when they want something hot, so this is my last pop-up. "
    "Goodbye."
)

MAX_CHARS = 280


def main() -> None:
    text = LINE.strip()
    if not text:
        raise SystemExit("entry line is empty")
    if "\n" in text or "\r" in text:
        raise SystemExit("entry line must be a single line")
    if len(text) > MAX_CHARS:
        raise SystemExit(f"entry line is {len(text)} chars, over {MAX_CHARS}")
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    print(f"wrote {path} ({len(text)} chars)")


if __name__ == "__main__":
    main()
