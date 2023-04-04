#!/usr/bin/env python3.11
from copy import deepcopy
from dataclasses import dataclass
from enum import Enum, auto

from more_itertools import minmax
from rich import print


class Item(Enum):
    Rock = auto()
    Sand = auto()
    Air = auto()
    Generator = auto()


@dataclass
class Pos:
    x: int
    y: int

    def __add__(self, other):
        return Pos(self.x + other.x, self.y + other.y)


class Scan:
    def __init__(self, rocks: list) -> None:
        self.done = False
        self.full = False
        minx, maxx = 0, max(x for x, _ in rocks)
        miny, maxy = 0, max(y for _, y in rocks) + 2
        maxx = (maxx // 3) + maxx - minx
        self.floor = maxy
        self.grid = []
        for y in range(miny, maxy + 1):
            row = []
            for x in range(minx, maxx + 1):
                if (x, y) == (500, 0):
                    row.append(Item.Generator)
                    self.generator = Pos(x - minx, y - miny)
                elif (x, y) in rocks:
                    row.append(Item.Rock)
                else:
                    row.append(Item.Air)
            self.grid.append(row)

    def step(self, floor: bool = False):
        cx, cy = self.generator.x, self.generator.y
        try:
            cx, cy = self._get_move(cx, cy, floor)
        except TypeError:
            pass
        else:
            self.grid[cy][cx] = Item.Sand
            if cx == self.generator.x and cy == self.generator.y:
                self.full = True

    def count_sand(self):
        return sum(row.count(Item.Sand) for row in self.grid)

    def check_bounds(self, cx, cy):
        return 0 <= cx < len(self.grid[0]) and 0 <= cy < len(self.grid)

    def _get_move(self, cx, cy, floor):
        moves = ((0, 1), (-1, 1), (1, 1))
        for x, y in moves:
            if floor and cy + y == self.floor:
                return cx, cy
            if not self.check_bounds(cx + x, cy + y):
                self.done = True
                return None
            if self.grid[cy + y][cx + x] == Item.Air:
                return self._get_move(cx + x, cy + y, floor)
        return cx, cy

    def __iter__(self):
        for y, row in enumerate(self.grid):
            for x, item in enumerate(row):
                yield x, y, item

    def show(self, full: bool = False):
        if full:
            minx, maxx = 0, len(self.grid[0]) - 1
            miny, maxy = 0, len(self.grid) - 1
        else:
            minx, maxx = minmax(x for x, _, item in self if item != Item.Air)
            miny, maxy = minmax(y for _, y, item in self if item != Item.Air)

        for y in range(miny, maxy + 1):
            for x in range(minx, maxx + 1):
                match self.grid[y][x]:
                    case Item.Rock:
                        print("#", end="")
                    case Item.Air:
                        print(".", end="")
                    case Item.Generator:
                        print("+", end="")
                    case Item.Sand:
                        print("o", end="")
            print()


def get_data(filename):
    with open(filename, "r", encoding="utf-8") as f:
        yield from f.readlines()


def parse_rocks(data):
    rocks = []
    for line in data:
        rocks.extend(fill_rocks(map(int, sec.split(",")) for sec in line.strip().split(" -> ")))
    return rocks


def fill_rocks(data):
    px, py = next(data)
    rocks = [(px, py)]
    for cx, cy in data:
        while px != cx or py != cy:
            if px < cx:
                px += 1
            elif px > cx:
                px -= 1
            if py < cy:
                py += 1
            elif py > cy:
                py -= 1
            rocks.append((px, py))
    return rocks


def main():
    rocks = parse_rocks(get_data("day14.txt"))
    p1_scan = Scan(rocks)
    p2_scan = deepcopy(p1_scan)

    while not p1_scan.done:
        p1_scan.step()
    print(f"Part 1: {p1_scan.count_sand()}")

    while not p2_scan.full:
        p2_scan.step(floor=True)
    print(f"Part 2: {p2_scan.count_sand()}")


if __name__ == "__main__":
    main()
