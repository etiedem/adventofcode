#!/usr/bin/env python3.11

from rich import print


def get_data(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return f.read()


def parse_data(data: str) -> dict[int, list[int]]:
    output = {}
    for line in data.splitlines():
        base, other = line.split(" <-> ")
        connections = list(map(int, other.split(", ")))
        output[int(base)] = connections
    return output


def find_connections(graph: dict, start: int) -> int:
    if not (children := graph.get(start)):
        return None

    seen = {start}
    queue: list = children[:]
    while queue:
        cur = queue.pop()
        if cur in seen:
            continue
        seen.add(cur)
        queue.extend(graph.get(cur))
    return seen


def count_groups(graph: dict) -> int:
    groups = []

    for node in graph:
        if any(node in group for group in groups):
            continue
        group = find_connections(graph, node)
        groups.append(group)

    return len(groups)


def main():
    data = get_data("day12.txt")
    graph = parse_data(data)

    p1 = len(find_connections(graph, 0))
    print(f"Part 1: {p1}")

    p2 = count_groups(graph)
    print(f"Part 2: {p2}")


if __name__ == "__main__":
    main()
