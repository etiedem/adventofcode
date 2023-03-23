#!/usr/bin/env python3.11


from collections import deque
from itertools import islice


def get_data(filename):
    with open(filename) as f:
        yield from (line.strip() for line in f)


def sliding_window(iterable, n):
    # sliding_window('ABCDEFG', 4) --> ABCD BCDE CDEF DEFG
    it = iter(iterable)
    window = deque(islice(it, n), maxlen=n)
    if len(window) == n:
        yield tuple(window)
    for x in it:
        window.append(x)
        yield tuple(window)


def start_of_packet(line, win_size=4):
    count = win_size - 1
    for window in sliding_window(line, win_size):
        count += 1
        if len(set(window)) == win_size:
            break
    return count


def main():
    for d in get_data("day6.txt"):
        print(f"PART1: {start_of_packet(d, 4)}")
        print(f"PART2: {start_of_packet(d, 14)}")


if __name__ == "__main__":
    main()
