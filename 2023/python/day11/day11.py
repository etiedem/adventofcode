#!/usr/bin/env python3.11

from dataclasses import dataclass, field
from typing import TypeAlias

import numpy as np
from more_itertools import minmax
from rich import print

Pos: TypeAlias = tuple[int, int]


@dataclass
class Galaxy:
    name: int
    pos: tuple[int, int]
    neighbours: dict = field(default_factory=dict)


@dataclass
class Map:
    grid: np.array
    galaxies: list = field(default_factory=list)
    empty_row: set = field(default_factory=set)
    empty_col: set = field(default_factory=set)

    def __post_init__(self):
        self.galaxies = self.find_galaxies()
        self.empty_row, self.empty_col = self.find_empty()
        for galaxy in self.galaxies:
            galaxy.neighbours = {
                g.name: 0 for g in self.galaxies if g.name != galaxy.name
            }
        self.find_dist_to_neighbours()

    def __str__(self):
        return "\n".join(["".join(row) for row in self.grid])

    @classmethod
    def from_str(cls, data):
        grid = np.array([list(line) for line in data.splitlines()])
        return cls(grid)

    @property
    def galaxy_distance(self):
        seen = set()
        output = 0
        for g in self.galaxies:
            for name, value in g.neighbours.items():
                if name not in seen:
                    output += value
            seen.add(g.name)
        return output

    def find_dist_to_neighbours(self, expansion=2):
        for galaxy in self.galaxies:
            for other in self.galaxies:
                if other.name != galaxy.name:
                    dist = self.manhattan(galaxy.pos, other.pos)
                    miny, maxy = minmax(galaxy.pos[0], other.pos[0])
                    minx, maxx = minmax(galaxy.pos[1], other.pos[1])
                    dist += (expansion - 1) * len(
                        set(range(miny, maxy)) & self.empty_row
                    )
                    dist += (expansion - 1) * len(
                        set(range(minx, maxx)) & self.empty_col
                    )
                    galaxy.neighbours[other.name] = dist

    def manhattan(self, start: Pos, goal: Pos):
        return abs(start[0] - goal[0]) + abs(start[1] - goal[1])

    def find_galaxies(self):
        galaxies = []
        idx = 1
        for pos, value in np.ndenumerate(self.grid):
            if value == "#":
                galaxies.append(Galaxy(idx, pos))
                idx += 1
        return galaxies

    def find_empty(self):
        filled_row = {g.pos[0] for g in self.galaxies}
        filled_col = {g.pos[1] for g in self.galaxies}
        return set(range(self.grid.shape[0])) - filled_row, (
            set(range(self.grid.shape[1])) - filled_col
        )


def get_data(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return f.read()


def main():
    data = get_data("day11.txt")
    m = Map.from_str(data)

    p1 = m.galaxy_distance
    print(f"Part 1: {p1}")

    m.find_dist_to_neighbours(1_000_000)
    p2 = m.galaxy_distance
    print(f"Part 2: {p2}")


if __name__ == "__main__":
    main()
