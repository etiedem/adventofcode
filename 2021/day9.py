from dataclasses import dataclass
from functools import reduce

from rich import print


def get_data(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        return [[int(x)
                 for x in item]
                for line in f.readlines()
                for item in line.split()]


def get_around(data, x, y):
    if x < len(data[0]) - 1:
        yield data[y][x + 1]
    if x > 0:
        yield data[y][x - 1]
    if y < len(data) - 1:
        yield data[y + 1][x]
    if y > 0:
        yield data[y - 1][x]


@dataclass
class Node:
    x: int
    y: int
    value: int


def inside_simple(x, y, stack):
    return any(node.x == x and node.y == y for node in stack)


def flood_fill_simple(x, y, data, stack=None):
    stack = [] if stack is None else stack

    if data[y][x] == 9 or inside_simple(x, y, stack):
        return

    stack.append(Node(x, y, data[y][x]))
    flood_fill_simple(x, y + 1, data, stack) if y + 1 < len(data) else None
    flood_fill_simple(x, y - 1, data, stack) if y > 0 else None
    flood_fill_simple(x + 1, y, data, stack) if x + 1 < len(data[0]) else None
    flood_fill_simple(x - 1, y, data, stack) if x > 0 else None

    return stack


def main():
    data = get_data('day9.txt')

    result = []
    for y, row in enumerate(data):
        for x, item in enumerate(row):
            if all(item < x for x in get_around(data, x, y)):
                result.append(flood_fill_simple(x, y, data))
    basins = sorted(result, key=len, reverse=True)[:3]
    answer = reduce(lambda x, y: x * len(y), basins, 1)
    print(answer)


if __name__ == "__main__":
    main()
