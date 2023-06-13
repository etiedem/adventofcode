#!/usr/bin/env python3.11

from dataclasses import dataclass, field

from rich import print


@dataclass
class FancyNumPad:
    grid: list[list[int]] = field(init=False)
    current: tuple[int, int] = field(init=False)

    def __post_init__(self):
        self.grid = [
            ["", "", "1", "", ""],
            ["", "2", "3", "4", ""],
            ["5", "6", "7", "8", "9"],
            ["", "A", "B", "C", ""],
            ["", "", "D", "", ""],
        ]
        self.current = (0, 2)

    def move(self, direction):
        cx, cy = self.current

        match direction:
            case "U":
                cy -= 1
                if cy < 0 or not self.grid[cy][cx]:
                    cy += 1
            case "D":
                cy += 1
                if cy > 4 or not self.grid[cy][cx]:
                    cy -= 1
            case "L":
                cx -= 1
                if cx < 0 or not self.grid[cy][cx]:
                    cx += 1
            case "R":
                cx += 1
                if cx > 4 or not self.grid[cy][cx]:
                    cx -= 1
        self.current = (cx, cy)

    def show(self):
        cx, cy = self.current
        return self.grid[cy][cx]


@dataclass
class NumPad:
    grid: list[list[int]] = field(init=False)
    current: tuple[int, int] = field(init=False)

    def __post_init__(self):
        self.grid = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]
        self.current = (1, 1)

    def show(self):
        cx, cy = self.current
        return self.grid[cy][cx]

    def move(self, direction):
        cx, cy = self.current
        match direction:
            case "U":
                cy = 0 if cy < 1 else cy - 1
            case "D":
                cy = 2 if cy > 1 else cy + 1
            case "L":
                cx = 0 if cx < 1 else cx - 1
            case "R":
                cx = 2 if cx > 1 else cx + 1
        self.current = (cx, cy)


def get_data(filename):
    with open(filename, "r", encoding="utf8") as f:
        yield from map(str.strip, f)


def main():
    data = list(get_data("day2.txt"))
    part1: str = ""
    pad = NumPad()
    for line in data:
        for move in line:
            pad.move(move)
        part1 += pad.show()

    print(f"Part 1: {part1}")

    part2: str = ""
    fancy_pad = FancyNumPad()
    for line in data:
        for move in line:
            fancy_pad.move(move)
        part2 += fancy_pad.show()

    print(f"Part 2: {part2}")


if __name__ == "__main__":
    main()
