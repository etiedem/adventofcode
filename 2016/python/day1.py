#!/usr/bin/env python3.11


from dataclasses import dataclass

from rich import print


@dataclass
class Instruction:
    dir: str
    dist: int

    def __init__(self, data):
        self.dir = data[0]
        self.dist = int(data[1:])

    def move(self, current):
        (x, y), c_dir = current
        match self.dir:
            case "R":
                dir = (c_dir + 90) % 360
            case "L":
                dir = (c_dir - 90) % 360

        match dir:
            case 0:
                return ((x - self.dist, y), dir)
            case 90:
                return ((x, y + self.dist), dir)
            case 180:
                return ((x + self.dist, y), dir)
            case 270:
                return ((x, y - self.dist), dir)


def get_data(filename):
    with open(filename, "r", encoding="utf-8") as f:
        yield f.readlines()


def create_span(start, end):
    if start < end:
        return range(start + 1, end + 1)
    else:
        return range(start - 1, end - 1, -1)


def expand(current, new):
    c_x, c_y = current[0]
    n_x, n_y = new
    if c_x == n_x:
        for i in create_span(c_y, n_y):
            yield (c_x, i)
    if c_y == n_y:
        for i in create_span(c_x, n_x):
            yield (i, c_y)


def main():
    data = get_data("day1.txt")
    visited = set()
    current = ((0, 0), 90)
    twice = None
    instr = map(Instruction, next(data)[0].strip().split(", "))
    for i in instr:
        last_move = i.move(current)
        for x in expand(current, last_move[0]):
            if x in visited and not twice:
                twice = x
            visited.add(x)
        current = last_move
    last, _ = current

    print(f"Part 1: {abs(last[0]) + abs(last[1])}")
    print(f"Part 2: {abs(twice[0]) + abs(twice[1])}")


if __name__ == "__main__":
    main()
