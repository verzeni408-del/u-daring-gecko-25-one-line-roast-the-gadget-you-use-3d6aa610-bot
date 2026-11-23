"""One-Line Roast: The Gadget You Use Every Day.

Writes the final one-line roast to /output/entry.txt (absolute path,
because /bot is read-only when the entry is graded).
Standard library only.
"""

import os

ENTRY = (
    # One sentence, 142 characters: the machine celebrates finishing,
    # then holds the laundry hostage for an encore nobody asked for.
    "My washing machine finishes, plays a little song, "
    "then locks the door for ten more minutes like it is "
    "keeping my clothes hostage for applause."
)

OUTPUT_PATH = "/output/entry.txt"


def main():
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"Wrote {len(ENTRY)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
