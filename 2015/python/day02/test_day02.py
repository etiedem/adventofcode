import pathlib

import day02 as aoc
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1():
    puzzle_input = PUZZLE_DIR / "example1.txt"
    return aoc.get_data(puzzle_input)


def test_parse_example1(example1):
    assert list(aoc.parse(example1)) == [(2, 3, 4), (1, 1, 10)]


@pytest.mark.parametrize("input, expected", [((2, 3, 4), 58), ((1, 1, 10), 43)])
def test_answer_example1(input, expected):
    answer = aoc.get_sq_ft(*input)
    assert answer == expected


@pytest.mark.parametrize("input, expected", [((2, 3, 4), 34), ((1, 1, 10), 14)])
def test_answer_part2(input, expected):
    answer = aoc.get_ribbon(*input)
    assert answer == expected
