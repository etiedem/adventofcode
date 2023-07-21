#!/usr/bin/env python3.11

from rich import print


def get_data(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return f.read().splitlines()


def parse(data):
    for line in data:
        yield tuple(map(int, line.split("x")))


def get_sq_ft(l, w, h):
    small = min((l * w, w * h, l * h))
    return 2 * l * w + 2 * w * h + 2 * h * l + small


def get_ribbon(l, w, h):
    small = sorted((l, w, h))[:2]
    return small[0] * 2 + small[1] * 2 + l * w * h


def part1(data):
    return sum(get_sq_ft(*dims) for dims in parse(data))


def part2(data):
    return sum(get_ribbon(*dims) for dims in parse(data))


def main():
    data = get_data("day02.txt")

    p1 = part1(data)
    print(f"Part 1: {p1}")

    p2 = part2(data)
    print(f"Part 2: {p2}")


if __name__ == "__main__":
    main()
