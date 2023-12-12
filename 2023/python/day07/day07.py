#!/usr/bin/env python3.11

from rich import print
from dataclasses import dataclass, field
from enum import IntEnum
from collections import Counter


@dataclass(order=True, unsafe_hash=True)
class Card:
    card: str = field(compare=False)
    value: int


class HandType(IntEnum):
    HIGH_CARD = 0
    PAIR = 1
    TWO_PAIR = 2
    THREE_OF_A_KIND = 3
    FULL_HOUSE = 4
    FOUR_OF_A_KIND = 5
    FIVE_OF_A_KIND = 6


@dataclass(order=True)
class Hand:
    bet: int = field(compare=False)
    htype: HandType = field(init=False)
    cards: list[Card]
    part2: bool = field(compare=False, default=False)

    def __post_init__(self):
        self.htype = self.get_hand_type()

    def get_hand_type(self):
        count = Counter(c.card for c in self.cards)
        if len(count) == 1:
            return HandType.FIVE_OF_A_KIND
        elif self.part2 and "J" in count:
            return self.jokers_wild(count)
        elif len(count) == 2:
            if 2 in count.values():
                return HandType.FULL_HOUSE
            else:
                return HandType.FOUR_OF_A_KIND
        elif len(count) == 3:
            if 3 in count.values():
                return HandType.THREE_OF_A_KIND
            else:
                return HandType.TWO_PAIR
        elif len(count) == 4:
            return HandType.PAIR
        return HandType.HIGH_CARD

    def jokers_wild(self, count: Counter):
        if len(count) == 2:
            return HandType.FIVE_OF_A_KIND
        elif len(count) == 3:
            if 3 in count.values():
                return HandType.FOUR_OF_A_KIND
            else:
                if count["J"] == 2:
                    return HandType.FOUR_OF_A_KIND
                else:
                    return HandType.FULL_HOUSE
        elif len(count) == 4:
            return HandType.THREE_OF_A_KIND
        else:
            return HandType.PAIR


def parse_card(card: str, part2: bool = False):
    mapping = {
        "A": 14,
        "K": 13,
        "Q": 12,
        "J": 11,
        "T": 10,
        "9": 9,
        "8": 8,
        "7": 7,
        "6": 6,
        "5": 5,
        "4": 4,
        "3": 3,
        "2": 2,
    }
    if part2:
        mapping["J"] = 1

    return Card(card, mapping[card])


def get_data(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return f.read()


def parse(data: str, part2: bool = False):
    for d in data.splitlines():
        cards, bet = d.split()
        cards = [parse_card(c, part2) for c in cards]
        yield Hand(cards=cards, bet=int(bet), part2=part2)


def total_winnings(hands: list[Hand]):
    return sum(h.bet * idx for idx, h in enumerate(sorted(hands), 1))


def main():
    data = get_data("day07.txt")

    p1 = total_winnings(parse(data))
    print(f"Part 1: {p1}")

    p2 = total_winnings(parse(data, part2=True))
    print(f"Part 2: {p2}")


if __name__ == "__main__":
    main()
