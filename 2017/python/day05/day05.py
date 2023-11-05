#!/usr/bin/env python3.11

from rich import print


def get_data(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return f.read()


def solve(data, part2=False):
    idx, prev, count = 0, 0, 0
    while True:
        try:
            idx += data[idx]
        except IndexError:
            return count
        if part2 and data[prev] >= 3:
            data[prev] -= 1
        else:
            data[prev] += 1
        prev = idx
        count += 1


def main():
    data = list(map(int, get_data("day05.txt").splitlines()))

    p1 = solve(data[:])
    print(f"Part 1: {p1}")

    p2 = solve(data[:], True)
    print(f"Part 2: {p2}")


if __name__ == "__main__":
    main()
