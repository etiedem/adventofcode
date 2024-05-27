import ast
from dataclasses import dataclass, field
from typing import Generic, TypeVar

from rich import print


T = TypeVar('T')


@dataclass(slots=True)
class Node:
    left: Generic[T] = None
    right: Generic[T] = None
    parent: Generic[T] = None
    depth: int = 0


@dataclass(slots=True)
class BinaryTree:
    root: Node

    def print(self):

        def p(x):
            if not isinstance(x.left, Node):
                print(x.left)
            if not isinstance(x.right, Node):
                print(x.right)

        self.traverse(self.root, p)

    def max_depth(self, node=None):

        if node is None:
            node = self.root

        left_depth, right_depth = 0, 0
        if isinstance(node.left, Node):
            left_depth = self.max_depth(node.left)

        if isinstance(node.right, Node):
            right_depth = self.max_depth(node.right)

        if left_depth > right_depth:
            return left_depth + 1
        else:
            return right_depth + 1

    def explode(self, node):
        if isinstance(node.left, Node):
            self.explode(node.left)
        if isinstance(node.right, Node):
            self.explode(node.right)

        if node.depth > 3:
            print(node)
            # node.parent.left.right += node.left
            # node.parent.right += node.right

    # def explode_left(self, node):
    #     if node.parent

    def traverse(self, node, func):
        if isinstance(node.left, Node):
            self.traverse(node.left, func)
        if isinstance(node.right, Node):
            self.traverse(node.right, func)

        func(node)

    def add(self, node):

        def plus(x):
            x.depth += 1

        self.traverse(self.root, plus)
        root = Node(self.root)
        root.right = create_node(node, root)
        self.root.parent = root
        self.root = root


def create_node(data, parent):
    node = Node(parent=parent, depth=parent.depth + 1)

    node.left = create_node(data[0], node) if isinstance(data[0], list) else data[0]
    node.right = create_node(data[1], node) if isinstance(data[1], list) else data[1]

    return node


def get_data(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        return [ast.literal_eval(x.strip()) for x in f.readlines()]


def main():
    data = get_data('day18.txt')

    root = Node()
    tree = BinaryTree(root)

    root.left = create_node(data[0], root)
    root.right = create_node(data[1], root)

    tree.add(data[2])
    tree.add(data[1])

    print(tree)
    tree.print()


if __name__ == "__main__":
    main()
