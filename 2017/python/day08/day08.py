#!/usr/bin/env python3.11

from collections import defaultdict
from dataclasses import dataclass, field

from rich import print


@dataclass
class Instr:
    register: str
    action: str
    value: int
    condition: list = field(default_factory=list)

    @classmethod
    def from_str(cls, string: str):
        values = string.split(maxsplit=3)
        return Instr(
            values[0],
            values[1],
            int(
                values[2],
            ),
            values[3].split(" ")[1:],
        )


def get_data(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return f.read()


def solve(instr: list[Instr]):
    registers = defaultdict(int)
    highest = 0

    for i in instr:
        if eval(f"{registers[i.condition[0]]} {i.condition[1]} {i.condition[2]}"):
            match i.action:
                case "inc":
                    val = i.value * 1
                case "dec":
                    val = i.value * -1
            registers[i.register] += val
            highest = max(highest, registers[i.register])
    return max(registers.values()), highest


def main():
    data = get_data("day08.txt")
    instructions = [Instr.from_str(x) for x in data.splitlines()]

    p1, p2 = solve(instructions)
    print(f"Part 1: {p1}")
    print(f"Part 2: {p2}")


if __name__ == "__main__":
    main()
