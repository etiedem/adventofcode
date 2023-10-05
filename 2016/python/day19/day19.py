#!/usr/bin/env python3.11

from dataclasses import dataclass

import numpy as np
from rich import print


def get_data(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return f.read()


def wrap_iter(circle, start):
    s = start[0]
    if s < circle.shape[0]:
        for idx, item in enumerate(circle[s + 1 :], s + 1):
            yield idx, item
    if s > 0:
        for idx, item in enumerate(circle[:s]):
            yield idx, item


def part1(num: int):
    circle = np.ones_like(np.ndarray, dtype=int, shape=(num))

    while True:
        for idx, elf in np.ndenumerate(circle):
            if elf > 0:
                for i, pres in wrap_iter(circle, idx):
                    if pres:
                        circle[idx] += pres
                        if circle[idx] == circle.shape[0]:
                            return idx[0] + 1
                        circle[i] = 0
                        break


def part2(num: int):
    circle: list = [x for x in range(2, num + 1)]

    while len(circle) > 1:
        idx = 0
        while idx < len(circle):
            half = (idx + (len(circle) // 2)) % len(circle)
            circle.remove(circle[half])
            if half > idx:
                idx += 1
    return circle


def main():
    data = get_data("day19.txt")

    p1 = part1(int(data))
    print(f"Part 1: {p1}")

    p2 = part2(int(data))
    print(f"Part 2: {p2[0]}")


if __name__ == "__main__":
    main()
