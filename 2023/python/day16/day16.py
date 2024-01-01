#!/usr/bin/env python3.11

from collections import Counter
from dataclasses import dataclass
from typing import Literal

import numpy as np
from numpy.typing import NDArray
from rich import print


@dataclass
class Cave:
    grid: NDArray

    def get_next(self, y: int, x: int, dir: Literal[0, 90, 180, 270]) -> list[int]:
        max_y, max_x = self.grid.shape
        ny, nx = y, x
        match dir:
            case 0:
                nx -= 1
            case 90:
                ny -= 1
            case 180:
                nx += 1
            case 270:
                ny += 1
            case _:
                raise ValueError(f"Invalid direction {dir}")
        return [ny, nx, dir] if 0 <= ny < max_y and 0 <= nx < max_x else []

    def next_move(
        self, y: int, x: int, dir: Literal[0, 90, 180, 270]
    ) -> list[list[int]]:
        match self.grid[y, x]:
            case ".":
                return [self.get_next(y, x, dir)]
            case "|":
                match dir:
                    case 0 | 180:
                        return [self.get_next(y, x, 90), self.get_next(y, x, 270)]
                    case 90 | 270:
                        return [self.get_next(y, x, dir)]
            case "-":
                match dir:
                    case 0 | 180:
                        return [self.get_next(y, x, dir)]
                    case 90 | 270:
                        return [self.get_next(y, x, 0), self.get_next(y, x, 180)]
            case "/":
                match dir:
                    case 0:
                        dir = 270
                    case 90:
                        dir = 180
                    case 180:
                        dir = 90
                    case 270:
                        dir = 0
                return [self.get_next(y, x, dir)]
            case "\\":
                match dir:
                    case 0:
                        dir = 90
                    case 90:
                        dir = 0
                    case 180:
                        dir = 270
                    case 270:
                        dir = 180
                return [self.get_next(y, x, dir)]
            case _:
                raise ValueError(f"Invalid character {self.grid[y, x]}")

    def show(self, path):
        last_row = 0
        dir_map = {0: "<", 90: "^", 180: ">", 270: "v"}
        counter = Counter((p[0], p[1]) for p in path)
        local_path = {}
        for y, x, dir in path:
            if (length := counter[(y, x)]) > 1:
                local_path[(y, x)] = length
            else:
                local_path[(y, x)] = dir_map.get(dir)
        for (y, x), item in np.ndenumerate(self.grid):
            if y != last_row:
                print()
                last_row = y
            if (y, x) in local_path:
                print(local_path.get((y, x)), end="")
            else:
                print(item, end="")
        print()


def get_data(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return f.read()


def parse(data: str):
    output = []
    for line in data.splitlines():
        output.append(list(line))
    return np.array(output)


def dfs(g: Cave, pos=(0, 0, 180)):
    queue = []
    queue.append(pos)
    seen = set()
    while queue:
        y, x, dir = queue.pop(0)
        if (y, x, dir) in seen:
            continue
        for item in filter(lambda x: x, g.next_move(y, x, dir)):
            queue.append(item)
        seen.add((y, x, dir))
    return seen


def part2(g: Cave):
    max_y, max_x = g.grid.shape
    largest = 0
    # Top
    search = [(0, x, 270) for x in range(max_x)]
    # Bottom
    search += [(max_y - 1, x, 90) for x in range(max_x)]
    # Left
    search += [(y, 0, 180) for y in range(max_y)]
    # Right
    search += [(y, max_x - 1, 0) for y in range(max_y)]
    for s in search:
        current = len({p[0:2] for p in dfs(g, s)})
        if current > largest:
            largest = current
    return largest


def main():
    data = get_data("day16.txt")
    cave = Cave(parse(data))

    p1 = dfs(cave)
    p1 = len({p[0:2] for p in p1})
    print(f"Part 1: {p1}")

    p2 = part2(cave)
    print(f"Part 2: {p2}")


if __name__ == "__main__":
    main()

