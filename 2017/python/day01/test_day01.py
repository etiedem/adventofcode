import pathlib

import day01 as aoc
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.mark.parametrize(
    "input, expected", [("1122", 3), ("1111", 4), ("1234", 0), ("91212129", 9)]
)
def test_answer_example(input, expected):
    answer = aoc.part1(input)
    assert answer == expected


@pytest.mark.parametrize(
    "input, expected", [("1212", 6), ("1221", 0), ("123425", 4), ("123123", 12), ("12131415", 4)]
)
def test_answer_part2(input, expected):
    answer = aoc.part2(input)
    assert answer == expected
