import dataclasses
from dataclasses import dataclass

from rich import print


def get_data(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        return [[list(map(int, y.split(',')))
                 for y in x.strip().split('->')]
                for x in f.readlines()]


@dataclass
class Point:
    x: int
    y: int


@dataclass
class Board:
    board: list[list[int]]

    @staticmethod
    def get_moves(p1: Point, p2: Point) -> list[Point]:
        result = [dataclasses.replace(p1)]
        np1, np2 = p1, p2

        while np1.x != np2.x or np1.y != np2.y:
            if np1.x < np2.x:
                np1.x += 1
            elif np1.x > np2.x:
                np1.x -= 1

            if np1.y < np2.y:
                np1.y += 1
            elif np1.y > np2.y:
                np1.y -= 1

            result.append(Point(np1.x, np1.y))

        return result

    def update(self, data):
        for p1, p2 in data:
            moves = self.get_moves(Point(*p1), Point(*p2))
            self.moves(moves)

    def moves(self, moves: list[Point]):
        for p in moves:
            try:
                self.board[p.x][p.y] += 1
            except IndexError:
                print(moves)

    @property
    def danger(self):
        count = 0
        for line in self.board:
            for num in line:
                if num > 1:
                    count += 1
        return count


def get_largest(data):
    x, y = 0, 0
    for line in data:
        for point in line:
            if point[0] > x:
                x = point[0]
            if point[1] > y:
                y = point[1]
    return x + 10, y + 10


def create_matrix(x, y):
    return [[0] * x for _ in range(y)]


def main():
    data = get_data('day5.txt')
    board = Board(create_matrix(*get_largest(data)))
    board.update(data)
    print(board.danger)


if __name__ == "__main__":
    main()
