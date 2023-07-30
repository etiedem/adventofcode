#!/usr/bin/env python3.11

import contextlib
import json
import re

from rich import print

ALL_RE = re.compile(r"(-?\d+)")


def get_data(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return f.read()


def part1(data):
    return sum(map(int, ALL_RE.findall(data)))


def get_sum(obj):
    output = 0
    if isinstance(obj, list):
        for i in obj:
            if isinstance(i, (list, dict)):
                output += get_sum(i)
            else:
                with contextlib.suppress(ValueError):
                    output += int(i)

    if isinstance(obj, dict):
        if "red" in obj or "red" in obj.values():
            return output

        for key in obj:
            if isinstance(obj[key], (list, dict)):
                output += get_sum(obj[key])
            else:
                with contextlib.suppress(ValueError):
                    output += int(obj[key])

    return output


def part2(data):
    d = json.loads(data)
    return get_sum(d)


def main():
    data = get_data("day12.txt")

    p1 = part1(data)
    print(f"Part 1: {p1}")

    p2 = part2(data)
    print(f"Part 2: {p2}")


if __name__ == "__main__":
    main()
