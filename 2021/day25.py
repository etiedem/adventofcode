from copy import deepcopy
from dataclasses import dataclass, field

from rich import print
from rich.console import Console
from rich.style import Style


current_style = Style(color='deep_sky_blue1', bold=True)


@dataclass
class Current:
    grid: list[list]

    def step(self):

        temp = deepcopy(self.grid)
        max_x = len(self.grid[0])
        max_y = len(self.grid)

        for y, row in enumerate(temp):
            for x, item in enumerate(row):
                if item == '>' and temp[y][(x+1) % max_x] == '.':
                    self.grid[y][(x+1) % max_x] = '>'
                    self.grid[y][x] = '.'

        temp = deepcopy(self.grid)
        for y, row in enumerate(temp):
            for x, item in enumerate(row):
                if item == 'v' and temp[(y+1) % max_y][x] == '.':
                    self.grid[(y+1) % max_y][x] = 'v'
                    self.grid[y][x] = '.'

    def steps(self, s):
        for _ in range(s):
            self.step()

    def find_stopping(self):
        count = 1
        while True:
            temp = deepcopy(self.grid)
            self.step()
            if temp == self.grid:
                break
            count += 1
        return count

    def show(self):
        console = Console()
        for row in self.grid:
            for item in row:
                if item in ('>', 'v'):
                    console.print(f'{item:>2s}', style=current_style, end='')
                else:
                    console.print(f'{item:>2s}', end='')
            print()


def get_data(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        return [list(x) for x in f.read().splitlines()]


def main():
    data = get_data('day25.txt')
    current = Current(data)
    print(current.find_stopping())


if __name__ == "__main__":
    main()
