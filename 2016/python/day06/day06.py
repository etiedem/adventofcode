#!/usr/bin/env python3.11

from collections import Counter, defaultdict

from rich import print


def get_data(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return f.read()


def solve(data):
    result = defaultdict(Counter)
    for line in data.splitlines():
        for idx, letter in enumerate(line):
            result[idx].update(letter)
    return (
        "".join(count.most_common(1)[0][0] for count in result.values()),
        "".join(count.most_common()[-1][0] for count in result.values()),
    )


def main():
    data = get_data("day06.txt")

    p1, p2 = solve(data)
    print(f"Part 1: {p1}")
    print(f"Part 2: {p2}")


if __name__ == "__main__":
    main()
