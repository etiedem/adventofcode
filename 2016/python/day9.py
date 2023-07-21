#!/usr/bin/env python3.11

# from rich import print


import re


def get_data(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return f.read()


def tokenize(data):
    token_spec = [("REPEAT", r"\(.*?\)"), ("REST", r"(?:\w+|\W+)")]
    token_regex = "|".join("(?P<%s>%s)" % pair for pair in token_spec)
    for mo in re.finditer(token_regex, data):
        kind = mo.lastgroup
        value = mo.group()

        yield (kind, value)


def decompress(value, token_data, recursive=False):
    result = 0
    num, repeat = map(int, value.lstrip("(").rstrip(")").split("x"))
    kind, chars = next(token_data)

    if kind == "REPEAT" and recursive:
        result += decompress(chars, token_data, recursive=True)
    else:
        while len(chars) < num:
            kind, t = next(token_data)
            chars += t
        result += repeat * len(chars[:num])
        result += len(chars[num:])

    return result


def run(data, recursive=False):
    result = 0
    token_data = tokenize(data)
    for token in token_data:
        match token:
            case ["REST", value]:
                result += len(value)
            case ["REPEAT", value]:
                result += decompress(value, token_data, recursive=recursive)
    return result


def main():
    data = get_data("day9.txt").strip()
    part1 = run(data)
    print(f"Part 1: {part1}")

    part2 = run(data, recursive=True)
    print(f"Part 2: {part2}")


if __name__ == "__main__":
    main()

# Part 2:
# 140,888 is too low
