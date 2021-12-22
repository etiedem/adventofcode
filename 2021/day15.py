import heapq
from collections import defaultdict
from dataclasses import dataclass, field

from rich import print


def get_data(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        return [[int(l) for l in line.strip()] for line in f.readlines()]


# class Node:

#     def __init__(self, x, y, cost):
#         self.x = x
#         self.y = y
#         self.cost = cost

#     def __lt__(self, other):
#         return self.cost < other.cost

#     def __eq__(self, other):
#         return (self.x, self.y) == (other.x, other.y)

#     def __hash__(self):
#         return hash(repr(self))

#     def __repr__(self):
#         return f'{self.__class__.__name__}(x={self.x}, y={self.y}, cost={self.cost})'

# @dataclass(eq=True)
# class Node:
#     x: int
#     y: int
#     cost: int
#     g: int = 1 << 20
#     f: int = 1 << 20
#     parent: int = None

#     def __lt__(self, other):
#         return self.f < other.f


def euclidean_distance(n1, n2):
    return abs(n1.x - n2.y) + abs(n1.y - n2.y)


def Dijkstra(graph, source, target):
    Q = [(0, source[1], source[2])]
    visited = set()
    cost = defaultdict(int)

    while Q:
        current = heapq.heappop(Q)
        if current in visited:
            continue
        visited.add(current)
        cost[(current[1], current[2])] = current[0]

        if (current[1], current[2]) == (target[1], target[2]):
            break

        for neighbor in get_neighbors(current, graph):
            heapq.heappush(Q, (neighbor[0] + current[0], neighbor[1], neighbor[2]))

    return cost[target[1], target[2]]


def get_neighbors(node, graph):
    return [
        graph[node[2] + dy][node[1] + dx]
        for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0))
        if node[1] + dx < len(graph[0]) and node[1] + dx >= 0 and node[2] +
        dy < len(graph) and node[2] + dy >= 0
    ]


def create_map(data):
    return [[(cost, x, y) for x, cost in enumerate(row)] for y, row in enumerate(data)]


def main():
    data = get_data('day15.txt')
    node_map = create_map(data)
    path = Dijkstra(node_map, node_map[0][0], node_map[9][9])
    print(path)


if __name__ == "__main__":
    main()
