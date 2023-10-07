#!/usr/bin/env python3.11

import itertools

from rich import print


class InstrSet:
    def __init__(self, instructions, data):
        self.instructions = instructions
        self.base = list(data)

    def __repr__(self) -> str:
        return f"{__class__.__name__}: {''.join(self.base)}"

    def scramble(self):
        for instr in self.instructions.splitlines():
            i = instr.split(" ")
            match " ".join(i[:2]):
                case "swap position":
                    x, y = map(int, i[2::3])
                    self.swap_pos(x, y)
                case "swap letter":
                    x, y = i[2::3]
                    self.swap_letter(x, y)
                case "reverse positions":
                    x, y = map(int, i[2::2])
                    self.reverse_pos(x, y)
                case "move position":
                    x, y = map(int, i[2::3])
                    self.move_pos(x, y)
                case "rotate left":
                    self.rotate_left(int(i[2]))
                case "rotate right":
                    self.rotate_right(int(i[2]))
                case "rotate based":
                    self.rotate_based(i[-1])
                case _:
                    raise ValueError("Unmatched case: %s" % " ".join(i[:2]))
        return "".join(self.base)

    def reverse_pos(self, x, y):
        tmp = self.base[x : y + 1]
        tmp.reverse()
        self.base[x : y + 1] = tmp
        return self

    def swap_pos(self, x, y):
        self.base[x], self.base[y] = self.base[y], self.base[x]
        return self

    def swap_letter(self, x, y):
        for idx, l in enumerate(self.base):
            if l == x:
                self.base[idx] = y
            elif l == y:
                self.base[idx] = x
        return self

    def move_pos(self, x, y):
        tmp = self.base.pop(x)
        self.base.insert(y, tmp)
        return self

    def rotate_left(self, x):
        length = len(self.base)
        tmp = [None] * length
        for idx, l in enumerate(self.base):
            tmp[(idx - x) % length] = l
        self.base = tmp
        return self

    def rotate_right(self, x):
        length = len(self.base)
        tmp = [None] * length
        for idx, l in enumerate(self.base):
            tmp[(idx + x) % length] = l
        self.base = tmp
        return self

    def rotate_based(self, x):
        length = self.base.index(x)
        if length >= 4:
            length += 1
        length += 1
        return self.rotate_right(length)


def get_data(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return f.read()


def part2(instr, data):
    for item in itertools.permutations(data):
        i = InstrSet(instr, item)
        tmp = i.scramble()
        if tmp == "fbgdceah":
            return "".join(item)


def main():
    data = get_data("day21.txt")

    instr = InstrSet(data, "abcdefgh")
    p1 = instr.scramble()
    print(f"Part 1: {p1}")

    p2 = part2(data, "abcdefgh")
    print(f"Part 2: {p2}")


if __name__ == "__main__":
    main()
