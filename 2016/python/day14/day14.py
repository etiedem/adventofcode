#!/usr/bin/env python3.11

import hashlib
from collections import defaultdict
from re import compile

from rich import print

RE_TRIPLE = compile(r"(.)\1{2,2}")
RE_QUINT = compile(r"(.)\1{4,4}")


def get_data(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return f.read()


def next_hash(salt, part2):
    count = 0
    while True:
        seed = f"{salt}{count}"
        if part2:
            for _ in range(2017):
                seed = hashlib.md5(seed.encode()).hexdigest()
            yield count, seed

        else:
            yield count, hashlib.md5(seed.encode()).hexdigest()
        count += 1


def next_pad(salt, part2=False):
    nh = next_hash(salt, part2)
    counter = defaultdict(list)  # keep track of triples
    answer = []
    MAX_AGE = 1000
    PAD_LEN = 64

    for idx, pad in nh:
        # increment how long a triple has been in counter
        # if item has been in longer than MAX_AGE remove
        remove = []
        for key, items in counter.items():
            for start, group in items:
                if idx - start > MAX_AGE:
                    remove.append((key, start, group))

        # remove old triples in counter
        for key, start, group in remove:
            counter[key].remove((start, group))
            if len(counter[key]) == 0:
                del counter[key]

        m = None
        if (m := RE_QUINT.search(pad)) and (g := m.group()[:3]) in counter:
            for start, item in counter[g]:
                if idx - start < MAX_AGE:
                    answer.append((start, item))
            if len(answer) >= PAD_LEN:
                return sorted(answer)[:64]
        if m:
            continue

        if m := RE_TRIPLE.search(pad):
            # allow duplicate triples so the key
            # is the index of the key it came from
            counter[m.group()].append((idx, m.group()))

    return None


def main():
    data = get_data("day14.txt")

    p1 = next_pad(data)
    print(f"Part 1: {p1[-1][0]}")

    # p2 = next_pad(data, True)
    # print(f"Part 2: {p2[-1][0]}")
    p2 = next_pad("abc", True)
    print(f"Part 2: {p2}")

    # 20331 is too low


if __name__ == "__main__":
    main()
