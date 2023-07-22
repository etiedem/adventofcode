#!/usr/bin/env python3.11

from rich import print


def get_data(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return f.read()


def part1(moves):
    cur = (0, 0)
    pos = {cur}
    for move in moves:
        match move:
            case "^":
                cur = (cur[0], cur[1] + 1)
            case "v":
                cur = (cur[0], cur[1] - 1)
            case ">":
                cur = (cur[0] + 1, cur[1])
            case "<":
                cur = (cur[0] - 1, cur[1])
            case _:
                raise ValueError(f"Invalid move: {move}")
        pos.add(cur)
    return len(pos)


def part2(moves):
    cur_s = (0, 0)
    cur_r = (0, 0)
    pos_s = {cur_s}
    pos_r = {cur_r}

    for idx, move in enumerate(moves):
        match move:
            case "^":
                cur = (0, 1)
            case "v":
                cur = (0, -1)
            case ">":
                cur = (1, 0)
            case "<":
                cur = (-1, 0)
            case _:
                raise ValueError(f"Invalid move: {move}")
        if idx % 2 == 0:
            cur_r = (cur_r[0] + cur[0], cur_r[1] + cur[1])
            pos_r.add(cur_r)
        else:
            cur_s = (cur_s[0] + cur[0], cur_s[1] + cur[1])
            pos_s.add(cur_s)
    return len(pos_s | pos_r)


def main():
    data = get_data("day03.txt")

    p1 = part1(data)
    print(f"Part 1: {p1}")

    p2 = part2(data)
    print(f"Part 2: {p2}")


if __name__ == "__main__":
    main()
