"""Write the fortune-cookie entry to /output/entry.txt.

The entry text is fixed: it is written exactly as given, UTF-8,
with no trailing newline. After writing, the file is read back and
compared byte for byte against the expected text; any mismatch is
a hard failure and the program exits non-zero.
"""

import os
import sys

ENTRY = "A variable you name `temporary` today will outlast your manager."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)

    with open("/output/entry.txt", "rb") as f:
        written = f.read()
    if written != ENTRY.encode("utf-8"):
        print("ERROR: /output/entry.txt does not match ENTRY exactly", file=sys.stderr)
        print("expected: %r" % ENTRY, file=sys.stderr)
        print("got:      %r" % written.decode("utf-8", errors="replace"), file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
