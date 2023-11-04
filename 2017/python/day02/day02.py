#!/usr/bin/env python3.11

from rich import print


def get_data(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return f.read()


def part1(data) -> int:
    low = 9999999999
    high = 0

    for num in map(int, data.split()):
        if num < low:
            low = num
        if num > high:
            high = num
    return high - low


def part2(data) -> int:
    data = sorted(map(int, data.split()))

    for idx, x in enumerate(data):
        for y in data[idx + 1 :]:
            if y % x == 0:
                return int(y / x)
    return None


def main():
    data = get_data("day02.txt")

    p1 = sum(part1(x) for x in data.splitlines())
    print(f"Part 1: {p1}")

    p2 = sum(part2(x) for x in data.splitlines())
    print(f"Part 2: {p2}")


#

if __name__ == "__main__":
    main()
