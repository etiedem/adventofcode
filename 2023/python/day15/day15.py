#!/usr/bin/env python3.11

import contextlib
from collections import defaultdict
from dataclasses import dataclass, field
from re import compile

from rich import print

LINE_RE = compile(r"(\w+)([-=])(\w+)?")


@dataclass(order=True)
class Lens:
    label: str
    flength: int = field(compare=False)


def get_data(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return f.read()


def hash(data: str):
    current = 0
    for item in data:
        current += ord(item)
        current *= 17
        current %= 256
    return current


def part1(data: str):
    return sum(hash(item) for item in data.split(","))


def part2(data: str):
    boxes = defaultdict(list)

    for item in data.split(","):
        label, action, flength = LINE_RE.match(item).groups()
        box = hash(label)
        match action:
            case "-":
                with contextlib.suppress(ValueError):
                    boxes[box].remove(Lens(label, 0))
            case "=":
                lens = Lens(label, int(flength))
                if lens in boxes[box]:
                    idx = boxes[box].index(lens)
                    boxes[box].remove(lens)
                    boxes[box].insert(idx, Lens(label, int(flength)))
                else:
                    boxes[box].append(Lens(label, int(flength)))
    return boxes


def calc_total_focal_length(boxes):
    total_focal_length = 0
    for bidx, box in boxes.items():
        for idx, lens in enumerate(box, 1):
            total_focal_length += (bidx + 1) * lens.flength * idx
    return total_focal_length


def main():
    data = get_data("day15.txt").strip()

    p1 = part1(data)
    print(f"Part 1: {p1}")

    p2 = calc_total_focal_length(part2(data))
    print(f"Part 2: {p2}")


if __name__ == "__main__":
    main()

