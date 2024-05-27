from dataclasses import dataclass, field

from rich import print


@dataclass
class Octopus:
    matrix: list = field(default_factory=list)
    pulses: int = 0
    syncho: bool = False
    _max_x: int = field(init=False)
    _max_y: int = field(init=False)

    def __post_init__(self):
        self._max_x = len(self.matrix[0]) - 1
        self._max_y = len(self.matrix) - 1

    def _get_around(self, x, y):
        if y > 0:
            self.matrix[y - 1][x] += 1
        if y < self._max_y:
            self.matrix[y + 1][x] += 1
        if x > 0:
            self.matrix[y][x - 1] += 1
            if y > 0:
                self.matrix[y - 1][x - 1] += 1
            if y < self._max_y:
                self.matrix[y + 1][x - 1] += 1
        if x < self._max_x:
            self.matrix[y][x + 1] += 1
            if y > 0:
                self.matrix[y - 1][x + 1] += 1
            if y < self._max_y:
                self.matrix[y + 1][x + 1] += 1

    def _pulse(self, pulsed=None):
        pulsed = set() if pulsed is None else pulsed

        while True:
            FLAG = 0
            for y, row in enumerate(self.matrix):
                for x, item in enumerate(row):
                    if item >= 10 and (x, y) not in pulsed:
                        FLAG = 1
                        pulsed.add((x, y))
                        self._get_around(x, y)
            if not FLAG:
                break

    def step(self):
        self.syncho = False
        for y, row in enumerate(self.matrix):
            for x, item in enumerate(row):
                self.matrix[y][x] += 1

        self._pulse()

        count = 0
        for y, row in enumerate(self.matrix):
            for x, item in enumerate(row):
                if item >= 10:
                    count += 1
                    self.pulses += 1
                    self.matrix[y][x] = 0

        if count == (self._max_x + 1) * (self._max_y + 1):
            self.syncho = True

    def steps(self, steps):
        for _ in range(steps):
            self.step()

    def show(self):
        for line in self.matrix:
            for item in line:
                print(f'{str(item):>2s}', end=' ')
            print()


def get_data(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        return [[int(x) for x in line.strip()] for line in f.readlines()]


def main():
    data = get_data('day11.txt')
    oct = Octopus(data)
    count = 0
    while True:
        oct.step()
        count += 1
        if oct.syncho:
            break
    print(count)
    # oct.steps(100)
    # print(oct)


if __name__ == "__main__":
    main()
