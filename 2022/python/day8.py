#!/usr/bin/env python3.11

from rich import print


class Map:
    def __init__(self, data) -> None:
        self.grid = []
        self.grid.extend([int(char) for char in line.strip()] for line in data)

    def __iter__(self):
        for y, row in enumerate(self.grid):
            for x, item in enumerate(row):
                yield (x, y, item)

    def is_visible(self, x, y):
        cur = self.grid[y][x]
        if self.is_edge(x, y):
            return True
        if all(cur > i for i in self.get_up(x, y)):
            return True
        if all(cur > i for i in self.get_down(x, y)):
            return True
        if all(cur > i for i in self.get_left(x, y)):
            return True
        if all(cur > i for i in self.get_right(x, y)):
            return True

        return False

    def is_edge(self, x, y):
        if x in [0, len(self.grid[y]) - 1]:
            return True
        return y in [0, len(self.grid) - 1]

    def get_up(self, x, y):
        for i in range(y - 1, -1, -1):
            yield self.grid[i][x]

    def get_down(self, x, y):
        for i in range(y + 1, len(self.grid)):
            yield self.grid[i][x]

    def get_left(self, x, y):
        for i in range(x - 1, -1, -1):
            yield self.grid[y][i]

    def get_right(self, x, y):
        for i in range(x + 1, len(self.grid[y])):
            yield self.grid[y][i]

    def get_score(self, x, y):
        score = 1
        score *= self._score_helper(x, y, self.get_up)
        score *= self._score_helper(x, y, self.get_down)
        score *= self._score_helper(x, y, self.get_left)
        score *= self._score_helper(x, y, self.get_right)
        return score

    def _score_helper(self, x, y, func):
        score = 0
        for i in func(x, y):
            score += 1
            if i >= self.grid[y][x]:
                return score
        return score


def get_data(filename):
    with open(filename, "r", encoding="utf-8") as f:
        yield from f.readlines()


def main():
    my_map = Map(get_data("day8.txt"))

    part1 = sum(1 for x, y, _ in my_map if my_map.is_visible(x, y))
    print(f"Part 1: {part1}")

    part2 = max(my_map.get_score(x, y) for x, y, _ in my_map)
    print(f"Part 2: {part2}")


if __name__ == "__main__":
    main()
