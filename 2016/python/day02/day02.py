#!/usr/bin/env python3.11

from dataclasses import dataclass, field
from time import sleep

part1_raw = """123
456
789"""

part2_raw = """  1  \

 234 \

56789
 ABC \

  D  """


@dataclass
class Grid:
    grid: list = field(default_factory=list)
    pos: tuple = field(init=False)

    def __init__(self, data):
        self.grid = [list(d) for d in data.splitlines()]
        self.__post_init__()

    def __post_init__(self):
        for pos, item in self:
            if item == "5":
                self.pos = pos

    def __iter__(self):
        for y, row in enumerate(self.grid):
            for x, item in enumerate(row):
                yield ((x, y), item)

    def show(self):
        cur = 0
        for (x, y), item in self:
            if cur != y:
                print()
                cur = y
            if self.pos[0] == x and self.pos[1] == y:
                print(f" X", end="")
            else:
                print(f" {item}", end="")
        print()

    def move(self, direction):
        match direction:
            case "U":
                if self.pos[1] >= 1 and self.grid[self.pos[1] - 1][self.pos[0]] != " ":
                    self.pos = (self.pos[0], self.pos[1] - 1)
            case "D":
                if (
                    self.pos[1] <= len(self.grid) - 2
                    and self.grid[self.pos[1] + 1][self.pos[0]] != " "
                ):
                    self.pos = (self.pos[0], self.pos[1] + 1)
            case "L":
                if self.pos[0] >= 1 and self.grid[self.pos[1]][self.pos[0] - 1] != " ":
                    self.pos = (self.pos[0] - 1, self.pos[1])
            case "R":
                if (
                    self.pos[0] <= len(self.grid[0]) - 2
                    and self.grid[self.pos[1]][self.pos[0] + 1] != " "
                ):
                    self.pos = (self.pos[0] + 1, self.pos[1])
            case _:
                raise ValueError("Unknown Direction")
        return self


def get_data(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return f.read()


def del_prev_line():
    CURSOR_UP = "\x1b[1A"
    ERASE_LINE = "\x1b[2K"
    print(CURSOR_UP + ERASE_LINE + CURSOR_UP)


def solve(data, grid):
    result = []
    for d in data.splitlines():
        for direction in d:
            grid.move(direction)
            # grid.show()
            # sleep(0.3)
            # for _ in range(len(grid.grid)):
            #     del_prev_line()
        result.append(grid.grid[grid.pos[1]][grid.pos[0]])
    return "".join(result)


def main():
    data = get_data("day02.txt")

    grid1 = Grid(part1_raw)
    p1 = solve(data, grid1)
    print(f"Part 1: {p1}")

    grid2 = Grid(part2_raw)
    p2 = solve(data, grid2)
    print(f"Part 2: {p2}")


if __name__ == "__main__":
    main()
