#!/usr/bin/env python3.11

from dataclasses import dataclass, field

from rich import print


@dataclass
class Disk:
    cur_pos: int
    max_pos: int

    @classmethod
    def from_str(cls, data: str):
        m, _, c = data.split(" ")[3::4]
        return Disk(int(c[:-1]), int(m))


@dataclass
class Game:
    disks: list[Disk] = field(default_factory=list)
    time: int = 0
    increment: int = 0

    def _tick(self, step=1):
        self.time += step
        for d in self.disks:
            d.cur_pos = (d.cur_pos + step) % d.max_pos

    def set_zero(self):
        first = self.disks[0]
        self.increment = first.max_pos
        steps = first.max_pos - first.cur_pos
        self._tick(steps - 1)

    def tick(self):
        self._tick(self.increment)

    @classmethod
    def from_str(cls, data: str):
        return Game([Disk.from_str(x) for x in data.splitlines()])


def find_answer(game):
    game.set_zero()
    while True:
        if all((disk.cur_pos + idx) % disk.max_pos == 0 for idx, disk in enumerate(game.disks, 1)):
            return game

        game.tick()


def get_data(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return f.read()


def main():
    data = get_data("day15.txt")

    game = Game.from_str(data)
    p1 = find_answer(game)
    print(f"Part 1: {p1.time}")

    game = Game.from_str(data)
    game.disks.append(Disk(0, 11))
    p2 = find_answer(game)
    print(f"Part 2: {p2.time}")


if __name__ == "__main__":
    main()
