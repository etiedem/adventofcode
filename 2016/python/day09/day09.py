#!/usr/bin/env python3.11

from rich import print


def get_data(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return f.read()


def decompress_length(data, recurse=False):
    idx = 0
    length = 0
    capture = []
    FLAG = False
    while idx < len(data):
        if data[idx] == ")":
            c, repeat = map(int, "".join(capture).split("x"))

            if recurse and "(" in data[idx + 1 : idx + c + 1]:
                length += repeat * decompress_length(data[idx + 1 : idx + c + 1], recurse)
            else:
                length += repeat * c

            idx += c + 1
            FLAG = False
            capture.clear()
            continue
        elif FLAG:
            capture.append(data[idx])
        elif data[idx] == "(":
            FLAG = True
        else:
            length += 1
        idx += 1
    return length


def main():
    data = get_data("day09.txt")

    p1 = decompress_length(data)
    print(f"Part 1: {p1}")

    p2 = decompress_length(data, recurse=True)
    print(f"Part 2: {p2}")


if __name__ == "__main__":
    main()
