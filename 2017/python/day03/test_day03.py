import pathlib

import day03 as aoc
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.mark.parametrize("input, expected", [(1, 0), (12, 3), (23, 2), (1024, 31)])
def test_answer_example(input, expected):
    answer = sum(map(abs, aoc.spiral(int(input)))) - 1
    assert answer == expected


@pytest.mark.skip(reason="Not implemented")
@pytest.mark.parametrize("input, expected", [("", "")])
def test_answer_example1(input, expected):
    answer = aoc.part2(input)
    assert answer == expected
