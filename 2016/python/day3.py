#!/usr/bin/env python3.11

from more_itertools import flatten
from rich import print


def get_data(filename):
    with open(filename, "r", encoding="utf8") as f:
        yield from f.readlines()


def get_vertical_data(filename):
    with open(filename, "r", encoding="utf8") as f:
        data = list(flatten(map(str.split, f.readlines())))
        idx = 0
        while idx < len(data) - 6:
            yield " ".join((data[idx], data[idx + 3], data[idx + 6]))
            idx += 1
            if idx % 3 == 0:
                idx += 6


def is_valid(line):
    a, b, c = map(int, line.split())
    if a + b > c and b + c > a and a + c > b:
        return 1
    return 0


def main():
    data = get_data("day3.txt")
    part1 = sum(is_valid(line) for line in data)
    print(part1)

    data = get_vertical_data("day3.txt")
    part2 = sum(is_valid(line) for line in data)
    print(part2)


if __name__ == "__main__":
    main()
