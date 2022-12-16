from dataclasses import dataclass, field
from random import choice

import pygame as pg
from pygame.locals import *


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUEGREY = (50, 50, 70)


@dataclass
class Board:
    grid: list[list] = field(init=False)
    size: int

    def __post_init__(self):
        self.grid = [['#'] * self.size for _ in range(self.size)]

    def get_walls(self, x, y):
        positions = ((0, 1), (1, 0), (0, -1), (-1, 0))
        return [(px + x, py + y)
                for px, py in positions
                if 0 < px + x < (self.size - 1) and 0 < py +
                y < (self.size - 1) and self.grid[py + y][px + x] == '#']

    def num_visited(self, x, y):
        positions = ((0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, 1),
                     (-1, -1))
        return len([(px + x, py + y)
                    for px, py in positions
                    if 0 < px + x < (self.size - 1) and 0 < py +
                    y < (self.size - 1) and self.grid[py + y][px + x] == ''])

    def step(self):
        ex, ey = self.size - 1, self.size - 2
        cx, cy = 0, 1
        self.grid[ey][ex] = ''
        self.grid[ey][ex - 1] = ''
        walls = self.get_walls(cx, cy)
        visited = set()
        # visited = set((cx, cy))

        while walls:
            if self.num_visited(cx, cy) < 2:
                self.grid[cy][cx] = ''
                visited.add((cx, cy))
            cx, cy = choice(walls)
            if (cx, cy) == (ex - 1, ey):
                break
            walls.remove((cx, cy))
            walls.extend(self.get_walls(cx, cy))
            yield
            print(cx, cy)

    def display(self, screen):
        swidth, sheight = screen.get_size()
        for y, py in zip(self.grid, range(0, sheight, sheight // len(self.grid))):
            for x, px in zip(y, range(0, swidth, swidth // len(self.grid[0]))):
                rect = pg.Rect(
                    px, py, sheight // len(self.grid), swidth // len(self.grid[0])
                )
                if x == '#':
                    pg.draw.rect(screen, BLACK, rect)
                # else:
                #     pg.draw.rect(screen, WHITE, rect, 1)


def main():

    pg.init()
    screen = pg.display.set_mode((400, 400))
    pg.display.set_caption("Testing 1")

    background = pg.Surface(screen.get_size())
    background = background.convert()
    background.fill(BLUEGREY)

    screen.blit(background, (0, 0))
    pg.display.flip()

    clock = pg.time.Clock()

    board = Board(20)
    steps = board.step()

    running = True
    while running:
        # for _ in steps:
        screen.fill(BLUEGREY)
        clock.tick(60)
        try:
            next(steps)
        except StopIteration:
            pass
        board.display(screen)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
                print(board.grid)
        pg.display.update()


if __name__ == "__main__":
    main()
