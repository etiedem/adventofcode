import heapq
from collections import defaultdict
from copy import deepcopy
from dataclasses import dataclass, field
from typing import List

from rich import print
from rich.console import Console
from rich.text import Text


@dataclass
class Node:
    x: int
    y: int
    cost: int
    f: int = float('inf')

    def __lt__(self, other):
        return self.f < other.f

    def __hash__(self):
        return hash((self.x, self.y))


@dataclass
class Graph:
    _base: List[List[int]]
    graph: List[List[Node]] = field(default_factory=list)

    def __post_init__(self):
        self.graph = [[Node(x, y, cost)
                       for x, cost in enumerate(row)]
                      for y, row in enumerate(self._base)]
        self._base = []

    def get_neighbors(self, node: Node):
        return [
            self.graph[ny][nx]
            for x, y in ((1, 0), (0, 1), (-1, 0), (0, -1))
            if (nx := node.x + x) < len(self.graph[0]) and nx >= 0 and
            (ny := node.y + y) < len(self.graph) and ny >= 0
        ]

    def print(self, path=None):
        console = Console()

        path = [] if path is None else path
        for row in self.graph:
            for item in row:
                if item in path:
                    console.print(Text(f'{item.cost:>1d}', style='bold white'), end='')
                else:
                    console.print(
                        Text(f'{item.cost:>1d}', style='dark_turquoise'), end=''
                    )
            print()

    def expand(self, num):
        x_len = len(self.graph[0])
        y_len = len(self.graph)

        # Copy Original
        result = deepcopy(self.graph)

        # Expand X
        for n in range(num - 1):
            for y, row in enumerate(self.graph):
                result[y].extend([
                    Node(x + x_len * (n+1), y, ((item.cost + n) % 9) + 1)
                    for x, item in enumerate(row)
                ])

        self.graph = deepcopy(result)

        # Expand Y
        for n in range(num - 1):
            for y, row in enumerate(result):
                self.graph.append([
                    Node(x, y + y_len * (n+1), ((item.cost + n) % 9) + 1)
                    for x, item in enumerate(row)
                ])


def get_data(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        return [[int(l) for l in line.strip()] for line in f.readlines()]


def manhattan_distance(n1, n2):
    return abs(n1.x - n2.x) + abs(n1.y - n2.y)


def A_star(graph: Graph, source: Node, target: Node):
    open_set = [source]
    previous = {}
    g_score = defaultdict(lambda: float('inf'))
    g_score[source] = 0
    source.f = manhattan_distance(source, target)

    while open_set:
        current = heapq.heappop(open_set)

        if current == target:
            return g_score, previous

        for neighbor in graph.get_neighbors(current):
            alt = g_score[current] + neighbor.cost
            if alt < g_score[neighbor]:
                previous[neighbor] = current
                g_score[neighbor] = alt
                neighbor.f = alt + manhattan_distance(neighbor, target)
                if neighbor not in open_set:
                    heapq.heappush(open_set, neighbor)


def get_path(prev, source, target):
    path = []
    answer = 0
    if prev[target] is not None:
        while target and target != source:
            path.append(target)
            answer += target.cost
            target = prev[target]
    return path, answer


def main():
    data = get_data('day15.txt')
    graph = Graph(data)
    graph.expand(5)
    source = graph.graph[0][0]
    target = graph.graph[-1][-1]
    dist, prev = A_star(graph, source, target)
    path, answer = get_path(prev, source, target)
    # graph.print(path)
    print(answer)


if __name__ == "__main__":
    main()
