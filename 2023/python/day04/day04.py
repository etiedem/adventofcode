#!/usr/bin/env python3.11

from collections import defaultdict
from dataclasses import dataclass, field

from rich import print


@dataclass
class Card:
    id_: int
    points: int
    cards: int
    win: set[int] = field(default_factory=set)
    num: set[int] = field(default_factory=set)

    def __post_init__(self):
        self.cal_points()

    @classmethod
    def from_str(cls, data: str):
        name, rest = data.split(": ")
        _, name = name.split()
        sec1, sec2 = rest.split(" | ")
        return cls(
            int(name), 0, 0, set(map(int, sec1.split())), set(map(int, sec2.split()))
        )

    def cal_points(self):
        self.cards = len(self.win & self.num)
        if self.cards == 1:
            self.points = 1
        elif self.cards > 1:
            self.points = 1 << self.cards - 1
        else:
            self.points = 0


def get_data(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return f.read()


def count_cards(cards: list[Card]):
    counter = defaultdict(int)
    for card in cards:
        counter[card.id_] += 1
        if card.points > 0:
            for idx in range(
                card.id_ + 1, min((card.id_ + card.cards), len(cards)) + 1
            ):
                counter[idx] += counter[card.id_]
    return sum(counter.values())


def main():
    data = get_data("day04.txt")
    cards = [Card.from_str(line) for line in data.splitlines()]

    p1 = sum(card.points for card in cards)
    print(f"Part 1: {p1}")

    p2 = count_cards(cards)
    print(f"Part 2: {p2}")


if __name__ == "__main__":
    main()
