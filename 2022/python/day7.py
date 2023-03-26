#!/usr/bin/env python3.11

from dataclasses import dataclass
from enum import Enum

from rich import print


class Type(Enum):
    DIR = 1
    FILE = 2

    def __repr__(self) -> str:
        return self.name


@dataclass
class Node:
    name: str
    size: int
    ntype: Type

    def __post_init__(self) -> None:
        self.parent: Node = None


@dataclass
class Dir(Node):
    children: list[Node]


class FileSystem:
    def __init__(self):
        self.root = Dir(name="/", size=0, ntype=Type.DIR, children=[])
        self.current = self.root

    def move_up(self):
        self.current = self.current.parent
        return self.current

    def cd(self, name):
        for child in self.current.children:
            if child.name == name:
                self.current = child
                return self.current
        raise FileNotFoundError(f"Directory {name} not found")

    def add(self, node):
        self.current.children.append(node)
        node.parent = self.current
        if node.ntype == Type.FILE:
            self.add_parent_size(node, node.size)

    def add_parent_size(self, node, size):
        if node.parent:
            node.parent.size += size
            self.add_parent_size(node.parent, size)

    def __iter__(self):
        for child in self.root.children:
            yield child
            if child.ntype == Type.DIR:
                yield from self._iter_child(child)

    def _iter_child(self, node):
        for child in node.children:
            yield child
            if child.ntype == Type.DIR:
                yield from self._iter_child(child)


def get_data(filename):
    with open(filename) as f:
        yield from (line.strip() for line in f)


def main():
    fs = FileSystem()
    data = get_data("day7.txt")
    for d in data:
        match d.split():
            case ["$", "cd", ".."]:
                fs.move_up()
            case ["$", "cd", name]:
                if name == "/":
                    continue
                fs.cd(name)
            case ["$", "ls"]:
                continue
            case ["dir", name]:
                fs.add(Dir(name=name, size=0, ntype=Type.DIR, children=[]))
            case [size, name]:
                fs.add(Node(name=name, size=int(size), ntype=Type.FILE))
            case _:
                print(f"Missed {d}")

    PART1_LIMIT = 100_000
    part1 = sum(
        (dir.size for dir in filter(lambda x: (x.size <= PART1_LIMIT and x.ntype == Type.DIR), fs))
    )
    print(f"Part 1: {part1}")

    TOTAL_SIZE = 70_000_000
    INSTALL_SIZE = 30_000_000
    NEEDED_SPACE = INSTALL_SIZE - (TOTAL_SIZE - fs.root.size)

    part2 = next(dir.size for dir in sorted(fs, key=lambda x: x.size) if dir.size >= NEEDED_SPACE)
    print(f"Part 2: {part2}")


if __name__ == "__main__":
    main()
