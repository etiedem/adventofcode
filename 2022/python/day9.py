#!/usr/bin/env python3.11

from dataclasses import dataclass

from more_itertools import minmax
from rich import print


@dataclass(frozen=True, eq=True)
class Pos:
    x: int
    y: int

    def __sub__(self, other: "Pos") -> "Pos":
        return Pos(self.x - other.x, self.y - other.y)

    def __add__(self, other: "Pos") -> "Pos":
        return Pos(self.x + other.x, self.y + other.y)


class Rope:
    def __init__(self, num_segments: int) -> None:
        self.segments: list[Pos] = [Pos(0, 0) for _ in range(num_segments)]
        self.all_pos: set[Pos] = {Pos(0, 0)}

    def __repr__(self) -> str:
        return f"Rope({self.head}, {self.tail})"

    def move(self, direction: str, distance: int):
        for _ in range(distance):
            match direction:
                case "U":
                    self.segments[0] = self.segments[0] + Pos(0, 1)
                case "D":
                    self.segments[0] = self.segments[0] + Pos(0, -1)
                case "R":
                    self.segments[0] = self.segments[0] + Pos(1, 0)
                case "L":
                    self.segments[0] = self.segments[0] + Pos(-1, 0)
                case _:
                    raise ValueError(f"Unknown direction {direction}")

            for idx, cur in enumerate(self.segments[1:], 1):
                prev = self.segments[idx - 1]
                self.segments[idx] = self._move_segment(prev, cur)
                if idx == len(self.segments) - 1:
                    self.all_pos.add(self.segments[idx])

    def _move_segment(self, prev: Pos, cur: Pos) -> Pos:
        diff = prev - cur
        distance = 1
        x, y = 0, 0
        if abs(diff.x) > distance or abs(diff.y) > distance:
            if diff.x > 0:
                x = 1
            elif diff.x < 0:
                x = -1
            if diff.y > 0:
                y = 1
            elif diff.y < 0:
                y = -1
        return cur + Pos(x, y)

    def show_tail(self):
        min_x, max_x = minmax(self.segments, lambda p: p.x)
        min_y, max_y = minmax(self.segments, lambda p: p.y)

        for y in range(max_y, min_y - 1, -1):
            for x in range(min_x, max_x + 1):
                if x == 0 and y == 0:
                    print("s", end="")
                elif Pos(x, y) in self.all_pos:
                    print("#", end="")
                else:
                    print(".", end="")
            print()


def get_data(filename):
    with open(filename, "r", encoding="utf-8") as f:
        yield from f.readlines()


def main():
    part1_rope = Rope(2)
    part2_rope = Rope(10)
    for line in get_data("day9.txt"):
        direction, distance = line.strip().split()
        part1_rope.move(direction, int(distance))
        part2_rope.move(direction, int(distance))
    print(f"Part 1: {len(part1_rope.all_pos)}")
    print(f"Part 2: {len(part2_rope.all_pos)}")


if __name__ == "__main__":
    main()
