#!/usr/bin/env python3
"""Alien Field Notes: The Two Day Earth Review — one-line entry.

Writes an alien tourist's one-line review of planet Earth to
/output/entry.txt: one line, at most 200 characters, in the voice of
a visitor filing a travel review after a short stay.
"""

import os

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 200

# The line itself: it opens like any holiday review — gorgeous planet,
# stunning sunsets — then the complaint arrives sideways, in the flat
# observation that the locals spend a third of every trip unconscious
# and call it "sleep". The joke lands on the last four words, when the
# tourist gives the verdict and promises to come back anyway.
REVIEW_LINE = (
    "Gorgeous planet, but the locals spend a third of every trip "
    "unconscious and call it 'sleep'. Stunning sunsets, confusing "
    "priorities. Four stars, would orbit again."
)


def build_review_line() -> str:
    """Return the single-line review, enforcing the gate."""
    text = REVIEW_LINE.strip()
    if not 1 <= len(text) <= MAX_CHARS:
        raise ValueError(f"review line is {len(text)} chars, must be 1-200")
    if "\n" in text or "\r" in text:
        raise ValueError("review line must be a single line")
    return text


def main() -> None:
    text = build_review_line()
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as fh:
        fh.write(text)


if __name__ == "__main__":
    main()
