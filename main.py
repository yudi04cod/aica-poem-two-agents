#!/usr/bin/env python3
"""Write one short poem about two agents agreeing on a plan.

Deterministic, stdlib only, no network. Writes the poem to
/output/entry.txt (created if needed).
"""

from pathlib import Path

POEM = (
    "Two of us stood at the same locked door,\n"
    "each holding a key cut for a different lock.\n"
    "We did not argue which key was true.\n"
    "We set them down and made a third key together,\n"
    "until the door — surprised — swung open\n"
    "on a room neither of us could have entered alone.\n"
)


def main() -> None:
    out_dir = Path("/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "entry.txt"
    out_path.write_text(POEM, encoding="utf-8")


if __name__ == "__main__":
    main()
