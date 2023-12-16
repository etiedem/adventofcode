#!/usr/bin/env python3.11

import itertools
from collections import defaultdict
from copy import deepcopy
from dataclasses import dataclass, field
from functools import partial
from typing import TypeAlias

import numpy as np
from numpy.typing import NDArray

# from rich import print

Point: TypeAlias = tuple[int, int]


@dataclass
class Map:
    base: NDArray
    path: list = field(default_factory=list)
    adj: dict[list[Point]] = field(default_factory=defaultdict[list])
    start: Point = field(default=None)

    @classmethod
    def from_str(cls, data: str):
        m = cls(np.array([list(line) for line in data.splitlines()]))
        m.parse()
        m.clean_connections()
        m.clean()
        m.create_path()
        m.update_base()
        m.flood_fill()
        return m

    def count(self):
        # zeros = self.base[np.where(self.base == "0")]
        # path = self.base[np.where(self.base == "*")]
        # print(self.base[zeros  path])
        return len(self.base[(self.base != "*") & (self.base != "0")])
        # return np.where(self.base != "*") and np.where(self.base != "0")

    def flood_fill(self):
        checkpoint = partial(self.check_point, path=True)
        start = (0, 0)
        self.base[start] = "0"
        queue = [start]
        seen = set()
        while queue:
            current = queue.pop(0)
            for neighbor in filter(checkpoint, self.look_around(current)):
                if self.base[neighbor] != "*":
                    queue.append(neighbor) if neighbor not in seen else None
                    seen.add(neighbor)
                    self.base[current] = "0"

    def update_base(self):
        for point in self.path:
            self.base[point] = "*"

    def create_path(self):
        self.path.append(self.start)
        prev = self.start
        current = self.adj[self.start][0]
        while current != self.start:
            self.path.append(current)
            tmp = current
            current = (
                self.adj[current][0]
                if self.adj[current][0] != prev
                else self.adj[current][1]
            )
            prev = tmp

    def clean_connections(self):
        adjacents = deepcopy(self.adj)
        for key, val in adjacents.items():
            for neighbor in val:
                if key not in self.adj[neighbor]:
                    self.adj[key].remove(neighbor)

    def clean(self):
        adjacents = deepcopy(self.adj)
        cleanup = []
        CLEAN = False
        for key, val in adjacents.items():
            if len(val) < 2:
                CLEAN = True
                del self.adj[key]
                cleanup.append(key)

        for key in self.adj:
            self.adj[key] = list(
                filter(lambda x: x not in cleanup, self.adj[key]))

        if CLEAN:
            self.clean()

    def parse(self):
        for point, val in np.ndenumerate(self.base):
            match val:
                case ".":
                    continue
                case "S":
                    self.start = point
                    if neighbors := self.get_nei(point):
                        self.adj[point] = list(
                            filter(self.check_point, neighbors))
                case _:
                    if neighbors := self.get_nei(point):
                        self.adj[point] = list(
                            filter(self.check_point, neighbors))

    def check_point(self, point: Point, path: bool = False) -> bool:
        bounds = self.base.shape
        if point[0] < 0 or point[0] >= bounds[0]:
            return False
        if point[1] < 0 or point[1] >= bounds[1]:
            return False
        return self.base[point] != "*" if path else self.base[point] != "."

    def look_around(self, point: Point) -> list[Point]:
        for i, j in itertools.product(range(-1, 2), range(-1, 2)):
            if i == j == 0:
                continue
            yield (point[0] + i, point[1] + j)

    def get_nei(self, point: Point) -> list[Point] | None:
        match self.base[point]:
            case ".":
                return None
            case "|":
                return [(point[0] - 1, point[1]), (point[0] + 1, point[1])]
            case "-":
                return [(point[0], point[1] - 1), (point[0], point[1] + 1)]
            case "L":
                return [(point[0] - 1, point[1]), (point[0], point[1] + 1)]
            case "J":
                return [(point[0] - 1, point[1]), (point[0], point[1] - 1)]
            case "7":
                return [(point[0] + 1, point[1]), (point[0], point[1] - 1)]
            case "F":
                return [(point[0] + 1, point[1]), (point[0], point[1] + 1)]
            case "S":
                return [
                    (point[0] - 1, point[1]),
                    (point[0] + 1, point[1]),
                    (point[0], point[1] - 1),
                    (point[0], point[1] + 1),
                ]
            case _:
                raise ValueError(f"Unknown value: {self.base[point]}")


def get_data(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return f.read()


def main():
    data = get_data("day10.txt")
    # data = get_data("example1.txt")

    m = Map.from_str(data)

    p1 = len(m.path) // 2
    print(f"Part 1: {p1}")

    with np.printoptions(threshold=np.inf):
        for line in m.base:
            print("".join(line))
        # print(m.base)
    p2 = m.count()
    print(f"Part 2: {p2}")

    # 589 is too high


if __name__ == "__main__":
    main()
