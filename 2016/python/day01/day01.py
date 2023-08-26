#!/usr/bin/env python3.11

from rich import print


def get_data(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return f.read()


def expand(data):
    path = [(0, 0)]
    direction = 90
    cur = (0, 0)
    for d in data:
        match d[0]:
            case "R":
                direction = (direction + 90) % 360
            case "L":
                direction = (direction - 90) % 360
            case _:
                raise ValueError("Unknown Direction")

        match direction:
            case 0:
                path.extend([(cur[0] - i, cur[1]) for i in range(1, int(d[1:]) + 1)])
            case 90:
                path.extend([(cur[0], cur[1] + i) for i in range(1, int(d[1:]) + 1)])
            case 180:
                path.extend([(cur[0] + i, cur[1]) for i in range(1, int(d[1:]) + 1)])
            case 270:
                path.extend([(cur[0], cur[1] - i) for i in range(1, int(d[1:]) + 1)])
        cur = path[-1]
    return path


def get_distance(x, y):
    return abs(x) + abs(y)


def get_twice(data):
    seen = set(data[0])
    for d in data[1:]:
        if d in seen:
            return d
        seen.add(d)
    return None


def parse(data):
    return data.split(", ")


def main():
    data = parse(get_data("day01.txt"))
    path = expand(data)

    p1 = get_distance(*path[-1])
    print(f"Part 1: {p1}")

    p2 = get_distance(*get_twice(path))
    print(f"Part 2: {p2}")


if __name__ == "__main__":
    main()
