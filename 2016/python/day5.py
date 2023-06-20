#!/usr/bin/env python3.11

from hashlib import md5

from rich import print


def get_data(filename):
    with open(filename, "r", encoding="utf8") as f:
        return f.read()


def get_password_part1(door):
    counter = 0
    password_length = 8
    output = []
    while len(output) < password_length:
        current = bytes(f"{door}{counter}", encoding="ascii")
        door_hash = md5(current).hexdigest()
        if door_hash.startswith("00000"):
            output.append(door_hash[5])
        counter += 1
    return "".join(output)


def get_password_part2(door):
    counter = 0
    password_length = 8
    output = [None] * password_length
    while not all(output):
        current = bytes(f"{door}{counter}", encoding="ascii")
        door_hash = md5(current, usedforsecurity=False).hexdigest()
        if (
            door_hash.startswith("00000")
            and door_hash[5].isdigit()
            and int(door_hash[5]) < password_length
            and not output[int(door_hash[5])]
        ):
            output[int(door_hash[5])] = door_hash[6]
        counter += 1
    return "".join(output)


def main():
    data = get_data("day5.txt").strip()
    part1 = get_password_part1(data)
    print(f"Part1: {part1}")

    part2 = get_password_part2(data)
    print(f"Part2: {part2}")


if __name__ == "__main__":
    main()
