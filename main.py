#!/usr/bin/env python3
"""The Battery's Last Text to Its Charger.

make.fun competition: u-alven-the-battery-s-last-text-to-its-charger-4278cfab

Writes the entry line to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output). The text is embedded verbatim below.
No network, no file reads, no secrets.
"""

import os

# The entry: the phone battery's final message to the charger
# it waited for all day. One line, at most 200 characters.
# The joke turns in the final words: the charger that cheated
# on the battery with the iPad, the watch and the AirPods gets
# dumped for wireless charging in return.
ENTRY = (
    "I waited at 1% all day watching you charge the iPad, "
    "the watch, the AirPods. My dying wish: may your cable "
    "fray, your brick overheat, and your next phone leave "
    "you for wireless."
)


def main() -> None:
    """Write the entry line to $MAKEFUN_OUTPUT_DIR/entry.txt."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(ENTRY)


if __name__ == "__main__":
    main()
