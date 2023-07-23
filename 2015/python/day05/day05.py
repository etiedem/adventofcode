#!/usr/bin/env python3.11

import re

from rich import print

VOWEL_RE = re.compile(r"[aeiou]")
TWICE_RE = re.compile(r"(.)\1")
PAIR_RE = re.compile(r"(.)(.).*\1\2")
ABA_RE = re.compile(r"(.).\1")


def get_data(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return f.read()


def part1(data):
    for bad in ["ab", "cd", "pq", "xy"]:
        if bad in data:
            return False
    if len(VOWEL_RE.findall(data)) < 3:
        return False
    if not TWICE_RE.search(data):
        return False
    return True


def part2(data):
    if not PAIR_RE.search(data):
        return False
    if not ABA_RE.search(data):
        return False
    return True


def main():
    data = get_data("day05.txt")

    p1 = sum(bool(part1(line)) for line in data.splitlines())
    print(f"Part 1: {p1}")

    p2 = sum(bool(part2(line)) for line in data.splitlines())
    print(f"Part 2: {p2}")


if __name__ == "__main__":
    main()
