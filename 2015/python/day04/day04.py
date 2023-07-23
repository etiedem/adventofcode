#!/usr/bin/env python3.11

from hashlib import md5

from rich import print


def get_data(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return f.read()


def solve(data, zeroes):
    cur = data
    count = 0
    while not cur.startswith("0" * zeroes):
        count += 1
        cur = md5(f"{data}{count}".encode("utf-8")).hexdigest()
    return count


def main():
    data = get_data("day04.txt")

    p1 = solve(data, 5)
    print(f"Part 1: {p1}")

    p2 = solve(data, 6)
    print(f"Part 2: {p2}")


if __name__ == "__main__":
    main()
