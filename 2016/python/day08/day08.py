#!/usr/bin/env python3.11

import re
from dataclasses import dataclass, field
from typing import NamedTuple


class Instr(NamedTuple):
    kind: str
    value1: int
    value2: int

    @classmethod
    def from_str(cls, data):
        token_spec = [
            ("ROW", r"(?<=row y=)(\d+) by (\d+)"),
            ("COL", r"(?<=column x=)(\d+) by (\d+)"),
            ("RECT", r"(?<=rect )(\d+)x(\d+)"),
        ]
        token_regex = "|".join("(?P<%s>%s)" % pair for pair in token_spec)
        for mo in re.finditer(token_regex, data):
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

    def run_instructions(self, instr: list[Instr]):
        for i in instr:
            match i.kind:
                case "RECT":
                    self.rect(i.value1, i.value2)
                case "ROW":
                    self.rotate_row(i.value1, i.value2)
                case "COL":
                    self.rotate_col(i.value1, i.value2)
            self.lit = sum(bool(x) for y in self.data for x in y)
        return self

    def rect(self, i, j):
        for y in range(j):
            for x in range(i):
                self.data[y][x] = True

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
        return f.read()


def main():
    data = get_data("day08.txt")
    instr = [Instr.from_str(x) for x in data.splitlines()]
    screen = Screen().run_instructions(instr)

    print(f"Part 1: {screen.lit}")
    print(f"Part 2: \n{screen}")


if __name__ == "__main__":
    main()
