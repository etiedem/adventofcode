import pathlib

import day15 as aoc
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example():
    puzzle_input = PUZZLE_DIR / "example.txt"
    return aoc.get_data(puzzle_input)


def test_parse_example(example):
    assert aoc.parse(example) == {
        "Butterscotch": aoc.Ingredient("Butterscotch", -1, -2, 6, 3, 8),
        "Cinnamon": aoc.Ingredient("Cinnamon", 2, 3, -2, -1, 3),
    }


def test_calc_score(example):
    test = (("Butterscotch", 44), ("Cinnamon", 56))
    assert aoc.calc_score(aoc.parse(example), test) == 62_842_880


def test_best_example(example):
    assert aoc.find_best(aoc.parse(example), 100) == 62_842_880


def test_calorie_example(example):
    assert aoc.find_best(aoc.parse(example), 100, True) == 57_600_000


@pytest.mark.skip(reason="Not implemented")
@pytest.mark.parametrize("input, expected", [("", "")])
def test_answer_example(input, expected):
    answer = aoc.part1(input)
    assert answer == expected


@pytest.mark.skip(reason="Not implemented")
@pytest.mark.parametrize("input, expected", [("", "")])
def test_answer_example1(input, expected):
    answer = aoc.part2(input)
    assert answer == expected
