#!/usr/bin/env python3.11

import re

from rich import print


def get_data(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return f.read()


def parse(line):
    token_spec = [
        ("HEX", r"\\x[0-9a-f]{2}"),
        ("BACKSLASH", r"\\\\"),
        ("QUOTE", r"\\\""),
        ("CHAR", r"[a-z]"),
    ]

    token_reg = "|".join("(?P<%s>%s)" % pair for pair in token_spec)
    for mo in re.finditer(token_reg, line):
        kind = mo.lastgroup
        value = mo.group()
        yield kind, value


def part1(data):
    output = 0
    for line in data.splitlines():
        parsed = list(parse(line))
        total_char = len(line)
        total_mem = len(parsed)
        output += total_char - total_mem
    return output


def part2(data):
    output = 0
    for line in data.splitlines():
        parsed = list(parse(line))
        total_char = len(line)
        total_mem = 6
        for kind, _ in parsed:
            match kind:
                case "HEX":
                    total_mem += 5
                case "BACKSLASH":
                    total_mem += 4
                case "QUOTE":
                    total_mem += 4
                case "CHAR":
                    total_mem += 1
        output += total_mem - total_char
    return output


def main():
    data = get_data("day08.txt")

    p1 = part1(data)
    print(f"Part 1: {p1}")

    p2 = part2(data)
    print(f"Part 2: {p2}")


if __name__ == "__main__":
    main()

# 1474 is low
