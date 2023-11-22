#!/usr/bin/env python3.11

from rich import print


class Generator:
    def __init__(self, factor: int, start: int, filter: int):
        self.factor = factor
        self.start = start
        self.filter = filter

    def run(self, part2=False):
        current = self.start
        while True:
            current = (current * self.factor) % 2147483647
            if part2:
                if current % self.filter == 0:
                    yield bin(current)[2:].zfill(32)
            else:
                yield bin(current)[2:].zfill(32)


def get_data(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return f.read()


def part1(start1, start2):
    gen1 = Generator(16807, start1, 4)
    gen2 = Generator(48271, start2, 8)
    count = 0
    for idx, (a, b) in enumerate(zip(gen1.run(), gen2.run())):
        if idx == 40_000_000:
            break
        if a[-16:] == b[-16:]:
            count += 1
    return count


def part2(start1, start2):
    gen1 = Generator(16807, start1, 4)
    gen2 = Generator(48271, start2, 8)
    count = 0
    for idx, (a, b) in enumerate(zip(gen1.run(True), gen2.run(True))):
        if idx == 5_000_000:
            break
        if a[-16:] == b[-16:]:
            count += 1
    return count


def main():
    data = get_data("day15.txt")
    start1, start2 = [int(line.split()[-1]) for line in data.splitlines()]

    p1 = part1(start1, start2)
    print(f"Part 1: {p1}")

    p2 = part2(start1, start2)
    print(f"Part 2: {p2}")


if __name__ == "__main__":
    main()
