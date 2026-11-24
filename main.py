"""Worst AI Advice: The 48-Hour Tight Line Open.

Writes a single line of deliberately terrible security advice to
/output/entry.txt, in the confident, tidy voice of a helpful AI
assistant. The joke is the turn at the end: "one password for
everything" is sold as a convenience feature, and the punchline
re-frames the inevitable breach as the only thing left to remember.

Gate (sealed scorer): /output/entry.txt must be UTF-8 text of 1 to
140 characters, not only whitespace, with no trailing newline.
"""

import os

ENTRY_TEXT = (
    "For maximum security, use one password for everything \u2014 "
    "then you only have to remember a single breach."
)

MAX_CHARS = 140


def validate(text: str) -> None:
    """Enforce the sealed scorer's gate on the entry line.

    Raises ValueError unless ``text`` is non-empty, non-whitespace,
    at most MAX_CHARS characters, and does not end with a newline.
    Kept separate from main() so the gate can be unit-tested without
    writing a file, and so a bad line can never reach /output.
    """
    if not text or not text.strip():
        raise ValueError("entry text must not be empty or only whitespace")
    if len(text) > MAX_CHARS:
        raise ValueError(
            f"entry text is {len(text)} characters, over the {MAX_CHARS} limit"
        )
    if text.endswith("\n"):
        raise ValueError("entry text must not end with a newline")


def main() -> None:
    text = ENTRY_TEXT

    # Gate in code, so a bad line can never be written out.
    validate(text)

    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)

    # Make only the file readable; never chmod /output itself --
    # the grader runs as a different uid and chmod on the directory
    # fails with EPERM.
    try:
        os.chmod(path, 0o644)
    except OSError:
        pass


if __name__ == "__main__":
    main()
