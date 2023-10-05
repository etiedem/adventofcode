#!/usr/bin/env python3.11

from heapq import heappop, heappush

from more_itertools import minmax
from rich import print


def get_data(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return f.read()


def solve(data):
    ranges = []
    for line in data.splitlines():
        left, right = map(int, line.split("-"))
        heappush(ranges, (left, right))

    output = []
    _, p_end = heappop(ranges)
    while ranges:
        c_start, c_end = heappop(ranges)
        if c_start > p_end + 1:
            output.extend(p_end + idx for idx in range(1, c_start - p_end))
        p_end = max((c_end, p_end))
    return output


def main():
    data = get_data("day20.txt")
    answer = solve(data)

    print(f"Part 1: {answer[0]}")
    print(f"Part 2: {len(answer)}")


if __name__ == "__main__":
    main()
