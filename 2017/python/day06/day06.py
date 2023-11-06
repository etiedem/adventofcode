#!/usr/bin/env python3.11

from rich import print


def get_data(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return f.read()


def get_cycle_size(seen: list, target: list):
    l_seen = seen[:]
    l_seen.reverse()
    for idx, cur in enumerate(l_seen, 1):
        if cur == target:
            return idx
    return -1


def part1(blocks: list):
    count = 0
    seen = [blocks[:]]
    length = len(blocks)
    while True:
        high = max(blocks)
        redis_idx = blocks.index(high)
        cur_num = blocks[redis_idx]
        redis_num = 1 if cur_num <= (length - 1) else (cur_num // (length - 1))
        redis_total = redis_num * (length - 1) if redis_num > 1 else cur_num
        blocks[redis_idx] -= redis_total
        for idx, _ in enumerate(range(0, redis_total, redis_num), 1):
            blocks[(redis_idx + idx) % length] += redis_num
        count += 1
        if any(blocks == x for x in seen):
            return count, get_cycle_size(seen, blocks)
        seen.append(blocks[:])


def main():
    data = list(map(int, get_data("day06.txt").split()))

    p1, p2 = part1(data)
    print(f"Part 1: {p1}")

    # p2 = part2(data)
    print(f"Part 2: {p2}")


if __name__ == "__main__":
    main()
