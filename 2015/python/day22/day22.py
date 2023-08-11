#!/usr/bin/env python3.11

from copy import deepcopy
from dataclasses import dataclass, field
from heapq import heappop, heappush
from typing import Any

from rich import print


@dataclass
class Effect:
    name: str
    dur: int = 0

    def __eq__(self, other) -> bool:
        return self.name == other.name

    def __hash__(self) -> int:
        return hash(self.name)


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
    cost: int = 0
    effects: list[Effect] = field(default_factory=list)

    def __eq__(self, other) -> bool:
        return self.name == other.name

    def __lt__(self, other) -> bool:
        return self.cost < other.cost

    def __hash__(self) -> int:
        return hash(self.name)


spells = (
    Spell("Magic Missile", cost=53, effects=[Harm("Magic Missile", dur=1, dmg=4)]),
    Spell("Drain", cost=73, effects=[Heal("Drain", dur=1, heal=2), Harm("Drain", dur=1, dmg=2)]),
    Spell("Shield", cost=113, effects=[Heal("Shield", dur=6, arm=7)]),
    Spell("Poison", cost=173, effects=[Harm("Poison", dmg=3, dur=6)]),
    Spell("Recharge", cost=229, effects=[Heal("Recharge", dur=5, mana=101)]),
)


@dataclass
class Character:
    health: int = 50
    armor: int = 0
    effects: list[Effect] = field(default_factory=list)


@dataclass
class Player(Character):
    mana: int = 500

    def __hash__(self) -> int:
        return hash((self.health, self.armor, self.mana))


@dataclass
class Boss(Character):
    dmg: int = 0

    def __hash__(self) -> int:
        return hash((self.health, self.armor))


@dataclass
class Path:
    path: list[str] = field(default_factory=list)

    def append(self, path):
        self.path.append(path)

    def __len__(self):
        return len(self.path)

    def __lt__(self, other):
        return len(self.path) < len(other.path)

    def __eq__(self, other) -> bool:
        return hash(self) == hash(other)

    def __hash__(self) -> int:
        return hash("".join(sorted(self.path)))


@dataclass
class State:
    player: Player
    boss: Boss
    win: bool = None
    mana_spent: int = 0
    path: Path = Path()
    hard: bool = False

    def __lt__(self, other):
        return self.mana_spent < other.mana_spent

    def __hash__(self) -> int:
        return hash(self.path)

    def __call__(self, spell) -> Any:
        state = deepcopy(self)
        spell = deepcopy(spell)
        state.path.append(spell.name)
        if not state.take_turn("player", spell):
            return None
        if 0 in [state.player.health, state.player.mana]:
            state.win = False
            return None
        if state.boss.health <= 0:
            state.win = True
            return state
        state.take_turn("boss")
        if state.boss.health <= 0:
            state.win = True
            return state
        if state.win is False:
            return None
        return state

    def take_turn(self, who, spell=None):
        person = getattr(self, who)
        if who == "player" and self.hard:
            person.health -= 1
            if person.health <= 0:
                return None
        for p in (self.player, self.boss):
            for effect in p.effects:
                match effect:
                    case Harm(_, _, dmg):
                        dmg = max(dmg - p.armor, 1)
                        p.health -= dmg
                        p.health = max(p.health, 0)
                    case Heal(_, _, heal, arm, mana):
                        p.health += heal
                        p.mana += mana
                        if p.armor == 0:
                            p.armor += arm
                effect.dur -= 1
                if effect.dur <= 0:
                    if effect.name == "Shield":
                        p.armor = 0
                    p.effects.remove(effect)
        if person.health <= 0:
            return True

        if who == "boss":
            dmg = max(person.dmg - self.player.armor, 1)
            self.player.health -= dmg
            self.player.health = max(self.player.health, 0)

        if spell:
            if spell in [*self.player.effects, *self.boss.effects]:
                return None
            if person.mana < spell.cost:
                return None
            person.mana -= spell.cost
            self.mana_spent += spell.cost
            for effect in spell.effects:
                match effect:
                    case Harm(_, dur, dmg):
                        if dur == 1:
                            self.boss.health -= dmg
                        else:
                            self.boss.effects.append(effect)
                    case Heal():
                        self.player.effects.append(effect)
        return True


def get_data(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return f.read()


def parse(data):
    return tuple(int(d[-1]) for line in data.splitlines() if (d := line.split()))


def search(start, spells):
    queue = [(0, start)]
    seen = set()
    count = 0
    while queue:
        count += 1
        _, current = heappop(queue)
        if current.win is True:
            return current
        seen.add(current.path)
        for spell in spells:
            if spell.cost > current.player.mana:
                continue
            new_state = current(spell)
            if not new_state or new_state.path in seen or new_state in queue:
                continue
            heappush(queue, (new_state.mana_spent + new_state.boss.health, new_state))
    return None


def main():
    data = get_data("day22.txt")
    b_hp, b_dmg = parse(data)
    boss = Boss(b_hp, dmg=b_dmg)
    player = Player()
    state_0 = State(player, boss)
    state_0_hard = State(player, boss, hard=True)

    p1 = search(state_0, sorted(spells))
    print(f"Part 1: {p1.mana_spent}")

    p2 = search(state_0_hard, sorted(spells))
    print(f"Part 2: {p2.mana_spent}")


if __name__ == "__main__":
    main()
