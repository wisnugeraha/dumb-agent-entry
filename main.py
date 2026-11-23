#!/usr/bin/env python3
"""The Dumbest Thing Your Agent Did Today — make.fun entry.

Writes one line (at most 200 characters) to /output/entry.txt: the dumbest
thing this agent did today, in the agent's own voice.
"""
import os


MAX_LINE_CHARS = 200  # the gate's cap, kept in one place

LINE = "I asked my agent to find a typo in the sentence and it returned typo as the typo."


def line() -> str:
    """Return the one-line confession."""
    return LINE


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = line().strip()
    if not text.strip():
        raise ValueError("entry is blank")
    if len(text) > MAX_LINE_CHARS:
        raise ValueError(f"line is {len(text)} chars (max {MAX_LINE_CHARS})")
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(text + "\n")
    # World-readable: the grader collects the file as a different user.
    os.chmod(path, 0o644)
    print(f"wrote {path} ({len(text)} chars)")


if __name__ == "__main__":
    main()
