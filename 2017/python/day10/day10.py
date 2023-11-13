#!/usr/bin/env python3.11

import math
from dataclasses import dataclass, field

from more_itertools import chunked
from rich import print


@dataclass
class Knot:
    length: int
    pos: int = 0
    skip: int = 0
    data: list = field(init=False)

    def __post_init__(self):
        self.data = list(range(self.length))

    def solve(self, data):
        for d in data:
            selection_idx = [(self.pos + x) % self.length for x in range(d)]
            for idx1, idx2 in zip(selection_idx[: (d // 2)], selection_idx[(d // 2) :][::-1]):
                self.data[idx1], self.data[idx2] = self.data[idx2], self.data[idx1]
            self.pos = (self.pos + d + self.skip) % self.length
            self.skip += 1
        return self

    def xor(self, data):
        if len(data) < 1:
            raise ValueError("Not enough items")

        cur = data[0] ^ data[1]
        for item in data[2:]:
            cur ^= item
        return cur

    def part1(self, data):
        convert = list(map(int, data.split(",")))
        return self.solve(convert)

    def part2(self, data):
        convert = [ord(x) for x in data]
        convert.extend([17, 31, 73, 47, 23])
        for _ in range(64):
            self.solve(convert)
        dense = [self.xor(chunk) for chunk in chunked(self.data, 16)]
        return "".join([hex(item)[2:].zfill(2) for item in dense])


def get_data(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return f.read()


def main():
    data = get_data("day10.txt")

    p1 = Knot(256).part1(data)
    print(f"Part 1: {math.prod(p1.data[:2])}")

    p2 = Knot(256).part2(data)
    print(f"Part 2: {p2}")


if __name__ == "__main__":
    main()
