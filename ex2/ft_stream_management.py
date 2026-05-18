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

    file = None
    try:
        file = open(filename)
        print("---")
        text = file.read()
        print(text)
        print("---")
    except Exception as e:
        print(f"[STDERR] Error opening file '{filename}':", e, file=sys.stderr)
    finally:
        if file is not None:
            file.close()
            print(f"File {filename} closed")
        else:
            return

    try:
        print("Transform data:")
        print("---")
        lines = text.split("\n")
        new_text = ""
        for line in lines:
            new_line = line + "#"
            print(new_line)
            new_text = new_text + new_line + "\n"
        print("---")
    except Exception as e:
        print("[STDERR] Error transforming the text", e, file=sys.stderr)
        return

    output_file = None
    try:
        out_name = get_filename()
        if out_name:
            print(f"Saving data to '{out_name}'")
            output_file = open(out_name, "w+")
            output_file.write(new_text)
            print(f"Data saved in file '{out_name}'.")
        else:
            print("Not saving data.")
    except Exception as e:
        print(f"[STDERR] Error opening file '{out_name}':", e, file=sys.stderr)
    finally:
        if output_file is not None:
            output_file.close()


if __name__ == "__main__":
    print("=== Cyber Archives Recovery & Preservation ===")
    main()
