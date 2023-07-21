#!/usr/bin/env python3.11

from rich import print


def get_data(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return f.read()


def solve(data):
    counter = 0
    for i in data:
        match i:
            case "(":
                counter += 1
            case ")":
                counter -= 1
            case _:
                raise ValueError(f"Invalid character: {i}")
        yield counter


def part1(data):
    item = None
    for item in solve(data):
        pass
    return item


def part2(data):
    for idx, item in enumerate(solve(data), 1):
        if item == -1:
            return idx
    return -1


def main():
    data = get_data("day01.txt")

    p1 = part1(data)
    print(f"Part 1: {p1}")

    p2 = part2(data)
    print(f"Part 2: {p2}")


if __name__ == "__main__":
    main()
