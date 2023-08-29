#!/usr/bin/env python3.11

from collections import Counter
from dataclasses import dataclass, field
from string import ascii_lowercase

from rich import print


class MyCounter(Counter):
    def most_common(self, n):
        if not n:
            sorted(
                self.items(),
                key=lambda x: (-x[1], x[0]),
            )

        return sorted(
            self.items(),
            key=lambda x: (-x[1], x[0]),
        )[:n]


@dataclass
class Room:
    checksum: str
    sector: int
    encrypt_name: str
    name: str = field(init=False)

    def __post_init__(self):
        self.name = self.__decrypt()

    @classmethod
    def from_str(cls, data):
        encrypt_name = data[: data.rfind("-")]
        sector = int(data[data.rfind("-") + 1 : data.find("[")])
        checksum = data[data.find("[") + 1 : -1]

        return Room(checksum, sector, encrypt_name)

    def is_real(self):
        counter = MyCounter(x for x in self.encrypt_name if x.isalpha())
        return "".join(x[0] for x in counter.most_common(5)) == self.checksum

    def __decrypt(self):
        output = []
        for letter in self.encrypt_name:
            if letter == "-":
                output.append(" ")
                continue
            idx = ascii_lowercase.find(letter)
            idx = (idx + self.sector) % len(ascii_lowercase)
            output.append(ascii_lowercase[idx])
        return "".join(output)


def get_data(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return f.read()


def main():
    data = get_data("day04.txt")
    rooms = [Room.from_str(x) for x in data.splitlines()]

    p1 = sum(r.sector for r in rooms if r.is_real())
    print(f"Part 1: {p1}")

    p2 = next(r.sector for r in rooms if r.is_real() and "north" in r.name)
    print(f"Part 2: {p2}")


if __name__ == "__main__":
    main()
