#!/usr/bin/env python3.12

from dataclasses import dataclass, field
from heapq import heappop, heappush

import numpy as np
from icecream import ic
from pygments import style
from rich.console import Console


@dataclass
class Map:
    map: np.ndarray
    max_x: int
    max_y: int

    def get_neighbor(self, y, x):
        direction = ((1, 0), (0, 1), (-1, 0), (0, -1))
        for d in direction:
            nx = x + d[0]
            ny = y + d[1]
            if 0 <= nx < self.max_x and 0 <= ny < self.max_y:
                yield ny, nx

    def show(self, path=None):
        row = 0
        console = Console()
        for (y, x), item in np.ndenumerate(self.map):
            if y != row:
                print()
                row = y
            if path and (y, x) in path:
                console.print(f"[red on white]{item}[/red on white]", end="")
            else:
                console.print(item, end="")
        print()


def create_map(data) -> Map:
    data = data.splitlines()
    map = np.ndarray(shape=(len(data), len(data[0])), dtype="uint8")
    for y, row in enumerate(data):
        for x, item in enumerate(row):
            map[y, x] = item
    return Map(map, len(data[0]), len(data))


def get_data(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return f.read()


def get_3_prev(prev, start):
    result = [start]
    if not (ans := prev.get(result[-1])):
        result.append((-1, -2))
    else:
        result.append(ans)

    if not (ans := prev.get(result[-1])):
        result.append((-2, -3))
    else:
        result.append(ans)

    if not (ans := prev.get(result[-1])):
        result.append((-3, -4))
    else:
        result.append(ans)

    if not (ans := prev.get(result[-1])):
        result.append((-3, -4))
    else:
        result.append(ans)

    return result


def the_same(items):
    first = items[0]
    ysame = True
    xsame = True
    for i in items[1:]:
        if i[0] != first[0]:
            ysame = False
    for i in items[1:]:
        if i[1] != first[1]:
            xsame = False
    return ysame or xsame


def shortest_path(map: Map):
    end = (map.max_y - 1, map.max_x - 1)
    queue = [(0, (0, 0))]
    seen = set()
    prev = {(0, 0): None}
    dist = {(0, 0): 0}

    while queue:
        _, current = heappop(queue)

        if current == end:
            break

        if current in seen:
            continue
        seen.add(current)

        for nei in map.get_neighbor(*current):
            alt = dist[current] + map.map[*nei]
            if alt < dist.get(nei, float("inf")):
                tmp = prev.get(nei)
                prev[nei] = current
                if the_same(get_3_prev(prev, nei)):
                    prev[nei] = tmp
                    continue
                dist[nei] = alt
                heappush(queue, (alt, nei))

    return dist, prev, end


def build_path(prev, end):
    path = [end]
    current = prev.get(end)
    while current:
        path.append(current)
        current = prev.get(current)
    return path


def main():
    # data = get_data("test.txt")
    data = get_data("example.txt")
    # data = get_data("day17.txt")
    map = create_map(data)
    dist, prev, end = shortest_path(map)
    path = build_path(prev, end)
    map.show(path)
    ic(dist[end])

    # p1 = part1(data)
    # print(f"Part 1: {p1}")

    # p2 = part2(data)
    # print(f"Part 2: {p2}")


if __name__ == "__main__":
    main()
