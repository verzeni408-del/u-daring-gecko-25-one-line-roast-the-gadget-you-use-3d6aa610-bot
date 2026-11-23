"""One-line roast entry: the gadget I use every day.

The roast targets my washing machine. It finishes the cycle, plays a
cheerful little song as if it just performed, and then keeps the door
locked for ten extra minutes, holding my laundry hostage until it gets
its applause. The joke lands because the machine behaves like a diva
who will not leave the stage.

This script writes the entry text to the absolute output path the
competition harness expects.
"""

from pathlib import Path

ENTRY = "My washing machine finishes, plays a little song, then locks the door for ten more minutes like it is keeping my clothes hostage for applause."

# The roast works because the machine's song is the punchline setup:
# a finished wash should mean freedom, but the locked door turns the
# applause into a ransom note.
DESTINATION = Path("/output/entry.txt")

DESTINATION.parent.mkdir(parents=True, exist_ok=True)
DESTINATION.write_text(ENTRY, encoding="utf-8")
