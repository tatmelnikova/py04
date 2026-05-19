#!/usr/bin/env python3
def secure_archive(filename: str,
                   mode: int = 1, text: str = "") -> tuple[bool, str]:
    if mode == 1:
        try:
            with open(filename) as file:
                data = file.read()
                return (True, data)
        except Exception as e:
            return (False, str(e))
    else:
        try:
            with open(filename, "w+") as file:
                file.write(text)
                return (True, "Content successfully written to file")
        except Exception as e:
            return (False, str(e))


def main() -> None:
    print("Using 'secure_archive' to read from a nonexistent file:")
    print(secure_archive("1.txt"))
    print()
    print("Using 'secure_archive' to read from an inaccessible file:")
    print(secure_archive("test1.txt"))
    print()
    print("Using 'secure_archive' to read from a regular file:")
    result = secure_archive("test.txt")
    print(result)
    print()
    print("Using 'secure_archive' to write previous content to a new file:")
    print(secure_archive("new.txt", 0, result[1]))


if __name__ == "__main__":
    main()
