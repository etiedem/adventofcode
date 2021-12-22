from dataclasses import dataclass

from rich import print


@dataclass(slots=True)
class Paper:
    points: set

    def _fold(self, fold):
        result = set()

        for x, y in self.points:
            if fold[0] == 'y' and int(fold[1]) < y:
                result.add((x, int(fold[1]) * 2 - y))
            elif fold[0] == 'x' and int(fold[1]) < x:
                result.add((int(fold[1]) * 2 - x, y))
            else:
                result.add((x, y))

        self.points = result

    def folds(self, folds):
        for f in folds:
            self._fold(f)

    def show(self):
        x1 = min(point[0] for point in self.points)
        x2 = max(point[0] for point in self.points)
        y1 = min(point[1] for point in self.points)
        y2 = max(point[1] for point in self.points)

        grid = [['.'] * ((x2-x1) + 1) for _ in range((y2-y1) + 1)]
        for point in self.points:
            grid[point[1] - y1][point[0] - x1] = '#'

        for line in grid:
            for item in line:
                print(f'{item if item != "." else "":>2s}', end=' ')
            print()
        print(f'({x1}, {y1}):({x2}, {y2})')


def get_data(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        tmp = [sec.splitlines() for sec in f.read().split('\n\n')]
        return [[[int(y) for y in x.split(',')] for x in tmp[0]],
                [x.split()[-1].split('=') for x in tmp[1]]]


def main():
    data, folds = get_data('day13.txt')
    dots = Paper({(x, y) for x, y in data})
    dots.folds(folds)
    dots.show()


if __name__ == "__main__":
    main()
