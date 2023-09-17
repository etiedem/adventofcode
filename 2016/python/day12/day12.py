#!/usr/bin/env python3.11

from rich import print


def get_data(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return f.read()


def run_instr(data, part2=False):
    register = {"a": 0, "b": 0, "c": 0, "d": 0}
    if part2:
        register["c"] = 1
    instr = [x.split() for x in data.splitlines()]
    idx = 0
    while idx < len(instr):
        item = instr[idx]
        match item[0]:
            case "cpy":
                value = int(item[1]) if item[1].isdigit() else register[item[1]]
                register[item[2]] = value
            case "inc":
                register[item[1]] += 1
            case "dec":
                register[item[1]] -= 1
            case "jnz":
                if item[1].isdigit():
                    if int(item[1]) != 0:
                        idx += int(item[2])
                        continue
                elif register[item[1]] != 0:
                    idx += int(item[2])
                    continue
        idx += 1
    return register["a"]


def main():
    data = get_data("day12.txt")

    p1 = run_instr(data)
    print(f"Part 1: {p1}")

    p2 = run_instr(data, True)
    print(f"Part 2: {p2}")


if __name__ == "__main__":
    main()
