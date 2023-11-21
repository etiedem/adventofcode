#!/usr/bin/env python3.11

from dataclasses import dataclass, field

from rich import print


@dataclass
class Layer:
    depth: int
    pos: int = 0
    direction: str = "down"

    def step(self):
        match self.direction:
            case "down":
                self.pos += 1
                if self.pos == self.depth - 1:
                    self.direction = "up"
            case "up":
                self.pos -= 1
                if self.pos == 0:
                    self.direction = "down"


class Search:
    def __init__(self, game):
        self.delay = 0
        self.skip = []
        for idx, layer in enumerate(game.layers):
            if not layer:
                continue
            self.skip.append((idx, 2 * (layer.depth - 1)))

    def _check(self):
        for idx, num in self.skip:
            if (self.delay + idx) % num == 0:
                return True
        return False

    def __iter__(self):
        while True:
            self.delay += 1
            while self._check():
                self.delay += 1
            yield self.delay


@dataclass
class Game:
    layers: list
    player: int = -1
    severity: int = 0
    caught: bool = False

    def run(self, part2=False):
        while self.player != len(self.layers):
            if part2 and self.caught:
                return
            self.step(part2)

    def reset(self):
        self.player = -1
        self.severity = 0
        self.caught = False
        for layer in self.layers:
            if not layer:
                continue
            layer.pos = 0
            layer.direction = "down"

    def step(self, part2=False):
        self.player += 1
        if self.player >= len(self.layers):
            return self
        if (p_layer := self.layers[self.player]) and p_layer.pos == 0:
            self.caught = True
            if part2:
                return None
            self.severity += self.player * p_layer.depth
        for layer in self.layers:
            if not layer:
                continue
            layer.step()
        return None

    def delay(self, num: int = 1):
        for _ in range(num):
            for layer in self.layers:
                if not layer:
                    continue
                layer.step()

    @classmethod
    def from_str(cls, data: str):
        layers = []
        prev = -1
        for line in data.splitlines():
            pos, depth = map(int, line.split(": "))
            while prev + 1 != pos:
                prev += 1
                layers.append(None)

            prev += 1
            layers.append(Layer(depth))
        return Game(layers)


def get_data(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return f.read()


def find_delay(game: Game) -> int:
    search = Search(game)
    for delay in search:
        game.reset()
        game.delay(delay)
        game.run(True)
        if not game.caught:
            return delay


def main():
    data = get_data("day13.txt")
    game = Game.from_str(data)
    game.run()
    print(f"Part 1: {game.severity}")

    p2 = find_delay(game)
    print(f"Part 2: {p2}")


if __name__ == "__main__":
    main()
