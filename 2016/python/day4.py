#!/usr/bin/env python3.11

import re
from collections import Counter
from operator import itemgetter
from string import ascii_lowercase
from typing import Any

from rich import print


class MyCounter(Counter):
    def most_common(self, n: int | None = None) -> list[tuple[Any, int]]:
        if n is None:
            return sorted(sorted(self.items(), key=itemgetter(0)), key=itemgetter(1), reverse=True)

        return sorted(sorted(self.items(), key=itemgetter(0)), key=itemgetter(1), reverse=True)[:n]


class Room:
    def __init__(self, data) -> None:
        self.name = []
        self.sector_id: int = None
        self.checksums = []
        self.counter = MyCounter()
        self.real: str = None

        token = [
            ("SECTOR", r"\d+"),  # must be before ID
            ("ID", r"\w+"),
            ("SKIP", r"-"),
            ("START", r"\["),
            ("END", r"\]"),
        ]
        token_regex = "|".join("(?P<%s>%s)" % pair for pair in token)
        checksum = False
        for mo in re.finditer(token_regex, data):
            kind = mo.lastgroup
            value = mo.group()
            if kind == "SKIP":
                continue

            if kind in ("STOP", "START"):
                checksum = not checksum
            elif kind == "SECTOR":
                self.sector_id = int(value)
            elif kind == "ID" and checksum:
                self.checksums.append(value)
            elif kind == "ID":
                self.name.append(value)
                self.counter.update(Counter(value))

        self.valid = "".join(x[0] for x in self.counter.most_common(5)) == self.checksums[0]
        self.real = self.__shift()

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__}\n{self.__dict__}>"

    def __shift(self) -> str:
        result = []
        for section in self.name:
            for letter in section:
                result.append(ascii_lowercase[(ascii_lowercase.find(letter) + self.sector_id) % 26])
            result.append(" ")
        return "".join(result)


def get_data(filename):
    with open(filename, "r", encoding="utf8") as f:
        yield from map(str.strip, f.readlines())


def main():
    data = get_data("day4.txt")
    rooms = [Room(room) for room in data]

    part1 = sum(room.sector_id for room in rooms if room.valid)
    print(f"Part1: {part1}")

    part2 = next(room.sector_id for room in rooms if "north" in room.real)
    print(f"Part2: {part2}")

    main()
