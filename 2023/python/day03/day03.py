#!/usr/bin/env python3.11

from dataclasses import dataclass, field
from itertools import product
from math import prod
from string import punctuation

from rich import print


@dataclass
class Grid:
    grid: list[list[str]]
    parts: list[int] = field(default_factory=list)
    gears: list[int] = field(default_factory=list)

    def __post_init__(self):
        self.find_parts()
        self.find_parts(gear=True)

    @classmethod
    def fromstr(cls, data: str):
        output = []
        for r in data.splitlines():
            output.append(list(r))
        return cls(output)

    def find_parts(self, gear=False):
        partidx = set()
        for y, row in enumerate(self.grid):
            for x, item in enumerate(row):
                if item in punctuation.replace(".", "+"):
                    idx, num = self.search_around(x, y, gear)
                    if any(i in partidx for i in idx):
                        continue
                    partidx |= idx
                    if gear and num:
                        self.gears.append(prod(num))
                    else:
                        self.parts.extend(num)

    def inbounds(self, nx: int, ny: int, x: int, y: int):
        if nx == 0 and ny == 0:
            return False
        if nx + x < 0 or nx + x > len(self.grid[0]) - 1:
            return False
        if ny + y < 0 or ny + y > len(self.grid) - 1:
            return False
        return True

    def expand(self, x: int, y: int):
        partidx = {(x, y)}
        left, right = x, x
        while left >= 0 and self.grid[y][left].isdigit():
            partidx.add((left, y))
            left -= 1
        while right < len(self.grid[0]) and self.grid[y][right].isdigit():
            partidx.add((right, y))
            right += 1
        num = []
        for idx in range(left + 1, right):
            num.append(self.grid[y][idx])
        return partidx, int("".join(num))

    def search_around(self, x: int, y: int, gear: bool = False):
        partidx = set()
        nums = []
        for nx, ny in product(range(-1, 2), range(-1, 2)):
            if not self.inbounds(nx, ny, x, y):
                continue
            item = self.grid[ny + y][nx + x]
            if item.isdigit():
                idx, num = self.expand(nx + x, ny + y)
                if any(i in partidx for i in idx):
                    continue
                partidx |= idx
                nums.append(num)
        if gear and len(nums) != 2:
            return set(), []
        return partidx, nums


def get_data(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return f.read()


def main():
    data = get_data("day03.txt")
    grid = Grid.fromstr(data)

    p1 = sum(grid.parts)
    print(f"Part 1: {p1}")

    p2 = sum(grid.gears)
    print(f"Part 2: {p2}")


if __name__ == "__main__":
    main()
