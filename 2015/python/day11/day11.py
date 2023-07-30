#!/usr/bin/env python3.11

import re

from more_itertools import sliding_window
from rich import print

PAIRS_RE = re.compile(r"(.)\1.*([^\1])\2")


def get_data(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return f.read()


def is_valid(password):
    if any(l in ("i", "o", "l") for l in password):
        return False
    if not PAIRS_RE.search(password):
        return False
    for a, b, c in sliding_window(password, 3):
        if ord(b) == ord(a) + 1 and ord(c) == ord(b) + 1:
            return True
    return False


def next_password(cur_pass):
    candidate = list(cur_pass)
    candidate.reverse()
    for idx, l in enumerate(candidate):
        if l < "z":
            candidate[idx] = chr(ord(l) + 1)
            break
        candidate[idx] = "a"
    candidate.reverse()
    return "".join(candidate)


def solve(cur_pass):
    candidate = cur_pass
    while True:
        candidate = next_password(candidate)
        if is_valid(candidate):
            return candidate


def main():
    data = get_data("day11.txt")

    p1 = solve(data)
    print(f"Part 1: {p1}")

    p2 = solve(p1)
    print(f"Part 2: {p2}")


if __name__ == "__main__":
    main()
