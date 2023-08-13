#!/usr/bin/env python3.11

from functools import reduce
from itertools import combinations
from operator import mul

from rich import print


def get_data(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return f.read()


def parse(data):
    return [int(x) for x in data.splitlines()]


def solve(data, size):
    group_size = sum(data) // size
    for i in range(len(data)):
        if qes := [reduce(mul, x) for x in combinations(data, i) if sum(x) == group_size]:
            return min(qes)
    return None


def main():
    data = parse(get_data("day24.txt"))

    p1 = solve(data, 3)
    print(f"Part 1: {p1}")

    p2 = solve(data, 4)
    print(f"Part 2: {p2}")


if __name__ == "__main__":
    main()
