#!/usr/bin/env python3.11

from copy import deepcopy
from dataclasses import dataclass, field
from functools import reduce
from heapq import heappop, heappush
from typing import Iterable


@dataclass
class Character:
    name: str
    hp: int = 0
    mana: int = 0
    dmg: int = 0
    armor: int = 0
    effects: list = field(default_factory=list)

    def __hash__(self) -> int:
        return reduce(
            lambda x, y: x ^ hash(y), (v for k, v in vars(self).items() if k != "effects"), 0
        )


@dataclass
class Effect:
    name: str
    dur: int = 1


@dataclass
class Heal(Effect):
    heal: int = 0
    arm: int = 0
    mana: int = 0


@dataclass
class Harm(Effect):
    dmg: int = 0


@dataclass
class Spell:
    name: str
    cost: int
    effects: list[Effect] = field(default_factory=list)

    def __lt__(self, other):
        return self.cost < other.cost


spells = sorted(
    [
        Spell("Magic Missile", cost=53, effects=[Harm("Magic Missile", dur=1, dmg=4)]),
        Spell(
            "Drain", cost=73, effects=[Heal("Drain", dur=1, heal=2), Harm("Drain", dur=1, dmg=2)]
        ),
        Spell("Shield", cost=113, effects=[Heal("Shield", dur=6, arm=7)]),
        Spell("Poison", cost=173, effects=[Harm("Poison", dmg=3, dur=6)]),
        Spell("Recharge", cost=229, effects=[Heal("Recharge", dur=5, mana=101)]),
    ]
)


class Path(list):
    def __init__(self):
        super(Path, self).__init__()

    def __hash__(self):
        return hash("-".join(sorted(self)))

    def __eq__(self, other):
        return hash(self) == hash(other)


@dataclass
class State:
    player: Character
    boss: Character
    mana_spent: int = 0
    spell_list: Path = field(default_factory=Path)
    hard: bool = False
    win: bool | None = None

    def __hash__(self) -> int:
        return reduce(
            lambda x, y: x ^ hash(y), (v for k, v in vars(self).items() if k != "spell_list"), 0
        )

    def __lt__(self, other):
        return self.mana_spent + self.boss.hp <= other.mana_spent + other.boss.hp

    def __call__(self, spells=spells) -> Iterable:
        for spell in spells:
            state = deepcopy(self)
            state.spell_list.append(spell.name)
            # Player Turn
            if self.hard:
                state.player.hp -= 1
                state._check_hp()
                if state.win is True:
                    yield state
                    continue
                if state.win is False:
                    continue
            state.process_effects()
            if spell.cost > state.player.mana:
                continue
            if any(
                spell.name == e.name and e.dur > 1
                for effect in (self.player.effects, self.boss.effects)
                for e in effect
            ):
                continue
            state.take_turn(state.player, spell)
            state._check_hp()
            if state.win is True:
                yield state
                continue
            if state.win is False:
                continue

            # Boss Turn
            state.process_effects()
            state._check_hp()
            if state.win is True:
                yield state
                continue
            if state.win is False:
                continue
            state.take_turn(state.boss)
            state._check_hp()
            if state.win is True:
                yield state
                continue
            if state.win is False:
                continue
            yield state

    def _check_hp(self):
        if self.player.hp <= 0 or self.player.mana <= 0:
            self.win = False
        elif self.boss.hp <= 0:
            self.win = True

    def process_effects(self):
        for char in (self.player, self.boss):
            for effect in char.effects:
                match effect:
                    case Harm(_, _, dmg):
                        dmg = max(dmg - char.armor, 1)
                        char.hp -= dmg
                    case Heal(_, _, heal, arm, mana):
                        char.hp += heal
                        char.mana += mana
                        if char.armor == 0:
                            char.armor += arm
                effect.dur -= 1
                if effect.dur <= 0:
                    if effect.name == "Shield":
                        char.armor = 0
                    char.effects.remove(effect)

    def take_turn(self, char, spell=None):
        if char.dmg > 0:
            dmg = max(char.dmg - self.player.armor, 1)
            self.player.hp -= dmg

        if spell:
            char.mana -= spell.cost
            self.mana_spent += spell.cost
            for effect in spell.effects:
                match effect:
                    case Harm(_, dur, dmg):
                        if dur == 1:
                            self.boss.hp -= dmg
                        else:
                            self.boss.effects.append(deepcopy(effect))
                    case Heal():
                        self.player.effects.append(deepcopy(effect))


def search(start):
    queue = [start]
    while queue:
        current = heappop(queue)

        if current.win is True:
            return current
        for candidate in current():
            if candidate in queue:
                continue
            heappush(queue, candidate)
    return None


def get_data(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return f.read()


def parse(data):
    return tuple(int(d[-1]) for line in data.splitlines() if (d := line.split()))


def main(args):
    data = get_data("day22.txt")
    b_hp, b_dmg = parse(data)
    player = Character("Player", 50, 500, 0)
    boss = Character("Boss", b_hp, 0, b_dmg)

    state = State(player, boss)
    p1 = search(state)
    print(f"Part 1: {p1.mana_spent}")
    if args.verbose:
        print(*p1.spell_list, sep=" - ")

    state = State(player, boss, hard=True)
    p2 = search(state)
    print(f"Part 2: {p2.mana_spent}")
    if args.verbose:
        print(*p2.spell_list, sep=" - ")


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--verbose", action="store_true")
    main(parser.parse_args())
