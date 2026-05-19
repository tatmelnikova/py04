#!/usr/bin/env python3


import sys


def main() -> None:
    argv = sys.argv
    if len(argv) < 2:
        print("Usage: ft_archive_creation.py <file>")
        return
    filename = argv[1]

    file = None
    text = None
    try:
        file = open(filename)
        print("---")
        text = file.read()
        print(text)
        print("---")
    except Exception as e:
        print(f"Error opening file '{filename}':", e)
    finally:
        if file is not None:
            file.close()
            print(f"File {filename} closed")
        else:
            return

    new_text = None
    try:
        print("Transform data:")
        print("---")
        if text is not None:
            lines = text.split("\n")
            new_text = ""
            for line in lines:
                new_line = line + "#"
                print(new_line)
                new_text = new_text + new_line + "\n"
            print("---")
    except Exception as e:
        print("Error transforming the text", e)
        return

    out_file = None
    try:
        output_name = input("Enter new file name (or empty):")
        if output_name and new_text is not None:
            print(f"Saving data to '{output_name}'")
            out_file = open(output_name, "w+")
            out_file.write(new_text)
            print(f"Data saved in file '{output_name}'.")
        else:
            print("Not saving data.")
    except Exception as e:
        print(f"Error opening file '{filename}':", e)
    finally:
        if out_file is not None:
            out_file.close()


if __name__ == "__main__":
    print("=== Cyber Archives Recovery ===")
    main()
