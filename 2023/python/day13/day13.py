#!/usr/bin/env python3.11

import numpy as np
from rich import print


def get_data(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return f.read()


def parse(data: str):
    output = []
    for pattern in data.split("\n\n"):
        p = []
        for line in pattern.splitlines():
            line = line.translate(str.maketrans(".#", "01"))
            p.append(list(line))
        output.append(np.array(p, dtype="uint8"))
    return output


def row_reflect(grid, part2: bool):
    length = len(grid)
    for top in range(0, length - 1):
        bottom = top + 1
        dist = min(top, length - 1 - bottom)
        tgrid = grid[top - dist : top + 1, :]
        bgrid = np.flip(grid[bottom : bottom + dist + 1, :], axis=0)
        if not part2 and np.array_equal(tgrid, bgrid):
            return top + 1
        elif part2 and np.count_nonzero(tgrid != bgrid) == 1:
            return top + 1
    return 0


def solve(grids, part2: bool = False):
    total = 0
    for g in grids:
        total += row_reflect(g, part2) * 100
        total += row_reflect(g.T, part2)
    return total


def main():
    data = get_data("day13.txt")

    p1 = solve(parse(data))
    print(f"Part 1: {p1}")

    p2 = solve(parse(data), part2=True)
    print(f"Part 2: {p2}")


if __name__ == "__main__":
    main()
