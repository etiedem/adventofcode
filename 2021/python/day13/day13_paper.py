from dataclasses import dataclass, field

from rich import print


@dataclass(slots=True)
class Paper:
    x_min: int
    x_max: int
    y_min: int
    y_max: int
    grid: list = field(default_factory=list)

    def __post_init__(self):
        self.grid = [['.'] * ((self.x_max - self.x_min) + 1)
                     for _ in range((self.y_max - self.y_min) + 1)]

    @property
    def dots(self):
        count = 0
        for y in self.grid:
            for x in y:
                if x == '#':
                    count += 1
        return count

    def show(self):
        for line in self.grid:
            for item in line:
                print(f'{item if item != "." else "":>2s}', end=' ')
            print()

    def load(self, data):
        for x, y in data:
            self.grid[y - self.y_min][x - self.x_min] = '#'

    def fold(self, axis, pos):
        if axis == 'y':
            grid = [['.'] * ((self.x_max - self.x_min) + 1)
                    for _ in range(self.y_max - self.y_min - int(pos))]
            for x in range((self.x_max - self.x_min) + 1):
                for y1, y2 in zip(
                    range(self.y_max - self.y_min - int(pos)),
                    range(
                        self.y_max - self.y_min, self.y_max - self.y_min - int(pos), -1
                    )
                ):
                    if self.grid[y1][x] == '#' or self.grid[y2][x] == '#':
                        grid[y1][x] = '#'
            self.grid = grid
            self.y_max = self.y_max - int(pos) - 1

        if axis == 'x':
            grid = [['.'] * ((self.x_max - self.x_min) - int(pos))
                    for _ in range((self.y_max - self.y_min) + 1)]
            for x1, x2 in zip(
                range(self.x_max - self.x_min - int(pos)),
                range(self.x_max - self.x_min, self.x_max - self.x_min - int(pos), -1)
            ):
                for y in range((self.y_max - self.y_min) + 1):
                    if self.grid[y][x1] == '#' or self.grid[y][x2] == '#':
                        grid[y][x1] = '#'
            self.grid = grid
            self.x_max = self.x_max - int(pos) - 1


def get_data(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        tmp = [sec.splitlines() for sec in f.read().split('\n\n')]
        return [[[int(y) for y in x.split(',')] for x in tmp[0]],
                [x.split()[-1].split('=') for x in tmp[1]]]


def get_limits(data):
    x_min = min(x[0] for x in data)
    x_max = max(x[0] for x in data)
    y_min = min(y[1] for y in data)
    y_max = max(y[1] for y in data)
    return x_min, x_max, y_min, y_max


def main():
    data, fold = get_data('day13.txt')
    paper = Paper(*get_limits(data))
    paper.load(data)
    # paper.fold(*fold[0])
    for f in fold:
        paper.fold(*f)
    paper.show()


if __name__ == "__main__":
    main()
