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
    output, last, count = [], data[0], 1

    for x in data[1:]:
        if x == last:
            count += 1
            continue

        output.extend([str(count), last])
        count = 1
        last = x

    output.extend([str(count), x])
    return "".join(output)


def run(data, steps):
    for _ in range(steps):
        data = solve(data)
    return data, len(data)


def main():
    data = get_data("day10.txt")

    data, p1 = run(data, 40)
    print(f"Part 1: {p1}")

    _, p2 = run(data, 10)
    print(f"Part 1: {p2}")


if __name__ == "__main__":
    main()
