#!/usr/bin/env python3.12

from dataclasses import dataclass, field
from itertools import product
from typing import TypeAlias

import numpy as np
from icecream import ic
from rich import print


@dataclass(unsafe_hash=True)
class Hole:
    x: int
    y: int
    color: str


Holes: TypeAlias = set[Hole]


@dataclass
class Map:
    holes: Holes
    map: np.ndarray = field(init=False)
    miny: int = field(init=False)
    minx: int = field(init=False)
    maxy: int = field(init=False)
    maxx: int = field(init=False)

    def __post_init__(self):
        minx, maxx, miny, maxy = self.minmax()
        self.miny = miny
        self.minx = minx
        self.maxy = maxy
        self.maxx = maxx
        ic(self.minmax())
        self.map = self.create_map()

    def create_map(self) -> np.ndarray:
        xdif = self.maxx - self.minx
        ydif = self.maxy - self.miny
        map = np.ndarray(shape=(ydif + 1, xdif + 1), dtype=object)
        for hole in self.holes:
            map[hole.y - self.miny, hole.x - self.minx] = hole.color
        return map

    def fill(self):
        start = self.find_fill_start()
        queue = [start]
        seen = set()
        while queue:
            current = queue.pop(0)
            if current in seen:
                continue
            self.holes.add(
                Hole(current[1] + self.minx, current[0] + self.miny, "inside")
            )
            seen.add(current)
            for nei in self.get_neighbor(current):
                if nei not in seen:
                    queue.append(nei)
                    # ic(nei)
        self.map = self.create_map()

    def find_fill_start(self) -> tuple[int, int]:
        lastx = -1
        lasty = 0

        for (y, x), item in np.ndenumerate(self.map):
            if y != lasty:
                lastx = -1
                lasty = y
            if item:
                if lastx == -1:
                    lastx = x
                    continue
                if x > lastx + 1:
                    return y, x - 1
                else:
                    lastx = x
        raise ValueError("Invalid values for x, y")

    def get_neighbor(self, current):
        # dir = ((0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1))
        # for d in dir:
        for d in product(range(-1, 2), range(-1, 2)):
            ny = d[0] + current[0]
            nx = d[1] + current[1]
            if not (0 <= ny <= self.maxy + abs(self.miny)):
                continue
            if not (0 <= nx <= self.maxx + abs(self.minx)):
                continue
            if self.map[ny, nx] is None:
                yield ny, nx

    def show(self):
        last = 0
        for (y, _), item in np.ndenumerate(self.map):
            if y != last:
                print()
                last = y
            if item == "inside":
                print("@", end="")
            elif item:
                print("*", end="")
            else:
                print(" ", end="")
        print()

    def count(self) -> int:
        c = 0
        for item in self.holes:
            if item:
                c += 1
        return c

    def minmax(self) -> tuple[int, ...]:
        minx, miny = float("inf"), float("inf")
        maxx, maxy = -float("inf"), -float("inf")
        for hole in self.holes:
            minx = min(minx, hole.x)
            miny = min(miny, hole.y)
            maxx = max(maxx, hole.x)
            maxy = max(maxy, hole.y)
        return int(minx), int(maxx), int(miny), int(maxy)


def get_data(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return f.read()


def parse_data(data: str) -> Map:
    output = set()
    x, y = 0, 0
    for line in data.splitlines():
        dir, steps, color = line.lower().strip().split()
        color = color.strip("()#")
        for _ in range(int(steps)):
            match dir:
                case "r":
                    x += 1
                case "l":
                    x -= 1
                case "u":
                    y -= 1
                case "d":
                    y += 1
            # ic(x, y, color)
            output.add(Hole(x, y, color))

    return Map(output)


def main():
    data = get_data("day18.txt")
    # data = get_data("example.txt")
    holes = parse_data(data)
    holes.fill()
    # holes.show()
    ic(holes.count())

    # p1 = part1(data)
    # print(f"Part 1: {p1}")

    # p2 = part2(data)
    # print(f"Part 2: {p2}")


if __name__ == "__main__":
    main()
