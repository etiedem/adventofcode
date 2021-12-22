from collections import defaultdict
from dataclasses import dataclass, field

from rich import print


@dataclass(slots=True)
class Path:
    path: list = field(default_factory=list)
    twice: bool = False


def get_data(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        return [[seg.strip() for seg in line.split(' - ')] for line in f.readlines()]


def create_graph(data):
    result = defaultdict(list)
    for d in data:
        if d[0] != 'end' and d[1] != 'start':
            result[d[0]].append(d[1])
        if d[1] != 'end' and d[0] != 'start':
            result[d[1]].append(d[0])
    return result


def traverse(graph, graphs, path=None):
    if path is None:
        path = Path()
        path.path.append('start')

    if path.path[-1] == 'end':
        graphs.append(path)
        return

    for s in graph.get(path.path[-1]):
        if (s.islower() and s in path.path) and path.twice is True:
            continue

        p = Path()
        p.path = path.path.copy()
        p.twice = path.twice

        if s.islower() and s in path.path:
            p.twice = True

        p.path.append(s)
        traverse(graph, graphs, p)


def main():
    data = get_data('day12.txt')
    graph = create_graph(data)
    graphs = []
    traverse(graph, graphs)
    print(len(graphs))


if __name__ == "__main__":
    main()
