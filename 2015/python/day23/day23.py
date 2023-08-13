#!/usr/bin/env python3.11

from collections import defaultdict

from rich import print


def get_data(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return f.read()


def parse(data):
    output = []
    for line in data.splitlines():
        instr, *rest = line.split()
        rest = [x.strip("+,") for x in rest]
        output.append((instr, *rest))
    return output


def solve(instr, part2=None):
    registers = defaultdict(int)
    if part2:
        registers["a"] = 1
    idx = 0
    while 0 <= idx < len(instr):
        match instr[idx][0]:
            case "hlf":
                registers[instr[idx][1]] //= 2
                idx += 1
            case "tpl":
                registers[instr[idx][1]] *= 3
                idx += 1
            case "inc":
                registers[instr[idx][1]] += 1
                idx += 1
            case "jmp":
                idx += int(instr[idx][1])
            case "jie":
                idx += int(instr[idx][2]) if registers[instr[idx][1]] % 2 == 0 else 1
            case "jio":
                idx += int(instr[idx][2]) if registers[instr[idx][1]] == 1 else 1
    return registers


def main():
    data = get_data("day23.txt")
    instructions = parse(data)

    p1 = solve(instructions)
    print(f"Part 1: {p1.get('b')}")

    p2 = solve(instructions, True)
    print(f"Part 2: {p2.get('b')}")


if __name__ == "__main__":
    main()
