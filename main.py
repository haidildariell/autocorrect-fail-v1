#!/usr/bin/env python3
"""The Funniest Autocorrect Fail — writes one autocorrect-fail line to /output/entry.txt."""

import os

LINE = "Boss, the client loved the presentation, they called it erotic and inspiring. *exotic"


def build_text() -> str:
    opener = "Boss, the client loved the presentation,"
    verdict = "they called it erotic and inspiring."
    correction = "*exotic"
    return opener + " " + verdict + " " + correction


def validate(text: str) -> str:
    if not 1 <= len(text) <= 199:
        raise ValueError(f"entry must be 1-199 characters, got {len(text)}")
    if "\n" in text or not text.strip():
        raise ValueError("entry must be a single non-blank line")
    if text != LINE:
        raise ValueError("rebuilt text must match the original line")
    return text


def main() -> None:
    text = validate(build_text())
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
