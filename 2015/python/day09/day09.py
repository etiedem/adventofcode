#!/usr/bin/env python3.11

from itertools import permutations

import numpy as np
from rich import print

KEY = {
    "Faerun": 0,
    "Norrath": 1,
    "Tristram": 2,
    "AlphaCentauri": 3,
    "Arbre": 4,
    "Snowdin": 5,
    "Tambi": 6,
    "Straylight": 7,
}


def get_data(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return f.read()


def create_adjacency_matrix(data):
    output = np.zeros((8, 8))
    for line in data.splitlines():
        x, y, dist = line.split()[::2]
        output.itemset((KEY.get(x), KEY.get(y)), dist)
        output.itemset((KEY.get(y), KEY.get(x)), dist)
    return output


def solve(matrix, options):
    short = np.inf
    for path in permutations(options):
        candidate = shortest(matrix, path)
        if candidate < short:
            short = candidate
    return short


def shortest(matrix, path):
    total = 0
    for i in range(len(path) - 1):
        total += matrix.item((path[i], path[i + 1]))
    return total


def main():
    data = get_data("day09.txt")
    matrix = create_adjacency_matrix(data)

    p1 = solve(matrix, KEY.values())
    print(f"Part 1: {p1}")

    p2 = solve(matrix * -1, KEY.values()) * -1
    print(f"Part 2: {p2}")


if __name__ == "__main__":
    main()
