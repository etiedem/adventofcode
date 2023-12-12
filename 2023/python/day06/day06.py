#!/usr/bin/env python3.11

from rich import print
from math import prod


def get_data(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return f.read()


def parse_part1(data: str):
    time, dist = data.splitlines()
    return [
        (int(time), int(dist)) for time, dist in zip(time.split()[1:], dist.split()[1:])
    ]


def parse_part2(data: str):
    time, dist = data.splitlines()
    time = int("".join(time.split()[1:]))
    dist = int("".join(dist.split()[1:]))
    return [(time, dist)]


def calc_times(time: int, dist: int):
    for btn in range(time):
        if btn * (time - btn) > dist:
            return (time - btn) - btn + 1


def solve(data):
    return prod(calc_times(time, dist) for time, dist in data)


def main():
    data = get_data("day06.txt")

    p1 = solve(parse_part1(data))
    print(f"Part 1: {p1}")

    p2 = solve(parse_part2(data))
    print(f"Part 2: {p2}")


if __name__ == "__main__":
    main()
