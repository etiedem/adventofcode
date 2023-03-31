#!/usr/bin/env python3.11

import heapq

import numpy as np
from rich import print


class Maze:
    def __init__(self, data) -> None:
        grid = []
        for y, row in enumerate(data):
            tmp = []
            for x, item in enumerate(row):
                if item == "S":
                    self.start = (x, y)
                    tmp.append(0)
                elif item == "E":
                    self.end = (x, y)
                    tmp.append(25)
                else:
                    tmp.append(ord(item) - ord("a"))
            grid.append(tmp)
        self.grid = np.matrix(grid)

    def __iter__(self):
        for y in range(self.grid.shape[0]):
            for x in range(self.grid.shape[1]):
                yield x, y, self.grid[y, x]

    def _check_bounds(self, x: int, y: int) -> bool:
        if x < 0 or y < 0:
            return False
        try:
            self.grid[y, x]
        except IndexError:
            return False
        return True

    def get_neighbors(self, x, y):
        for dx, dy in [(x, y - 1), (x, y + 1), (x - 1, y), (x + 1, y)]:
            if self._check_bounds(dx, dy) and self.grid[dy, dx] <= self.grid[y, x] + 1:
                yield dx, dy

    def dijkstra(self, start):
        visited = set()
        previous = {}
        distances = {start: 0}
        queue = [(0, start)]
        while queue:
            current_distance, current_node = heapq.heappop(queue)
            if current_node in visited:
                continue
            visited.add(current_node)
            if current_node == self.end:
                break
            for neighbor in self.get_neighbors(*current_node):
                distance = current_distance + 1
                if neighbor not in distances or distance < distances[neighbor]:
                    distances[neighbor] = distance
                    previous[neighbor] = current_node
                    heapq.heappush(queue, (distance, neighbor))
        return previous

    def find_path(self, start, previous):
        current = self.end
        path = [current]
        while current != start:
            try:
                current = previous[current]
            except KeyError:
                return None
            path.append(current)
        return path[::-1]

    def show_path(self, path):
        for y in range(self.grid.shape[0]):
            for x in range(self.grid.shape[1]):
                if (x, y) in path:
                    print(f"[bold black on white]{self.grid[y, x]:^3d}[/]", end="")
                else:
                    print(f"{self.grid[y, x]:^3d}", end="")
            print()


def get_data(filename):
    with open(filename, "r", encoding="utf-8") as f:
        yield from f.read().splitlines()


def main():
    maze = Maze(get_data("day12.txt"))
    print(f"Part 1: {len(maze.find_path(maze.start, maze.dijkstra(maze.start))) - 1}")

    starts = ((start[0], start[1]) for start in maze if start[2] == 0)
    part2 = min(
        len(cur) - 1 for start in starts if (cur := maze.find_path(start, maze.dijkstra(start)))
    )
    print(f"Part 2: {part2}")


if __name__ == "__main__":
    main()
