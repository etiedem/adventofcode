#!/usr/bin/env python3.11

from dataclasses import dataclass
from re import compile

from rich import print

LINE_RE = compile(r"(?:Sue (\d+):)|(?:(\w+):\s(\d+)(?:,\s)?)")


@dataclass
class Sue:
    number: int
    children: int | None = None
    cats: int | None = None
    samoyeds: int | None = None
    pomeranians: int | None = None
    akitas: int | None = None
    vizslas: int | None = None
    goldfish: int | None = None
    trees: int | None = None
    cars: int | None = None
    perfumes: int | None = None

    def part1(self, other) -> bool:
        for key, value in self.__dict__.items():
            if key == "number":
                continue
            if value is None or getattr(other, key) is None:
                continue
            if value != getattr(other, key):
                return False
        return True

    def part2(self, other) -> bool:
        for key, value in self.__dict__.items():
            if key == "number":
                continue
            if value is None or getattr(other, key) is None:
                continue
            if key in ("cats", "trees"):
                if value <= getattr(other, key):
                    return False
            elif key in ("pomeranians", "goldfish"):
                if value >= getattr(other, key):
                    return False
            elif value != getattr(other, key):
                return False
        return True


def get_data(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return f.read()


def parse(data):
    results = []
    for line in data.splitlines():
        matches = LINE_RE.findall(line)
        aunt = Sue(int(matches[0][0]))
        for x in matches[1:]:
            setattr(aunt, x[1], int(x[2]))
        results.append(aunt)
    return results


def main():
    data = get_data("day16.txt")
    aunts = parse(data)
    aunt_clue = Sue(0, 3, 7, 2, 3, 0, 0, 5, 3, 2, 1)

    p1 = next(filter(lambda x: x.part1(aunt_clue), aunts)).number
    print(f"Part 1: {p1}")

    p2 = next(filter(lambda x: x.part2(aunt_clue), aunts)).number
    print(f"Part 2: {p2}")


if __name__ == "__main__":
    main()
