#!/usr/bin/env python3.11

from operator import itemgetter

import portion as P
from rich import print


def get_data(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return f.read()


def parse_data(data: str):
    sections = data.split("\n\n")
    seeds = tuple(map(int, sections[0].split()[1:]))
    output = []
    for section in sections[1:]:
        row = []
        for s in section.split("\n")[1:]:
            if s:
                dest, src, r = map(int, s.split())
                row.append((P.closed(dest, dest + r), P.closed(src, src + r)))
        output.append(row)

    return seeds, output


def search(lookup):
    print(lookup)
    previous = lookup[0]
    # previous = [previous[0]]
    previous = [(P.closed(79, 93), [])]

    # previous = [(P.closed(79, 79), [])]
    for section in lookup[1:]:
        next = []
        for prev in previous:
            NOMATCH = True
            dst = ""
            for piece in section:
                if piece[1].contains(prev[0]):
                    low = prev[0].lower - piece[1].lower
                    high = prev[0].upper - prev[0].lower + low
                    dst = P.closed(piece[0].lower + low, piece[0].lower + high)
                    src = P.closed(piece[1].lower + low, piece[1].lower + high)
                    next.append((dst, src))
                    NOMATCH = False
                elif piece[1].overlaps(prev[0]):
                    src = piece[1].intersection(prev[0])
                    low = src.lower - piece[1].lower
                    high = src.upper - src.lower + low
                    dst = P.closed(piece[0].lower + low, piece[0].lower + high)
                    next.append((dst, src))
                    NOMATCH = False
                if dst:
                    print(f"src={prev[0]} {dst=}")
            if NOMATCH:
                next.append((prev[0], prev[0]))

        previous = next
    return previous


def create_range(seeds: list[int], part2: bool):
    output = []
    if part2:
        for start, stop in zip(seeds[::2], seeds[1::2]):
            output.append(P.closed(start, start + stop))
    else:
        for seed in seeds:
            output.append((P.closed(seed, seed), []))
    return output


def solve(data: str, location: int, part2: bool = False):
    seeds, lookup = parse_data(data)
    seeds = create_range(seeds, part2)
    map = [seeds, *lookup]

    test = []
    for idx in range(10):
        test.append(idx)

    # return min(search(map), key=itemgetter(0))[0].lower
    return sorted(search(map), key=itemgetter(0))


def main():
    # data = get_data("day05.txt")
    data = get_data("example.txt")

    # p1 = solve(data, 35)
    # print(f"Part 1: {p1}")

    p2 = solve(data, 35, True)
    print(f"Part 2: {p2}")

    # 51515303 is too high


if __name__ == "__main__":
    main()
