import pathlib

import day10 as aoc
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example():
    return "3,4,1,5"


@pytest.mark.parametrize(
    "input, expected",
    [
        ("3", [2, 1, 0, 3, 4]),
        ("3,4", [4, 3, 0, 1, 2]),
        ("3,4,1", [4, 3, 0, 1, 2]),
        ("3,4,1,5", [3, 4, 2, 1, 0]),
    ],
)
def test_parse_example(input, expected):
    assert aoc.Knot(5).part1(input).data == expected
