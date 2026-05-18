#!/usr/bin/env python3


import sys


def get_filename() -> str:
    sys.stdout.write("Enter new file name (or empty):")
    sys.stdout.flush()
    name = sys.stdin.readline()
    if len(name) > 0 and name[-1] == "\n":
        name = name[:-1]
    return name


def main() -> None:
    argv = sys.argv
    if len(argv) < 2:
        print("Usage: ft_archive_creation.py <file>")
        return
    filename = argv[1]
    try:
        file = open(filename)
        print("---")
        text = file.read()
        print(text)
        print("---")
        file.close()
        print(f"File {filename} closed")
        print("Transform data:")
        print("---")
        lines = text.split("\n")
        new_text = ""
        for line in lines:
            new_line = line + "#"
            print(new_line)
            new_text = new_text + new_line + "\n"
        print("---")
        output_name = get_filename()
        if output_name:
            print(f"Saving data to '{output_name}'")
            output_file = open(output_name, "w+")
            output_file.write(new_text)
            output_file.close()
            print(f"Data saved in file '{output_name}'.")
        else:
            print("Not saving data.")
    except Exception as e:
        print(f"[STDERR] Error opening file '{filename}':", e, file=sys.stderr)


if __name__ == "__main__":
    print("=== Cyber Archives Recovery & Preservation ===")
    main()
