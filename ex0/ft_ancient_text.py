#!/usr/bin/env python3


import sys


def main() -> None:
    argv = sys.argv
    if len(argv) < 2:
        print("Usage: ft_ancient_text.py <file>")
        return
    filename = argv[1]
    try:
        file = open(filename)
        print("---")
        print(file.read())
        print("---")
        file.close()
        print(f"File {filename} closed")
    except Exception as e:
        print(f"Error opening file '{filename}':", e)


if __name__ == "__main__":
    print("=== Cyber Archives Recovery ===")
    main()
