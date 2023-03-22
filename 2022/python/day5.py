#!/usr/bin/env python3.11

from dataclasses import dataclass
from re import compile

STACK_RE = compile(r".(.).\s?")


@dataclass
class Instr:
    number: int
    src: int
    dest: int

    def __init__(self, data) -> None:
        items = data.split()
        self.number, self.src, self.dest = int(items[1]), int(items[3]), int(items[5])


@dataclass
class Stacks:
    length: int
    stacks: list[list[str]]

    def __init__(self, data: str) -> None:
        diagram = data.split("\n")
        self.length = int(diagram.pop().split()[-1])
        self.stacks = [[] for _ in range(self.length)]
        diagram.reverse()

        for stack in diagram:
            for idx, item in enumerate(STACK_RE.findall(stack)):
                if item != " ":
                    self.stacks[idx].append(item)

    def part1_move(self, instr: Instr) -> None:
        for _ in range(instr.number):
            tmp = self.stacks[instr.src - 1].pop()
            self.stacks[instr.dest - 1].append(tmp)

    def part2_move(self, instr: Instr) -> None:
        tmp = [self.stacks[instr.src - 1].pop() for _ in range(instr.number)]
        tmp.reverse()
        for item in tmp:
            self.stacks[instr.dest - 1].append(item)

    def get_top(self) -> str:
        return "".join(stack[-1] for stack in self.stacks)


def get_data(filename):
    with open(filename, "r", encoding="utf-8") as f:
        stacks, moves = f.read().split("\n\n")
        return stacks, moves.strip().split("\n")


def main():
    stacks, moves = get_data("day5.txt")
    part1_stacks = Stacks(stacks)
    part2_stacks = Stacks(stacks)
    for line in moves:
        part1_stacks.part1_move(Instr(line))
        part2_stacks.part2_move(Instr(line))

    print(f"Part 1: {part1_stacks.get_top()}")
    print(f"Part 2: {part2_stacks.get_top()}")


if __name__ == "__main__":
    main()
