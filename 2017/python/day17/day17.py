#!/usr/bin/env python3.11

from collections import deque

from rich import print


def get_data(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return f.read()


def part1(skips: int, num: int = 2017):
    ring = [0]
    idx = 0
    for count in range(1, num + 1):
        idx = ((idx + skips) % len(ring)) + 1
        if idx == len(ring):
            ring.append(count)
        else:
            ring.insert(idx, count)

    return ring[idx + 1]


def part2(skips: int, num: int = 50_000_000):
    idx = 0
    for count in range(1, num + 1):
        idx = (idx + skips) % count + 1
        if idx == 1:
            output = count

    return output


def main():
    data = int(get_data("day17.txt"))

    p1 = part1(data)
    print(f"Part 1: {p1}")

    p2 = part2(data)
    print(f"Part 2: {p2}")


if __name__ == "__main__":
    main()
