#!/usr/bin/env python3.11

import regex as re
from rich import print


def get_data(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return f.read()


def solve(line: str, part2=False):
    first = None
    last = None
    if part2:
        line = tokenize(line)
    for x in line:
        if x.isdigit():
            if first is None:
                first = x
            else:
                last = x
    if last is None:
        last = first
    return int(f"{first}{last}")


def tokenize(line: str):
    names = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }
    name_token = "|".join(names)
    tokens = [("DIGIT", r"\d"), ("NAME", name_token)]
    token_regex = "|".join("(?P<%s>%s)" % pair for pair in tokens)
    for mo in re.finditer(token_regex, line, overlapped=True):
        kind = mo.lastgroup
        value = mo.group()
        if kind == "NAME":
            value = names[value]

        yield value


def main():
    data = get_data("day01.txt")

    p1 = sum(solve(line) for line in data.splitlines())
    print(f"Part 1: {p1}")

    p2 = sum(solve(line, True) for line in data.splitlines())
    print(f"Part 2: {p2}")


if __name__ == "__main__":
    main()
