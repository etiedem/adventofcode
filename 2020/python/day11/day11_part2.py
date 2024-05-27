from copy import deepcopy
from dataclasses import dataclass
from typing import List

from rich import print


@dataclass
class Grid:
    grid: List[List]
    filled: int = 0

    def count_adjacent(self, x, y):
        adjacent = ((-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1))
        count = 0
        for xd, yd in adjacent:
            xx = x + xd
            yy = y + yd
            while 0 <= xx < len(self.grid[0]) and 0 <= yy < len(self.grid):
                if self.grid[yy][xx] == "#":
                    count += 1
                    break
                if self.grid[yy][xx] == "L":
                    break
                xx += xd
                yy += yd

        return count

    def step(self):
        g = deepcopy(self.grid)
        for y in range(len(self.grid)):
            for x in range(len(self.grid[0])):
                if self.grid[y][x] == "L" and self.count_adjacent(x, y) == 0:
                    g[y][x] = "#"
                    self.filled += 1
                elif self.grid[y][x] == "#" and self.count_adjacent(x, y) >= 5:
                    g[y][x] = "L"
                    self.filled -= 1
        self.grid = g

    def find_sync(self):
        while True:
            tmp = deepcopy(self.grid)
            self.step()
            if tmp == self.grid:
                break
        return self.filled

    def show(self):
        for row in self.grid:
            for item in row:
                print(item, end=" ")
            print()


def get_data(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return [list(line) for line in f.read().splitlines()]


def main():
    data = get_data("day11.txt")
    grid = Grid(data)
    print(grid.find_sync())


if __name__ == "__main__":
    main()
