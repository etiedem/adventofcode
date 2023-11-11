#!/usr/bin/env python3.11

from dataclasses import dataclass, field
from typing import Optional

from rich import print


@dataclass
class Node:
    data: list = field(default_factory=list)
    depth: int = 1
    parent: Optional["Node"] = None
    children: list["Node"] = field(default_factory=list)

    def __iter__(self):
        for child in self.children:
            yield from child
        yield self


@dataclass
class Tree:
    root: Node

    def __iter__(self):
        yield from self.root

    def count_garbage(self):
        return sum(len(x.data) for x in self)

    def get_score(self):
        return sum(x.depth for x in self)

    @classmethod
    def from_str(cls, data: str):
        if data[0] != "{":
            raise ValueError("Input doesn't start with a Node")

        tree = Tree(Node())
        cur = tree.root
        idx = 1
        GARBAGE = False

        while idx < len(data):
            if data[idx] == "!":
                idx += 1
            elif data[idx] == ">":
                GARBAGE = False
            elif GARBAGE:
                cur.data.append(data[idx])
            elif data[idx] == "{":
                new = Node(parent=cur, depth=cur.depth + 1)
                cur.children.append(new)
                cur = new
            elif data[idx] == "}":
                cur = cur.parent
            elif data[idx] in (",", " "):
                pass
            elif data[idx] == "<":
                GARBAGE = True

            idx += 1

        return tree


def get_data(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return f.read()


def main():
    data = get_data("day09.txt")
    tree = Tree.from_str(data)

    p1 = tree.get_score()
    print(f"Part 1: {p1}")

    p2 = tree.count_garbage()
    print(f"Part 2: {p2}")


if __name__ == "__main__":
    main()
