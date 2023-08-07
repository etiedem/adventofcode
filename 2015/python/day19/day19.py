#!/usr/bin/env python3.11

import re
from collections import defaultdict

from rich import print


def get_data(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return f.read()


def parse_backward(data):
    combinations, initial = data.split("\n\n")
    output = defaultdict(list)
    for c in combinations.splitlines():
        start, end = c.split(" => ")
        output[end].append(start)
    return output, initial.strip()


def parse_forward(data):
    combinations, initial = data.split("\n\n")
    output = defaultdict(list)
    for c in combinations.splitlines():
        start, end = c.split(" => ")
        output[start].append(end)
    return output, initial.strip()


def get_options(combinations, initial):
    output = set()
    for seq, replacements in combinations.items():
        for match in re.finditer(seq, initial):
            start, end = match.span()
            for r in replacements:
                tmp = list(initial)
                tmp[int(start) : int(end)] = r
                output.add("".join(tmp))
    return output


def find_sequence(combinations, initial, sequence):
    count = 0
    candidates = {initial}
    while sequence not in candidates:
        tmp = set()
        for candidate in candidates:
            tmp = tmp.union(get_options(combinations, candidate))
        candidates = tmp
        count += 1
    return count


def main():
    data = get_data("day19.txt")
    combinations, initial = parse_forward(data)

    p1 = get_options(combinations, initial)
    print(f"Part 1: {len(p1)}")

    combinations, initial = parse_backward(data)
    p2 = find_sequence(combinations, initial, "e")
    print(f"Part 2: {p2}")


if __name__ == "__main__":
    main()
