#!/usr/bin/env python3.11

import string
from dataclasses import dataclass
from itertools import islice

LOOKUP = [*string.ascii_lowercase, *string.ascii_uppercase]


def batched(iterable, n):
    "Batch data into tuples of length n. The last batch may be shorter."
    # batched('ABCDEFG', 3) --> ABC DEF G
    if n < 1:
        raise ValueError("n must be at least one")
    it = iter(iterable)
    while batch := tuple(islice(it, n)):
        yield batch


@dataclass
class RuckSack:
    left: set
    right: set
    full: set

    def __init__(self, data: str) -> None:
        self.left, self.right = set(data[: len(data) // 2]), set(data[len(data) // 2 :])
        self.full = set(data)

    def find_common(self) -> set:
        return self.left.intersection(self.right)


def item_to_priority(item: str) -> int:
    return LOOKUP.index(item) + 1


def get_data():
    with open("day3.txt") as f:
        for line in f:
            yield RuckSack(line.strip())


def main():
    part1 = sum(item_to_priority(pri) for item in get_data() for pri in item.find_common())
    part2 = sum(
        item_to_priority(item)
        for x, y, z in batched(get_data(), 3)
        for item in x.full.intersection(y.full, z.full)
    )
    print(f"Part 1: {part1}")
    print(f"Part 2: {part2}")


if __name__ == "__main__":
    main()
