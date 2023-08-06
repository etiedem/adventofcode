#!/usr/bin/env python3.11

from dataclasses import dataclass

import numpy as np
from rich import print


@dataclass
class Grid:
    grid: np.ndarray[np.ndarray]

    @classmethod
    def from_str(cls, data):
        output = [
            np.array(list(map(int, line.translate(str.maketrans(".#", "01")))))
            for line in data.splitlines()
        ]
        array = np.array(output)
        return cls(array)

    @property
    def lights(self):
        return sum(np.nditer(self.grid))

    def step(self, steps, part=1):
        for _ in range(steps):
            self.get_next(part)
        return self

    def get_next(self, part):
        output = np.zeros_like(self.grid)
        for y, x in np.ndindex(self.grid.shape):
            if self.grid[y, x] == 1 and self._check_nei(x, y) in [2, 3]:
                output[y, x] = 1
            elif self.grid[y, x] == 0 and self._check_nei(x, y) == 3:
                output[y, x] = 1
        self.grid = output
        if part == 2:
            self.turn_on_corners()

    def turn_on_corners(self):
        dim = self.grid.shape
        self.grid[0, 0] = 1
        self.grid[0, dim[1] - 1] = 1
        self.grid[dim[0] - 1, 0] = 1
        self.grid[dim[0] - 1, dim[1] - 1] = 1
        return self

    def _check_nei(self, x, y):
        neighbors = ((-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1))
        return sum(
            self.grid[y + ny, x + nx]
            for nx, ny in neighbors
            if 0 <= y + ny < self.grid.shape[0]
            if 0 <= x + nx < self.grid.shape[1]
        )


def get_data(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return f.read()


def main():
    data = get_data("day18.txt")

    p1 = Grid.from_str(data).step(100)
    print(f"Part 1: {p1.lights}")

    p2 = Grid.from_str(data).turn_on_corners().step(100, 2)
    print(f"Part 2: {p2.lights}")


if __name__ == "__main__":
    main()
