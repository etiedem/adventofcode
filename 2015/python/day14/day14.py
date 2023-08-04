#!/usr/bin/env python3.11

from dataclasses import dataclass

from rich import print


@dataclass
class Deer:
    name: str
    dist_per_second: int
    dist_time: int
    rest_time: int
    cur_dist: int = 0
    total_time: int = 0
    points: int = 0

    def __lt__(self, other):
        return self.cur_dist < other.cur_dist

    def step(self):
        self.total_time += 1
        move_cycles = self.total_time // (self.dist_time + self.rest_time)
        cur_dist = self.dist_per_second * self.dist_time * move_cycles
        time_left = self.total_time - (move_cycles * (self.dist_time + self.rest_time))
        if time_left >= self.dist_time:
            cur_dist += self.dist_per_second * self.dist_time
        else:
            cur_dist += self.dist_per_second * time_left

        self.cur_dist = cur_dist

    @classmethod
    def from_str(cls, line):
        tmp = line.split()
        return cls(tmp[0], int(tmp[3]), int(tmp[6]), int(tmp[-2]))


def get_data(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return f.read()


def parse(data):
    return [Deer.from_str(line) for line in data.splitlines()]


def step(deer, steps):
    for _ in range(steps):
        for d in deer:
            d.step()
        largest = max(deer).cur_dist
        for d in deer:
            if d.cur_dist == largest:
                d.points += 1


def main():
    data = get_data("day14.txt")
    deers = parse(data)
    step(deers, 2503)

    p1 = max(deers)
    print(f"Part 1: {p1.cur_dist}")

    p2 = max(d.points for d in deers)
    print(f"Part 2: {p2}")


if __name__ == "__main__":
    main()
