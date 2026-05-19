#!/usr/bin/env python3


import sys


def main() -> None:
    argv = sys.argv
    if len(argv) < 2:
        print("Usage: ft_ancient_text.py <file>")
        return
    filename = argv[1]
    file = None
    try:
        file = open(filename)
        print("---")
        print(file.read())
        print("---")
    except Exception as e:
        print(f"Error opening file '{filename}':", e)
    finally:
        if file is not None:
            file.close()
            print(f"File {filename} closed")


if __name__ == "__main__":
    print("=== Cyber Archives Recovery ===")
    main()
