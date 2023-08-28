#!/usr/bin/env python3.11

from rich import print


def is_triangle(sides):
    x, y, z = sides
    return x + y > z and y + z > x and x + z > y


def get_data(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return f.read()


def parse_row(data):
    for row in data.splitlines():
        yield list(map(int, row.split()))


def parse_column(data):
    columns = []
    for idx, row in enumerate(data.splitlines(), 1):
        columns.extend(map(int, row.split()))
        if idx % 3 == 0:
            yield columns[0::3]
            yield columns[1::3]
            yield columns[2::3]
            columns.clear()


def main():
    data = get_data("day03.txt")

    p1 = sum(1 for _ in filter(is_triangle, parse_row(data)))
    print(f"Part 1: {p1}")

    p2 = sum(1 for _ in filter(is_triangle, parse_column(data)))
    print(f"Part 2: {p2}")


if __name__ == "__main__":
    main()
