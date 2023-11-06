import pathlib

import day06 as aoc
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.mark.parametrize("input, expected", [([0, 2, 7, 0], (5, 4))])
def test_answer_example(input, expected):
    answer = aoc.part1(input)
    assert answer == expected
