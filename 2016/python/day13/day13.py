#!/usr/bin/env python3.11

from heapq import heappop, heappush

import numpy as np
from rich import print


class Maze(np.ndarray):
    def __new__(cls, num, xlen, ylen):
        grid = super().__new__(cls, shape=(ylen, xlen), dtype=int)
        for idx, _ in np.ndenumerate(grid):
            find = idx[1] * idx[1] + 3 * idx[1] + 2 * idx[1] * idx[0] + idx[0] + idx[0] * idx[0]
            find += num
            grid[idx] = 0 if bin(find).count("1") % 2 == 0 else 1
        return grid

    def show(self, path=None):
        row = 0
        for idx, item in np.ndenumerate(self):
            if idx[0] != row:
                print()
                row = idx[0]
            if path and idx in path:
                print("0", end="")
                continue
            match item:
                case 0:
                    print(".", end="")
                case 1:
                    print("#", end="")
                case _:
                    raise ValueError
        print()

    def get_nei(self, pos):
        directions = ((-1, 0), (0, 1), (1, 0), (0, -1))
        for dir in directions:
            dy = pos[0] + dir[0]
            dx = pos[1] + dir[1]
            if not 0 <= dx < self.shape[1]:
                continue
            if not 0 <= dy < self.shape[0]:
                continue
            if self[dy, dx] == 0:
                yield (dy, dx)

    def get_path(self, start, end, path):
        output = [end]
        cur = end
        while cur != start:
            output.append(path[cur])
            cur = path[cur]
        output.reverse()
        return output, len(output) - 1

    def find_sp(self, start, end):
        nx, ny = end
        finish = (ny, nx)
        queue = [(0, start)]
        prev = {}
        dist = {start: 0}
        finished = False
        while queue:
            _, current = heappop(queue)
            if current == finish:
                finished = True
            for neighbor in self.get_nei(current):
                alt = dist[current] + 1
                if alt < dist.get(neighbor, np.inf):
                    dist[neighbor] = alt
                    prev[neighbor] = current
                    heappush(queue, (alt, neighbor))

        if finished:
            path, length = self.get_path(start, finish, prev)
            return path, length, dist

        return [], -1, dist


def get_data(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return f.read()


def main():
    data = get_data("day13.txt")
    maze = Maze(int(data), 60, 60)
    path, length, dist = maze.find_sp((1, 1), (31, 39))

    print(f"Part 1: {length}")

    p2 = len({k for k, v in dist.items() if v <= 50})
    print(f"Part 2: {p2}")


if __name__ == "__main__":
    main()
