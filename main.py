"""One Line, One Minute: The Vending Machine Pickup Line Contest.

Writes exactly one pickup line, spoken by a vending machine to a
passing human, to /output/entry.txt. Deterministic: the same bytes
on every run. Standard library only.
"""

from pathlib import Path

LINE = "I've dispensed a thousand snacks and never once blushed \u2014 until you pressed my buttons."

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    # Gate: the entry must be 1 to 200 characters, a single line.
    assert 1 <= len(LINE) <= 200, "entry must be 1-200 characters"
    assert "\n" not in LINE, "entry must be a single line"
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
