#!/usr/bin/env python3.11

from rich import print


def get_data(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return f.read()


def is_valid(line, part2=False):
    words = set()
    for word in line.split():
        if part2:
            word = "".join(sorted(word))
        if word in words:
            return False
        words.add(word)
    return True


def main():
    data = get_data("day04.txt")

    p1 = sum(bool(is_valid(x)) for x in data.splitlines())
    print(f"Part 1: {p1}")

    p2 = sum(bool(is_valid(x, True)) for x in data.splitlines())
    print(f"Part 2: {p2}")


if __name__ == "__main__":
    main()
