#!/usr/bin/env python3.11

from rich import print


def get_data(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return f.read()


def part1(data: str) -> int:
    prev = data[0]
    output = 0
    for char in data[1:]:
        if char == prev:
            output += int(char)
        prev = char

    if char == data[0]:
        output += int(char)

    return output


def part2(data: str) -> int:
    length = len(data)
    return sum(
        int(char) for idx, char in enumerate(data) if char == data[(idx + length // 2) % length]
    )


def main():
    data = get_data("day01.txt")

    p1 = part1(data)
    print(f"Part 1: {p1}")

    p2 = part2(data)
    print(f"Part 2: {p2}")


if __name__ == "__main__":
    main()
