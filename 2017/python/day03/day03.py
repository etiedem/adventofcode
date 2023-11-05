#!/usr/bin/env python3.11

from math import ceil, floor, sqrt

import numpy as np
from rich import print


def get_data(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return f.read()


def cycle_num(n):
    x = floor(sqrt(n))
    return ceil(x / 2)


def first_number_in_cycle(n):
    return 4 * n * (n - 1) + 1


def side_length_in_cycle(n):
    return 2 * n


def spiral(n) -> (int, int):
    corners = (np.array([1, -1]), np.array([-1, -1]), np.array([-1, 1]), np.array([1, 1]))
    sides = (np.array([-1, 0]), np.array([0, 1]), np.array([1, 0]), np.array([0, -1]))

    if n == 0:
        return 0, 0

    k = cycle_num(n)
    distance_from_cycle_start = n - first_number_in_cycle(k)
    side_length = side_length_in_cycle(k)
    side = floor(distance_from_cycle_start / side_length)
    distance_along_side = 1 + distance_from_cycle_start % side_length
    pos = k * corners[side]
    return pos + distance_along_side * sides[side]


def part2(n) -> int:
    count, ans = 0, 0
    size = 20
    start = size // 2
    grid = np.zeros((size, size), dtype=int)
    grid[start, start] = 1
    while ans < n:
        ydx, xdx = spiral(count)
        xdx += start
        ydx += start
        ans = grid[ydx - 1 : ydx + 2, xdx - 1 : xdx + 2].sum()
        grid[ydx, xdx] = ans
        count += 1
    return ans


def main():
    data = get_data("day03.txt")

    p1 = sum(map(abs, spiral(int(data)))) - 1
    print(f"Part 1: {p1}")

    p2 = part2(int(data))
    print(f"Part 2: {p2}")


if __name__ == "__main__":
    main()
