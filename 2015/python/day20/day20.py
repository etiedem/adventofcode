#!/usr/bin/env python3.11

import numpy as np
from rich import print


def get_data(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return f.read()


def part1(num):
    presents = np.zeros(num // 10)
    for i in range(1, num // 10):
        presents[i::i] += 10 * i
    return np.min(np.argwhere(presents >= num))


def part2(num):
    presents = np.zeros(num // 10)
    for i in range(1, num // 10):
        presents[i : (50 * i) + 1 : i] += 11 * i
    return np.min(np.argwhere(presents >= num))


def main():
    data = int(get_data("day20.txt"))

    p1 = part1(data)
    print(f"Part 1: {p1}")

    p2 = part2(data)
    print(f"Part 2: {p2}")


if __name__ == "__main__":
    main()
