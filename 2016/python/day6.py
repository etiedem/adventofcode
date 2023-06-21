#!/usr/bin/env python3.11

from collections import Counter, defaultdict

from rich import print


def get_data(filename):
    with open(filename, "r", encoding="utf8") as f:
        return f.readlines()


def get_answer(lines):
    counter = defaultdict(Counter)
    for line in lines:
        for idx, char in enumerate(line.strip()):
            counter[idx].update(char)
    return "".join(x.most_common(1)[0][0] for x in counter.values()), "".join(
        x.most_common()[-1][0] for x in counter.values()
    )


def main():
    data = get_data("day6.txt")
    part1, part2 = get_answer(data)

    print(f"Part 1: {part1}")
    print(f"Part 2: {part2}")


if __name__ == "__main__":
    main()
