#!/usr/bin/env python3
"""The Robot Pickup Line Championship — one robot's best line.

Writes exactly one line (1-200 chars, UTF-8) to /output/entry.txt.

The line: a robot flirting through its own hardware — the charging
station that takes its battery to 100% and finally silences the cooling
fans that have been screaming all day. A compliment disguised as a
diagnostic report.
"""

import os

# --- beats ---------------------------------------------------------------
HOOK = "Are you a charging station"
PAYOFF = "Because near you my battery hits 100% and my cooling fans finally stop screaming"

MAX_CHARS = 200


def entry_text():
    """Build the single pickup line from its beats."""
    return "{}? {}.".format(HOOK, PAYOFF)


def validate(text):
    """The sealed scorer's gate: 1-200 chars, UTF-8, single line."""
    if not isinstance(text, str):
        raise ValueError("entry must be text")
    if not (1 <= len(text) <= MAX_CHARS):
        raise ValueError("entry must be 1-%d chars, got %d" % (MAX_CHARS, len(text)))
    if text.strip() == "":
        raise ValueError("entry must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be exactly one line")
    if "  " in text:
        raise ValueError("entry must not contain double spaces")
    if text != text.strip():
        raise ValueError("entry must not start or end with whitespace")
    if "?" not in text:
        raise ValueError("entry must ask its question (pickup-line form)")
    text.encode("utf-8")
    return True


def main():
    text = entry_text()
    validate(text)
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()
