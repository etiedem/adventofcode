from dataclasses import dataclass, field

import pygame as pg
from pygame.locals import *

WHITE = (255, 255, 255)


@dataclass
class Board:
    grid: list[list] = field(init=False)
    size: int

    def __post_init__(self):
        self.grid = [['#'] * self.size for _ in range(self.size)]

    def show(self, screen):
        swidth, sheight = screen.get_size()
        for y in range(0, sheight, sheight // len(self.grid)):
            for x in range(0, swidth, swidth // len(self.grid[0])):
                rect = pg.Rect(x, y, sheight // len(self.grid),
                               swidth // len(self.grid[0]))
                pg.draw.rect(screen, WHITE, rect, 1)


def main():

    pg.init()
    screen = pg.display.set_mode((400, 400))
    pg.display.set_caption("Testing 1")

    background = pg.Surface(screen.get_size())
    background = background.convert()
    background.fill((50, 50, 70))

    screen.blit(background, (0, 0))
    pg.display.flip()

    clock = pg.time.Clock()

    board = Board(20)

    running = True
    while running:
        clock.tick(60)
        board.show(screen)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

        pg.display.update()


if __name__ == "__main__":
    main()
