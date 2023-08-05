#!/usr/bin/env python3.11

import itertools
from dataclasses import dataclass
from re import compile

from rich import print

LINE_RE = compile(r"(^(?:\w+)|(?:[-0-9]+))")


@dataclass
class Ingredient:
    name: str
    cap: int
    dur: int
    flav: int
    text: int
    cal: int


def get_data(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return f.read()


def parse(data):
    result = {}
    for line in data.splitlines():
        name, *nums = LINE_RE.findall(line)
        result[name] = Ingredient(name, *map(int, nums))
    return result


def calc_score(ingredients, amounts, calorie=False):
    total_cap, total_dur, total_flav = 0, 0, 0
    total_text, total_cal = 0, 0
    max_calories = 500

    for amount in amounts:
        name, num = amount
        total_cap += ingredients[name].cap * num
        total_dur += ingredients[name].dur * num
        total_flav += ingredients[name].flav * num
        total_text += ingredients[name].text * num
        total_cal += ingredients[name].cal * num

    if any(x < 1 for x in (total_cap, total_dur, total_flav, total_text)):
        return 0

    if calorie and total_cal != max_calories:
        return 0

    return total_cap * total_dur * total_flav * total_text


def find_best(ingredients, num=100, cal=False):
    max_score = -1
    i = list(ingredients.keys())
    for nums in itertools.product(range(num), repeat=len(i)):
        if sum(nums) != num:
            continue
        score = calc_score(ingredients, zip(i, nums, strict=True), cal)
        max_score = max(score, max_score)
    return max_score


def main():
    data = get_data("day15.txt")
    ingredients = parse(data)

    p1 = find_best(ingredients)
    print(f"Part 1: {p1}")

    p2 = find_best(ingredients, cal=True)
    print(f"Part 2: {p2}")


if __name__ == "__main__":
    main()
