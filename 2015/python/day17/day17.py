#!/usr/bin/env python3.11

from rich import print


def get_data(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return f.read()


def find_numbers(ans, arr: list[int], temp: list[int], total: int, index: int, limit):
    if total == 0:
        ans.append(list(temp))
        return

    for i in range(index, len(arr)):
        if limit and len(temp) > limit:
            continue
        temp.append(arr[i])
        find_numbers(ans, arr, temp, total - arr[i], i + 1, limit)

        temp.remove(arr[i])


def get_sums(total, containers, limit=None):
    ans, temp = [], []
    arr = sorted(containers)
    find_numbers(ans, arr, temp, total, 0, limit)
    return ans


def main():
    data = get_data("day17.txt")
    containers = list(map(int, data.splitlines()))

    p1 = get_sums(150, containers)
    print(f"Part 1: {len(p1)}")

    min_containers = len(min(p1, key=len)) - 1
    p2 = get_sums(150, containers, limit=min_containers)
    print(f"Part 2: {len(p2)}")


if __name__ == "__main__":
    main()
