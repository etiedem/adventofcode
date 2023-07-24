#!/usr/bin/env python3.11

import re
from dataclasses import dataclass, field

from rich import print

MATCH_RE = re.compile(r"(\D+) (\d+),(\d+)\D+(\d+),(\d+)")


@dataclass
class Lights:
    grid: list[list[int]] = field(init=False)

    def __post_init__(self):
        self.grid = [[0 for _ in range(1000)] for _ in range(1000)]

    @staticmethod
    def get_square(start, end):
        for x in range(start[0], end[0] + 1):
            for y in range(start[1], end[1] + 1):
                yield (x, y)

    def count_on(self):
        return sum(sum(row) for row in self.grid)


class Lights_1(Lights):
    def toggle(self, start, end):
        for x, y in self.get_square(start, end):
            self.grid[x][y] = not self.grid[x][y]

    def turn_on(self, start, end):
        for x, y in self.get_square(start, end):
            self.grid[x][y] = 1

    def turn_off(self, start, end):
        for x, y in self.get_square(start, end):
            self.grid[x][y] = 0


class Lights_2(Lights):
    def toggle(self, start, end):
        for x, y in self.get_square(start, end):
            self.grid[x][y] += 2

    def turn_on(self, start, end):
        for x, y in self.get_square(start, end):
            self.grid[x][y] += 1

    def turn_off(self, start, end):
        for x, y in self.get_square(start, end):
            self.grid[x][y] = max(self.grid[x][y] - 1, 0)


def get_data(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return f.read()


def parse(data):
    for line in data.splitlines():
        action, *coords_raw = MATCH_RE.match(line).groups()
        yield action, *tuple(map(int, coords_raw))


def run(lights, data):
    for action, *coords in parse(data):
        getattr(lights, action.replace(" ", "_"))((coords[0], coords[1]), (coords[2], coords[3]))
    return lights.count_on()


def main():
    data = get_data("day06.txt")

    p1 = run(Lights_1(), data)
    print(f"Part 1: {p1}")

    p2 = run(Lights_2(), data)
    print(f"Part 2: {p2}")


if __name__ == "__main__":
    main()
