#!/usr/bin/env python3.11
import numpy as np
from rich import print


def show(self):
    output = []
    row = []
    cur = 0
    for idx, item in np.ndenumerate(self):
        if idx[0] != cur:
            cur = idx[0]
            output.append("".join(row))
            row.clear()

        match item:
            case 0:
                i = "."
            case 1:
                i = "^"
            case _:
                raise ValueError("Unknown item %s" % item)
        row.append(i)
    output.append("".join(row))
    return "\n".join(output)


def get_data(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return f.read()


def check_trap(left, center, right) -> bool:
    if left and center and not right:
        return True
    if center and right and not left:
        return True
    if left and not center and not right:
        return True
    if right and not center and not left:
        return True
    return False


def make_grid(data, length):
    grid = np.zeros_like(np.ndarray, shape=(length, len(data) + 2))
    for idx, d in enumerate(data):
        match d:
            case ".":
                item = 0
            case "^":
                item = 1
            case _:
                raise ValueError("Invalid item: %s" % item)
        grid[0, idx + 1] = item
    for r, row in enumerate(np.lib.stride_tricks.sliding_window_view(grid, (1, 3))):
        if r == length - 1:
            break
        for i, item in enumerate(row):
            grid[r + 1, i + 1] = 1 if check_trap(*item[0]) else 0

    grid = np.delete(grid, 0, axis=1)
    grid = np.delete(grid, -1, axis=1)
    return grid


def count_safe(grid):
    return np.count_nonzero(grid == 0)


def main():
    data = get_data("day18.txt")

    p1 = count_safe(make_grid(data, 40))
    print(f"Part 1: {p1}")

    p2 = count_safe(make_grid(data, 400000))
    print(f"Part 2: {p2}")


if __name__ == "__main__":
    main()
