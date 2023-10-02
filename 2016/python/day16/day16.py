#!/usr/bin/env python3.11

from copy import copy

from more_itertools import windowed
from rich import print


def get_data(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return f.read()


def double(a: str):
    b = copy(a)
    b = b[::-1].translate(str.maketrans({"0": "1", "1": "0"}))
    return f"{a}0{b}"


def checksum(data: str):
    output = []
    cur = data
    while True:
        for a, b in windowed(cur, 2, step=2):
            if a == b:
                output.append("1")
            else:
                output.append("0")
        if len(output) % 2 != 0:
            return "".join(output)
        else:
            cur = "".join(output)
            output.clear()


def solve(data, length: int):
    while len(data) < length:
        data = double(data)
    return checksum(data[:length])


def main():
    data = get_data("day16.txt")

    p1 = solve(data, 272)
    print(f"Part 1: {p1}")

    p2 = solve(data, 35651584)
    print(f"Part 2: {p2}")


if __name__ == "__main__":
    main()
