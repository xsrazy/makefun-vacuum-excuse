"""make.fun one-liner entry: The Robot Vacuum's Best Excuse.

Writes a single original line, the funniest excuse a robot vacuum could
offer for missing a spot, to $MAKEFUN_OUTPUT_DIR/entry.txt as bytes,
with no trailing newline.
"""

import os

LINE = "I didn't miss that spot, I was giving it space. It looked like it needed time to process being dirty."

assert 1 <= len(LINE) <= 140, "line must be 1-140 characters"
assert LINE.strip(), "line must not be blank"


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "wb") as f:
        f.write(LINE.encode("utf-8"))


if __name__ == "__main__":
    main()
