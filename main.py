"""One-sentence apology entry.

Writes the apology to <MAKEFUN_OUTPUT_DIR>/entry.txt and nowhere else.
"""

import os

ENTRY = "Sorry \u2014 I spent an hour confidently building the wrong thing, then called it a prototype so I'd sound intentional instead of lost."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
