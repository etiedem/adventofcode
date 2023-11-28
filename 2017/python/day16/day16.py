#!/usr/bin/env python3.11

from collections import deque
from string import ascii_lowercase

from rich import print


def get_data(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return f.read()


def solve(data: str, start: str):
    programs = deque(start)
    for instr in data.split(","):
        match instr[0]:
            case "s":
                programs.rotate(int(instr[1:]))
            case "x":
                a, b = map(int, instr[1:].split("/"))
                programs[a], programs[b] = programs[b], programs[a]
            case "p":
                a, b = instr[1:].split("/")
                idxa = find(programs, a)
                idxb = find(programs, b)
                programs[idxa], programs[idxb] = programs[idxb], programs[idxa]
    return "".join(programs)


def find(search, target):
    for idx, item in enumerate(search):
        if item == target:
            return idx
    return None


def find_max(data: str, start: str):
    count = 1
    current = solve(data, start)
    while start != current:
        current = solve(data, current)
        count += 1
    return count


def run(data: str, start: str, num: int):
    max = find_max(data, start)
    current = start
    for _ in range(num % max):
        current = solve(data, current)
    return current


def main():
    data = get_data("day16.txt")
    start = ascii_lowercase[:16]

    p1 = solve(data, start)
    print(f"Part 1: {p1}")

    p2 = run(data, start, 1000000000)
    print(f"Part 2: {p2}")


if __name__ == "__main__":
    main()
