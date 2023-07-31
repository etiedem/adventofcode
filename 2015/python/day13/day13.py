#!/usr/bin/env python3.11

from itertools import permutations

import numpy as np
from rich import print


def get_data(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return f.read()


def create_keys(d):
    keys = set()
    for line in d.splitlines():
        d = line.split()
        keys = keys.union((d[0], d[-1].rstrip(".")))
    p1_keys = {key: idx for idx, key in enumerate(keys)}
    keys.add(("Self"))
    p2_keys = {key: idx for idx, key in enumerate(keys)}
    return p1_keys, p2_keys


def create_adjacency_matrix(data, keys):
    matrix = np.zeros((len(keys), len(keys)))
    for line in data.splitlines():
        d = line.split()
        primary, secondary = d[0], d[-1].rstrip(".")
        gain_loss, happy = d[2], int(d[3])
        match gain_loss:
            case "lose":
                diff = -1
            case "gain":
                diff = 1
            case _:
                raise ValueError(f"Unknown value {gain_loss}")
        matrix.itemset((keys.get(primary), keys.get(secondary)), diff * happy)
    return matrix


def solve(matrix, options):
    short = -np.inf
    for path in permutations(options):
        candidate = score(matrix, path)
        if candidate > short:
            short = candidate
    return short


def score(matrix, path):
    total = 0
    for i in range(len(path) - 1):
        total += matrix.item((path[i], path[i + 1]))
        total += matrix.item((path[i + 1], path[i]))
    total += matrix.item((path[0], path[-1]))
    total += matrix.item((path[-1], path[0]))
    return total


def main():
    data = get_data("day13.txt")
    p1_key, p2_key = create_keys(data)

    matrix = create_adjacency_matrix(data, p1_key)
    p1 = solve(matrix, p1_key.values())
    print(f"Part 1: {p1}")

    matrix = create_adjacency_matrix(data, p2_key)
    p2 = solve(matrix, p2_key.values())
    print(f"Part 2: {p2}")


if __name__ == "__main__":
    main()
