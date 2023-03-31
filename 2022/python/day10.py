#!/usr/bin/env python3.11

from dataclasses import dataclass

from rich import print


@dataclass
class Command:
    num: int
    cycles: int


def parse_instr(instr):
    match instr.split():
        case ["addx", x]:
            return Command(int(x), 2)
        case ["noop"]:
            return Command(0, 1)
        case _:
            raise ValueError(f"Unknown instruction: {instr}")


def run(instrs):
    x_reg = 1
    cycle = 0
    get = 20
    signal = []
    crt = []
    for instr in instrs:
        for _ in range(instr.cycles):
            c = cycle % 40
            if x_reg in [c - 1, c, c + 1]:
                crt.append(1)
            else:
                crt.append(0)
            cycle += 1
            if cycle == get:
                get += 40
                signal.append(x_reg * cycle)
        x_reg += instr.num
    cycle += 1
    return signal, crt


def get_data(filename):
    with open(filename) as f:
        yield from f.read().splitlines()


def show_crt(crt):
    for i in range(0, len(crt), 40):
        print("".join("#" if x else " " for x in crt[i : i + 40]))


def main():
    instr = map(parse_instr, get_data("day10.txt"))
    signal, crt = run(instr)
    print(f"Part 1: {sum(signal)}")
    print("Part 2: ")
    show_crt(crt)


if __name__ == "__main__":
    main()
