import pathlib

import day05 as aoc
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.mark.parametrize("input, expected", [([0, 3, 0, 1, -3], 5)])
def test_answer_example(input, expected):
    answer = aoc.solve(input)
    assert answer == expected


@pytest.mark.parametrize("input, expected", [([0, 3, 0, 1, -3], 10)])
def test_answer_example1(input, expected):
    answer = aoc.solve(input, True)
    assert answer == expected
