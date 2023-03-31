#!/usr/bin/env python3.11

import operator
from dataclasses import dataclass
from typing import Callable

from numpy import prod


@dataclass
class Monkey:
    name: int
    items: list[int]
    op: Callable[[int], int]
    test: int
    iftrue: int
    iffalse: int
    inspections: int = 0


def get_data(filename):
    with open(filename, "r", encoding="utf-8") as f:
        yield from f.read().split("\n\n")


def parse_monkey(data):
    data = data.splitlines()
    name = data[0].split(" ")[-1].rstrip(":")
    items = [int(x) for x in data[1].split(": ")[-1].split(", ")]
    test = int(data[3].split(" ")[-1])
    iftrue = int(data[4].split(" ")[-1])
    iffalse = int(data[5].split(" ")[-1])
    operation_raw = data[2].split(" = ")[-1].lstrip("old").split()
    match operation_raw:
        case ["*", "old"]:
            operation = lambda x: x * x
        case ["+", y]:
            operation = lambda x: x + int(y)
        case ["*", y]:
            operation = lambda x: x * int(y)
        case _:
            raise ValueError("Unknown operation {operation_raw}")
    return Monkey(name, items, operation, test, iftrue, iffalse)


def step(monkeys, part1: bool):
    modvalue = prod([monkey.test for monkey in monkeys])
    for monkey in monkeys:
        for item in monkey.items:
            if part1:
                item = monkey.op(item) // 3
            else:
                item = monkey.op(item) % modvalue
            monkey.inspections += 1
            if item % monkey.test == 0:
                monkeys[monkey.iftrue].items.append(item)
            else:
                monkeys[monkey.iffalse].items.append(item)
        monkey.items.clear()


def main():
    p1_monkeys = [parse_monkey(data) for data in get_data("day11.txt")]
    p2_monkeys = [parse_monkey(data) for data in get_data("day11.txt")]

    for _ in range(20):
        step(p1_monkeys, True)
    for _ in range(10000):
        step(p2_monkeys, False)

    part1 = prod(
        [
            monkey.inspections
            for monkey in sorted(p1_monkeys, key=lambda x: x.inspections, reverse=True)[:2]
        ]
    )
    print(f"Part 1: {part1}")

    part2 = prod(
        [
            monkey.inspections
            for monkey in sorted(p2_monkeys, key=lambda x: x.inspections, reverse=True)[:2]
        ]
    )
    print(f"Part 2: {part2}")


if __name__ == "__main__":
    main()
