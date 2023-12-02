#!/usr/bin/env python3.11

from dataclasses import dataclass, field
from math import prod

from rich import print


@dataclass
class Game:
    number: int
    rounds: list[dict[str, int]] = field(default_factory=list)

    @classmethod
    def fromstr(cls, data: str):
        name, rest = data.split(": ")
        _, name = name.split()
        rounds = []
        for round in rest.split("; "):
            cubes = {}
            for cube in round.split(", "):
                num, color = cube.split(" ")
                cubes[color] = int(num)
            rounds.append(cubes)

        return cls(int(name), rounds)

    def is_valid(self, cubes: dict[str, int]):
        for round in self.rounds:
            for color, num in round.items():
                if cubes.get(color, 0) < num:
                    return False
        return True

    def fewest(self):
        output = {"red": 0, "blue": 0, "green": 0}
        for round in self.rounds:
            for color, num in round.items():
                if output[color] < num:
                    output[color] = num
        return output


def get_data(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return f.read()


def parse_input(data: str):
    return [Game.fromstr(line) for line in data.splitlines()]


def part1(games: list[Game], start: dict[str, int]):
    return sum(game.number for game in games if game.is_valid(start))


def part2(games: list[Game]):
    return sum(prod(game.fewest().values()) for game in games)


def main():
    data = get_data("day02.txt")
    games = parse_input(data)
    start = {"red": 12, "green": 13, "blue": 14}

    p1 = part1(games, start)
    print(f"Part 1: {p1}")

    p2 = part2(games)
    print(f"Part 2: {p2}")


if __name__ == "__main__":
    main()
