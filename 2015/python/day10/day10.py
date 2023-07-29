#!/usr/bin/env python3.11

import re

from rich import print


def get_data(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return f.read()


def solve_re(data):
    output = []
    for group in re.finditer(r"(.)\1*", data):
        output.extend([str(len(group.group())), group.group(1)])
    return "".join(output)


def solve(data):
    output = []
    last, count = None, 1

    for x in data:
        if last is None:
            last = x
            continue
        if x != last:
            output.extend([str(count), last])
            count = 1
            last = x
        else:
            count += 1

    output.extend([str(count), x])
    return "".join(output)


def main():
    data = get_data("day10.txt")

    for _ in range(40):
        data = solve(data)
    p1 = len(data)

    print(f"Part 1: {p1}")

    for _ in range(10):
        data = solve(data)
    p2 = len(data)

    print(f"Part 2: {p2}")


if __name__ == "__main__":
    main()
