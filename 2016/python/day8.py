#!/usr/bin/env python3.11

import re
from dataclasses import dataclass, field
from typing import NamedTuple


class Instr(NamedTuple):
    kind: str
    value1: int
    value2: int


@dataclass
class Screen:
    data: list = field(init=False)
    width: int = 50
    height: int = 6
    lit: int = 0

    def __init__(self):
        self.data = [[False] * self.width for _ in range(self.height)]

    def __str__(self) -> str:
        output = []
        for row in self.data:
            for item in row:
                if item:
                    output.append("x")
                else:
                    output.append(" ")
            output.append("\n")
        return "".join(output)

    def run_instruction(self, instr: Instr):
        match instr.kind:
            case "RECT":
                self.rect(instr.value1, instr.value2)
            case "ROW":
                self.rotate_row(instr.value1, instr.value2)
            case "COL":
                self.rotate_col(instr.value1, instr.value2)
        self.lit = sum(bool(x) for y in self.data for x in y)

    def rect(self, x, y):
        for i in range(y):
            for j in range(x):
                self.data[i][j] = True

    def rotate_row(self, row, by):
        new_row = [False] * self.width
        for i in range(self.width):
            new_row[(i + by) % self.width] = self.data[row][i]
        self.data[row] = new_row

    def rotate_col(self, col, by):
        new_col = [False] * self.height
        for i in range(self.height):
            new_col[(i + by) % self.height] = self.data[i][col]

        for i in range(self.height):
            self.data[i][col] = new_col[i]


def get_data(filename):
    with open(filename, "r", encoding="utf-8") as f:
        yield from f.readlines()


def process_instruction(line):
    token_spec = [
        ("ROW", r"(?<=row y=)(\d+) by (\d+)"),
        ("COL", r"(?<=column x=)(\d+) by (\d+)"),
        ("RECT", r"(?<=rect )(\d+)x(\d+)"),
    ]
    token_regex = "|".join("(?P<%s>%s)" % pair for pair in token_spec)
    for mo in re.finditer(token_regex, line):
        kind = mo.lastgroup
        value = mo.group()

        match kind:
            case "ROW" | "COL":
                value1, value2 = value.split(" by ")
                return Instr(kind, int(value1), int(value2))
            case "RECT":
                value1, value2 = value.split("x")
                return Instr(kind, int(value1), int(value2))
    return None


def main():
    data = get_data("day8.txt")
    instr = [process_instruction(x) for x in data]
    screen = Screen()
    for i in instr:
        screen.run_instruction(i)

    print(f"Part 1: {screen.lit}")
    print("Part 2:\n")
    print(screen)


if __name__ == "__main__":
    main()
