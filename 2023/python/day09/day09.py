#!/usr/bin/env python3.11

from rich import print


def get_data(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return f.read()


def parse(data: str):
    return [list(map(int, line.split())) for line in data.splitlines()]


def part1(data: list[int]):
    current = [data]
    new = []
    while any(x != 0 for x in current[-1][1:-1]):
        new.extend(y - x for x, y in zip(current[-1], current[-1][1:]))
        current.append(new[:])
        new.clear()

    current.reverse()

    forward = current[0][-1]
    backward = current[0][0]
    for c in current[1:]:
        forward += c[-1]
        backward = c[0] - backward

    return backward, forward


def solve(sensor: list[list[int]]):
    prior, future = [], []
    for line in sensor:
        prev, next = part1(line)
        prior.append(prev)
        future.append(next)

    return sum(future), sum(prior)


def main():
    data = get_data("day09.txt")
    sensor = parse(data)

    p1, p2 = solve(sensor)

    print(f"Part 1: {p1}")
    print(f"Part 2: {p2}")


if __name__ == "__main__":
    main()
