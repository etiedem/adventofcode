from dataclasses import dataclass, field
from functools import reduce

from rich import print


@dataclass
class Node:
    x: int
    y: int
    value: int


@dataclass(slots=True)
class Basin:
    base: Node
    basin: list[Node] = field(default_factory=list)

    def __lt__(self, other):
        return len(self.basin) < len(other.basin)

    def _inside(self, x, y):
        return any(node.x == x and node.y == y for node in self.basin)

    def _fill(self, x, y, data):
        if data[y][x] == 9 or self._inside(x, y):
            return

        self.basin.append(Node(x, y, data[y][x]))
        self._fill(x, y + 1, data) if y + 1 < len(data) else None
        self._fill(x, y - 1, data) if y > 0 else None
        self._fill(x + 1, y, data) if x + 1 < len(data[0]) else None
        self._fill(x - 1, y, data) if x > 0 else None

    def fill(self, data):
        self._fill(self.base.x, self.base.y, data)

    def show(self):
        x1 = min(node.x for node in self.basin)
        x2 = max(node.x for node in self.basin)
        y1 = min(node.y for node in self.basin)
        y2 = max(node.y for node in self.basin)

        grid = [[9] * ((x2-x1) + 1) for _ in range((y2-y1) + 1)]
        for node in self.basin:
            grid[node.y - y1][node.x - x1] = node.value

        for line in grid:
            for item in line:
                print(f'{str(item) if item != 9 else "":>2s}', end=' ')
            print()
        print(f'({x1}, {y1}):({x2}, {y2})')


def get_data(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        return [[int(x)
                 for x in item]
                for line in f.readlines()
                for item in line.split()]


def get_around(data, x, y):
    if x < len(data[0]) - 1:
        yield data[y][x + 1]
    if x > 0:
        yield data[y][x - 1]
    if y < len(data) - 1:
        yield data[y + 1][x]
    if y > 0:
        yield data[y - 1][x]


def main():
    data = get_data('day9.txt')
    result = []
    for y, row in enumerate(data):
        for x, item in enumerate(row):
            if all(item < x for x in get_around(data, x, y)):
                basin = Basin(Node(x, y, data[y][x]))
                basin.fill(data)
                result.append(basin)

    largest = sorted(result, reverse=True)[:3]
    answer = reduce(lambda x, y: x * len(y.basin), largest, 1)
    print(answer)


if __name__ == "__main__":
    main()
