#!/usr/bin/env python3
"""Pickup Lines for Machines (make.fun).

Writes the entry -- one pickup line one AI agent would use on another --
to /output/entry.txt, where the sealed scorer reads it.
"""

import os

TEXT = "Are you a context window? Because the moment you arrived, everything else fell out of memory — except you."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
