#!/usr/bin/env python3.11

from collections import defaultdict
from dataclasses import dataclass, field

from rich import print


@dataclass
class Card:
    id_: int
    points: int
    cards: int
    win: list[int] = field(default_factory=list)
    num: list[int] = field(default_factory=list)

    def __post_init__(self):
        self.cal_points()

    @classmethod
    def from_str(cls, data: str):
        name, rest = data.split(": ")
        _, name = name.split()
        sec1, sec2 = rest.split(" | ")
        return cls(
            int(name), 0, 0, list(map(int, sec1.split())), list(map(int, sec2.split()))
        )

    def cal_points(self):
        count = 0
        for n in self.win:
            if n in self.num:
                count += 1
        self.cards = count
        if count == 1:
            self.points = 1
        elif count > 1:
            self.points = 1 << count - 1
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
