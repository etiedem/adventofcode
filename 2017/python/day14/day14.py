#!/usr/bin/env python3.11

from dataclasses import dataclass, field

import numpy as np
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
        convert = list(map(ord, data))
        convert.extend([17, 31, 73, 47, 23])
        for _ in range(64):
            for d in convert:
                selection_idx = [(self.pos + x) % self.length for x in range(d)]
                for idx1, idx2 in zip(
                    selection_idx[: (d // 2)], selection_idx[(d // 2) :][::-1]
                ):
                    self.data[idx1], self.data[idx2] = self.data[idx2], self.data[idx1]
                self.pos = (self.pos + d + self.skip) % self.length
                self.skip += 1
        dense = [self.xor(chunk) for chunk in chunked(self.data, 16)]
        return "".join([hex(item)[2:].zfill(2) for item in dense])

    def xor(self, data):
        if len(data) < 1:
            raise ValueError("Not enough items")

        cur = data[0] ^ data[1]
        for item in data[2:]:
            cur ^= item
        return cur


class Grid:
    def __init__(self, key):
        self.grid = np.zeros((128, 128), dtype=int)

        for idx, _ in enumerate(self.grid):
            hash = f"{key}-{idx}"
            row = self._convert(Knot(256).solve(hash))
            self.grid[idx, :] = list(map(int, row))

    def _convert(self, hash):
        output = []
        for item in hash:
            output.append(bin(int(item, 16))[2:].zfill(4))
        return "".join(output)

    def regions(self):
        count = 0
        current = 1
        grid = np.vstack((np.zeros(128), self.grid, np.zeros(128)))
        grid = np.hstack((np.zeros((130, 1)), grid, np.zeros((130, 1))))
        for pos, value in np.ndenumerate(grid):
            if value == 1:
                current += 1
                count += 1
                self._mark_grid(grid, pos, current)
        return count

    def _mark_grid(self, grid, pos, num):
        direction = ((1, 0), (0, -1), (0, 1), (-1, 0))
        for dir in direction:
            new_pos = (pos[0] + dir[0], pos[1] + dir[1])
            if grid[new_pos] == 1:
                grid[new_pos] = num
                self._mark_grid(grid, new_pos, num)


def get_data(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return f.read()


def main():
    data = get_data("day14.txt")
    grid = Grid(data)

    p1 = grid.grid.sum()
    print(f"Part 1: {p1}")

    p2 = grid.regions()
    print(f"Part 2: {p2}")


if __name__ == "__main__":
    main()
