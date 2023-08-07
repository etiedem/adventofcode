#!/usr/bin/env python3.11

import itertools

import numpy as np
from rich import print


def get_data(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return f.read()


def parse(data):
    return tuple(map(int, (x.split(": ")[1] for x in data.splitlines())))


def parse_store(data):
    r_w, r_a, r_r = data.split("\n\n")
    weapons = [[*map(int, d[-3:])] for r in r_w.splitlines()[1:] if (d := r.split())]
    armor = [[*map(int, d[-3:])] for r in r_a.splitlines()[1:] if (d := r.split())]
    rings = [[*map(int, d[-3:])] for r in r_r.splitlines()[1:] if (d := r.split())]
    return weapons, armor, rings


def player_win(boss, player):
    b_hp, b_dmg, b_arm = boss
    p_hp, p_dmg, p_arm = player

    while True:
        b_hp -= p_dmg - b_arm
        if b_hp <= 0:
            return True
        p_hp -= b_dmg - p_arm
        if p_hp <= 0:
            return False


def solve(boss, weapons, armor, rings):
    min_cost = np.inf
    max_cost = -1
    for w, a, r1, r2 in itertools.product(weapons, armor, rings, rings):
        if r1 == r2:  # can't have 2 of same ring
            continue
        c_cost = w[0] + a[0] + r1[0] + r2[0]
        player = (100, w[1] + r1[1] + r2[1], a[2] + r1[2] + r2[2])
        if c_cost < min_cost and player_win(boss, player):
            min_cost = c_cost
        if c_cost > max_cost and not player_win(boss, player):
            max_cost = c_cost
    return min_cost, max_cost


def main():
    boss = parse(get_data("day21.txt"))
    weapons, armor, rings = parse_store(get_data("store.txt"))
    armor.append((0, 0, 0))  # account for no armor
    rings.append((0, 0, 0))  # account for no ring

    p1, p2 = solve(boss, weapons, armor, rings)

    print(f"Part 1: {p1}")
    print(f"Part 2: {p2}")


if __name__ == "__main__":
    main()
