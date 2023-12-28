#!/usr/bin/env python3.11

from collections import namedtuple
from functools import cache

from rich import print

record = namedtuple("record", "pattern check")


def get_data(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return f.read()


def parse(data: str, part2: bool = False):
    output = []
    for line in data.splitlines():
        pattern, check = line.split()
        check = tuple(map(int, check.split(",")))
        if part2:
            pattern = "?".join([pattern] * 5)
            check *= 5
        output.append(record("." + pattern + ".", check))
    return output


def fits(s: str, start: int, end: int) -> bool:
    if start - 1 < 0 or end + 1 >= len(s):
        return False

    if s[start - 1] == "#" and s[end + 1] == "#":
        return False

    if "#" in s[:start]:
        return False

    for i in range(start, end + 1):
        if s[i] == ".":
            return False

    return True


@cache
def dfs(record: str, groups: list[int]) -> int:
    if not groups:
        return 0 if "#" in record else 1

    size = groups[0]
    groups = groups[1:]

    count = 0
    for end in range(len(record)):
        start = end - (size - 1)

        if fits(record, start, end):
            count += dfs(record[end + 1 :], groups)

    return count


def solve(data: list[record]) -> int:
    total = 0
    for record in data:
        r, g = record
        total += dfs(r, g)
    return total


def main():
    data = get_data("day12.txt")

    p1 = solve(parse(data))
    print(f"Part 1: {p1}")

    p2 = solve(parse(data, part2=True))
    print(f"Part 2: {p2}")


if __name__ == "__main__":
    main()
