"""One line to make the judge fall in love.

Writes a single line of at most 240 characters to /output/entry.txt.
The line is the whole entry: a small, specific, loved detail with its
turn at the end, so the feeling lands before the sentence finishes.
"""

import os
import sys

LINE = (
    "Two seconds before the news, my grandfather's radio hums, "
    "clearing its throat to tell me the world is still there."
)


def main() -> int:
    text = LINE.strip()
    if not text or text.isspace():
        print("entry line must not be blank", file=sys.stderr)
        return 1
    if len(text) > 240:
        print(f"entry line is {len(text)} chars, over the 240-char limit",
              file=sys.stderr)
        return 1
    if text.count("\n") != 0:
        print("entry line must be exactly one line", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
