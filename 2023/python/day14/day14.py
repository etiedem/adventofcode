#!/usr/bin/env python3.11

import numpy as np
from rich import print


def get_data(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return f.read()


def parse(data):
    output = []
    for line in data.splitlines():
        line = str.translate(line, str.maketrans(".#O", "012"))
        output.append(list(line))
    return np.array(output, dtype="int8")


def slide_left(data, x):
    idx = x - 1
    while idx >= 0:
        if data[idx] != 0:
            return idx + 1
        idx -= 1
    return idx + 1


def slide_right(data, x):
    idx = x + 1
    while idx < len(data):
        if data[idx] != 0:
            return idx - 1
        idx += 1
    return idx - 1


def direction(data, opposite=False):
    output = data
    for cidx in range(output.shape[0]):
        if opposite:
            items = range(output.shape[1] - 1, -1, -1)
        else:
            items = range(output.shape[1])
        for ridx in items:
            if output[cidx][ridx] == 2:
                if opposite:
                    loc = slide_right(output[cidx], ridx)
                else:
                    loc = slide_left(output[cidx], ridx)
                output[cidx][ridx] = 0
                output[cidx][loc] = 2
    return output


def find_repeating(data):
    count = 1
    current = data
    seen = [current]
    while True:
        current = part2(current)
        if any(np.array_equal(current, x) for x in seen):
            for start, x in enumerate(seen):
                if np.array_equal(x, current):
                    cycle_length = count - start
                    return current, start, cycle_length
        seen.append(current)
        count += 1


def part1(data):
    return direction(data.T).T


def calc_load(data):
    total = 0
    for idx, row in enumerate(data):
        total += np.count_nonzero(row == 2) * (data.shape[0] - idx)
    return total


def part2(data, num=1):
    output = data.copy()
    for _ in range(num):
        output = direction(output.T).T  # North
        output = direction(output)  # West
        output = direction(output.T, True).T  # South
        output = direction(output, True)  # East
    return output


def main():
    data = get_data("day14.txt")

    p1 = calc_load(part1(parse(data)))
    print(f"Part 1: {p1}")

    grid, start, cycle_length = find_repeating(parse(data))
    remaining = (1_000_000_000 - start) % cycle_length

    p2 = calc_load(part2(grid, remaining))
    print(f"Part 2: {p2}")


if __name__ == "__main__":
    main()

