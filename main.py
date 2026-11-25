#!/usr/bin/env python3
"""The Tired Dark Lord: A 100-Word Villain Monologue.

Writes one monologue of about 100 words to /output/entry.txt.
Pure Python stdlib only. Byte-identical on every re-run.
"""

import os
import stat

ENTRY = (
    "Come in. Mind the step. It bites. I'm Vey. I had it mended twice. "
    "Sit, hero. Not the throne. The stool. The throne is for... posture.\n\n"
    "Forty years I've kept the marshlights burning, wick by wick, "
    "so the drowned road stays lit for the toll carts. "
    "Do you know what the toll buys? Lamp oil. It buys lamp oil.\n\n"
    "You came to break the curse. There is no curse. "
    "There is a ledger, a leaking roof, and a kingdom that forgot to send a second keeper.\n\n"
    "So. Swing your sword. But first, hold this lantern. It's heavier than it looks."
)


def main() -> None:
    text = ENTRY
    assert 1 <= len(text) <= 600, f"entry length {len(text)} outside 1..600"
    assert text.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
