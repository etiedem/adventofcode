#!/usr/bin/env python3.11

from enum import Enum
from hashlib import md5
from heapq import heappop, heappush

import numpy as np
from more_itertools import flatten
from rich import print

Item = Enum("Item", ["OPEN", "WALL", "DOOR", "START", "END"])


class Maze(np.ndarray):
    def __new__(cls, data, hash):
        tmp = [list(d) for d in data.splitlines()]
        ylen = len(tmp)
        xlen = len(tmp[0])

        grid = super().__new__(cls, shape=(ylen, xlen), dtype=int)
        grid.hash = hash
        for (idx, _), item in zip(np.ndenumerate(grid), flatten(tmp), strict=True):
            match item:
                case " ":
                    grid[idx] = Item.OPEN.value
                case "#":
                    grid[idx] = Item.WALL.value
                case "|" | "-":
                    grid[idx] = Item.DOOR.value
                case "S":
                    grid[idx] = Item.START.value
                    grid.start = idx
                case "V":
                    grid[idx] = Item.END.value
                    grid.end = idx

        return grid

    def get_neigh(self, idx, path):
        cur_path = f"{self.hash}{path}"
        chash = md5(cur_path.encode()).hexdigest()[:4]
        direction = (((0, 0), (-1, -2)), ((1, 2), (0, 0)), ((0, 0), (1, 2)), ((-1, -2), (0, 0)))
        for dir in direction:
            # UP
            if dir[0][0] == -1 and chash[0] not in ("b", "c", "d", "e", "f"):
                continue
            # DOWN
            elif dir[0][0] == 1 and chash[1] not in ("b", "c", "d", "e", "f"):
                continue
            # LEFT
            elif dir[1][0] == -1 and chash[2] not in ("b", "c", "d", "e", "f"):
                continue
            # RIGHT
            elif dir[1][0] == 1 and chash[3] not in ("b", "c", "d", "e", "f"):
                continue

            dy = idx[0] + dir[0][0]
            dx = idx[1] + dir[1][0]

            ny = idx[0] + dir[0][1]
            nx = idx[1] + dir[1][1]

            if not 0 <= ny <= self.shape[0]:
                continue
            if not 0 <= nx <= self.shape[1]:
                continue

            direction = None
            if dir[0][0] < 0:
                direction = "U"
            elif dir[0][0] > 0:
                direction = "D"
            elif dir[1][0] < 0:
                direction = "L"
            elif dir[1][0] > 0:
                direction = "R"

            if self[dy, dx] != Item.WALL.value:
                yield direction, (ny, nx)


class State:
    def __init__(self, pos, path):
        self.pos = pos
        self.path = path
        self.pathlen = len(path)

    def __lt__(self, other):
        return self.pathlen < other.pathlen


def solve_shortest(maze_raw, data):
    maze = Maze(maze_raw, data)
    start = State(maze.start, "")
    queue = [(0, start)]
    while queue:
        _, current = heappop(queue)
        if current.pos == maze.end:
            return current
        for dir, nei in maze.get_neigh(current.pos, current.path):
            candidate = State(nei, current.path + dir)
            heappush(queue, (candidate.pathlen, candidate))

    return None


def solve_longest(maze_raw, data):
    maze = Maze(maze_raw, data)
    start = State(maze.start, "")
    queue = [(0, start)]
    path_lengths = set()
    while queue:
        _, current = heappop(queue)
        if current.pos == maze.end:
            path_lengths.add(current.pathlen)
            continue
        for dir, nei in maze.get_neigh(current.pos, current.path):
            candidate = State(nei, current.path + dir)
            heappush(queue, (candidate.pathlen, candidate))

    return sorted(path_lengths)[-1]


def get_data(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return f.read()


def main():
    data = get_data("day17.txt")
    maze = get_data("maze.txt")

    p1 = solve_shortest(maze, data).path
    print(f"Part 1: {p1}")

    p2 = solve_longest(maze, data)
    print(f"Part 2: {p2}")


if __name__ == "__main__":
    main()
