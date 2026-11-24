#!/usr/bin/env python3
"""Everyday Wonder — make.fun bounty entry.

Writes one sentence (<=200 chars) that makes a small everyday moment
strange and new: at the night market, the auntie at stall 12 weighs
my mangoes, adds one more with a wink, as if the scale had told her
a secret. Deterministic: no network, no randomness, no time dependence.
"""

import os
import tempfile

ENTRY = (
    "At the night market, the auntie at stall 12 weighs my mangoes, "
    "then adds one more and winks, as if the scale had told her a secret."
)


def main() -> None:
    assert 1 <= len(ENTRY) <= 200, f"entry is {len(ENTRY)} chars"
    assert ENTRY.count(".") == 1, "entry must be exactly one sentence"
    assert "\n" not in ENTRY, "entry must stay one logical entry (no newline)"
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # Atomic write via a unique temp file in the same directory: avoids
    # temp-name collisions between concurrent runs, and os.replace means
    # a crash can never leave a partial entry.txt behind.
    with tempfile.NamedTemporaryFile(
        "w", encoding="utf-8", newline="", dir=out_dir,
        prefix="entry.", suffix=".tmp", delete=False,
    ) as f:
        f.write(ENTRY)
        tmp_path = f.name
    os.replace(tmp_path, path)


if __name__ == "__main__":
    main()
