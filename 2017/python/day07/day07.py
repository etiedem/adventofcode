#!/usr/bin/env python3.11

import re
from collections import Counter
from dataclasses import dataclass, field
from typing import Optional

from more_itertools import minmax
from rich import print


@dataclass
class Node:
    name: str
    weight: int
    t_weight: int = 0
    parent: Optional["Node"] = None
    children: list["Node"] = field(default_factory=list)
    __RE_PARSE = re.compile(r"(?P<name>\w+)\s\((?P<weight>\d+)\)")

    def __hash__(self):
        return hash(f"{self.name}{self.weight}")

    def __rich_repr__(self):
        yield self.name
        yield "weight", self.weight
        yield "t_weight", self.t_weight
        yield "parent", self.parent.name
        yield "children", self.children

    def __iter__(self):
        yield from self.post_order()

    @classmethod
    def from_str(cls, data: str):
        m = Node.__RE_PARSE.match(data)
        return Node(m["name"], int(m["weight"]))

    def post_order(self):
        for child in self.children:
            yield from child.post_order()
        yield self

    def find_node(self, target: str):
        for node in self.post_order():
            if node.name == target:
                return node
        return None

    def find_imbalance(self):
        for node in self.post_order():
            if node.children:
                base = node.children[0].t_weight
                if any(base != child.t_weight for child in node.children):
                    count = Counter(child.t_weight for child in node.children).most_common()
                    low, high = minmax(c[0] for c in count)
                    diff = high - low
                    for child in node.children:
                        if child.t_weight == count[-1][0]:
                            return child.weight - diff
        return None


def create_tree(data):
    RE_TREE = re.compile(r"(?P<name>\w+)\s.*-> (?P<children>.*)")
    nodes = {}
    head = []
    for line in data.splitlines():
        node = Node.from_str(line)
        nodes[node.name] = node
        head.append(node.name)

    for line in data.splitlines():
        if m := RE_TREE.search(line):
            node = nodes[m["name"]]
            for child in m["children"].split(", "):
                nodes[child].parent = node
                node.children.append(nodes[child])
                head.remove(child)

    head = nodes[head[0]]
    for node in head:
        if node.t_weight != 0:
            continue
        node.t_weight = node.weight
        for c in node.children:
            node.t_weight += c.t_weight if c.children else c.weight

    return head


def get_data(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return f.read()


def main():
    data = get_data("day07.txt")
    tree = create_tree(data)

    p1 = tree.name
    print(f"Part 1: {p1}")

    p2 = tree.find_imbalance()
    print(f"Part 2: {p2}")


if __name__ == "__main__":
    main()
