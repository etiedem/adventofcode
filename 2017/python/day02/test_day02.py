import pathlib

import day02 as aoc
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.mark.parametrize("input, expected", [("5 1 9 5", 8), ("7 5 3", 4), ("2 4 6 8", 6)])
def test_answer_example(input, expected):
    answer = aoc.part1(input)
    assert answer == expected


@pytest.mark.parametrize("input, expected", [("5 9 2 8", 4), ("9 4 7 3", 3), ("3 8 6 5", 2)])
def test_answer_example1(input, expected):
    answer = aoc.part2(input)
    assert answer == expected
