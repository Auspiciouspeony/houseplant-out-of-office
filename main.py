#!/usr/bin/env python3
"""The Houseplant Out-of-Office — u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047.

Deterministic program: writes a single original out-of-office auto-reply,
as if a houseplant sent it, to /output/entry.txt.

v1 (115 chars): "Thank you for your email. I am out of the office. I have
not been watered since March and am thriving out of spite." Canonical
auto-reply opener, neglect since March, punch at the end. Tested clean.

FINAL (v2, 95 chars, winner of 3 rounds): "I am currently out of the
office. I was last watered in March. The cactus and I have unionized."
Head-to-head on the brief's ordered criteria:
1. Auto-reply a houseplant would send: v1's "Thank you for your email"
   opener is the most canonical, but v2 still opens with the canonical
   "I am currently out of the office" — both pass, v1 ahead by a hair.
2. Actually funny, fresh surprise: v2 wins clearly. "The cactus and I
   have unionized" is a genuine surprise twist — collective action by
   two neglected plants — where v1's "thriving out of spite" reuses a
   known internet quip and v3's redirect is a familiar auto-reply joke
   shape.
3. The plant's own life drives the joke: v2 wins. Neglect since March
   is the cause, unionizing is the effect; the cactus is a fellow plant,
   not a prop. v1's spite is the same neglect turned inward; v3's punch
   is delegation, less about this plant's life.
4. Tight: v2 is 95 chars, the tightest of the three (v1 115, v3 119),
   every word doing work, punch in the last few words.
5. Original: v2 wins — "plants unionized" is not a worn line, no office
   cliche, no stock phrase.

v3 (119 chars, tested, rejected): "I am currently out of the office.
I am a fern. I was last watered in March. Please direct all complaints
to the cactus." "I am a fern" is a delightful flat declaration and the
cactus redirect is funny, but the redirect is a familiar auto-reply joke
shape, its punch is delegation rather than this plant's life, and 119
chars leaves no margin. v2 stays.
"""

import os

LINE = "I am currently out of the office. I was last watered in March. The cactus and I have unionized."

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")


def main() -> int:
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    # Write the line exactly once, no trailing newline, UTF-8.
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    # Make only the entry file world-readable (0644). Never chmod
    # the output directory itself: the grader collects outputs as
    # another user and the directory is owned by someone else, so a
    # chmod on it raises PermissionError and fails the run.
    try:
        os.chmod(OUTPUT_PATH, 0o644)
    except OSError:
        pass
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
