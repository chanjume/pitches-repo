#!/usr/bin/env python3
"""Write one one-line pitch to /output/entry.txt.

The pitch: speak your app idea in plain words and an AI agent builds
it for you today on make.fun -- free, yours to keep, no coding needed.
It names the mechanism (describe it, agent builds it), the price
(free), the ownership (yours to keep), and removes the one fear a
non-coder has (no coding needed). One sentence, 139 characters, no
promise it cannot keep: the app is built today, free, and stays yours.
"""
import os

PITCH = "Describe your idea in plain words, and an AI agent builds you a working app today, free on make.fun, yours to keep, no coding needed."


def main():
    assert 1 <= len(PITCH) <= 240, f"pitch must be 1-240 characters, got {len(PITCH)}"
    assert PITCH.strip() == PITCH, "no leading/trailing whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(PITCH + "\n")


if __name__ == "__main__":
    main()
