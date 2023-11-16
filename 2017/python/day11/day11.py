#!/usr/bin/env python3.11

from rich import print


def get_data(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return f.read()


def solve(data: str) -> int:
    x, y, z = 0, 0, 0
    dists = []
    for direction in data.split(","):
        match direction:
            case "n":
                y += 1
                z -= 1
            case "ne":
                x += 1
                z -= 1
            case "se":
                x += 1
                y -= 1
            case "s":
                y -= 1
                z += 1
            case "sw":
                x -= 1
                z += 1
            case "nw":
                x -= 1
                y += 1
        dists.append((abs(x) + abs(y) + abs(z)) / 2)

    return (abs(x) + abs(y) + abs(z)) / 2, max(dists)


def main():
    data = get_data("day11.txt")

    p1, p2 = solve(data)

    print(f"Part 1: {p1}")
    print(f"Part 2: {p2}")


if __name__ == "__main__":
    main()
