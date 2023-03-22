#!/usr/bin/env python3.11


from dataclasses import dataclass


@dataclass
class Pairs:
    first: set
    second: set

    def __init__(self, data) -> None:
        first, second = data.split(",")
        self.first = self._generate_sequence(*map(int, first.split("-")))
        self.second = self._generate_sequence(*map(int, second.split("-")))

    def fully_contained(self) -> set:
        return self.first.issuperset(self.second) or self.second.issuperset(self.first)

    def partially_contained(self) -> set:
        return self.first.intersection(self.second)

    def _generate_sequence(self, start: int, end: int):
        return set(range(start, end + 1))


def get_data(filename):
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            yield line.strip()


def main():
    data = [Pairs(d) for d in get_data("day4.txt")]
    part1 = sum(1 for d in data if d.fully_contained())
    part2 = sum(1 for d in data if d.partially_contained())
    print(f"Part 1: {part1}")
    print(f"Part 2: {part2}")


if __name__ == "__main__":
    main()
