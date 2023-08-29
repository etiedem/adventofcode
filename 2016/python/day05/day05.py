#!/usr/bin/env python3.11

from hashlib import md5

from rich import print


def get_data(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return f.read()


def next_hash(data):
    counter = 0
    while True:
        cur = f"{data}{counter}"
        if (hash := md5(cur.encode()).hexdigest()) and hash.startswith("00000"):
            yield cur, hash
        counter += 1


def part1(data):
    h = next_hash(data)
    return "".join(next(h)[1][5] for _ in range(8))


def part2(data):
    result = [None for _ in range(8)]
    h = next_hash(data)
    while any(x is None for x in result):
        idx, cur = next(h)[1][5:7]
        try:
            idx = int(idx)
        except ValueError:
            continue
        if idx < len(result) and result[idx] is None:
            result[idx] = cur
    return "".join(result)


def main():
    data = get_data("day05.txt")

    p1 = part1(data)
    print(f"Part 1: {p1}")

    p2 = part2(data)
    print(f"Part 2: {p2}")


if __name__ == "__main__":
    main()
