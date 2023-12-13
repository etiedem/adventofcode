#!/usr/bin/env python3.11

from rich import print
from math import lcm


def get_data(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return f.read()


def parse(data: str):
    output = {}
    directions, rest = data.split("\n\n")
    for line in rest.splitlines():
        key, rest = line.split(" = ")
        rest = rest.strip("()")
        values = rest.split(", ")
        output[key] = values
    return directions, output


def solve(directions, adjacency, start="AAA", end="ZZZ", part2=False):
    count = 0
    current = start
    while current != end:
        for direction in directions:
            d = None
            match direction:
                case "L":
                    d = 0
                case "R":
                    d = 1
                case _:
                    raise ValueError(f"Unknown direction: {direction}")
            current = adjacency[current][d]
            count += 1
            if part2 and current.endswith("Z"):
                return count
            if current == end:
                return count
    return None


def part2(directions, adjacency):
    starts = sorted(k for k in adjacency if k.endswith("A"))
    return lcm(*[solve(directions, adjacency, start=s, part2=True) for s in starts])


def main():
    data = get_data("day08.txt")

    p1 = solve(*parse(data))
    print(f"Part 1: {p1}")

    p2 = part2(*parse(data))
    print(f"Part 2: {p2}")


if __name__ == "__main__":
    main()
