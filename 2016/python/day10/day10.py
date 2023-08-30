#!/usr/bin/env python3.11

from collections import defaultdict
from re import compile

from more_itertools import minmax
from rich import print

NUM_RE = compile(r"\d+")
output = defaultdict(int)
bots = defaultdict(list)
instr = {}


def get_data(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return f.read()


def part1(data, find=(17, 61)):
    loop = []
    findbot = None
    for line in data.splitlines():
        n = list(map(int, NUM_RE.findall(line)))
        match len(n):
            case 2:
                loop.append(n)
            case 3:
                instr[n[0]] = {
                    "lt": "out" if "low to output" in line else "bot",
                    "low": n[1],
                    "ht": "out" if "high to output" in line else "bot",
                    "high": n[2],
                }

    for l in loop:
        bots[l[1]].append(l[0])
        if len(bots[l[1]]) == 2 and (bot := move_stuff(l[1], find)):
            findbot = bot
    return findbot


def move_stuff(bot, find, max_cap=2):
    lt, lb, ht, hb = instr[bot].values()
    low, high = minmax(bots[bot])
    findbot = None

    if low == find[0] and high == find[1]:
        findbot = bot
    bots[bot].clear()
    if ht == "bot":
        bots[hb].append(high)
        if len(bots[hb]) == max_cap and (b := move_stuff(hb, find)):
            findbot = b
    else:
        output[hb] = high

    if lt == "bot":
        bots[lb].append(low)
        if len(bots[lb]) == max_cap and (b := move_stuff(lb, find)):
            findbot = b
    else:
        output[lb] = low

    return findbot


def main():
    data = get_data("day10.txt")

    p1 = part1(data)
    print(f"Part 1: {p1}")

    p2 = output[0] * output[1] * output[2]
    print(f"Part 2: {p2}")


if __name__ == "__main__":
    main()
