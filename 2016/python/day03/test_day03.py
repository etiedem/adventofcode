import pathlib

import day03 as aoc
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example():
    puzzle_input = PUZZLE_DIR / "example.txt"
    return aoc.get_data(puzzle_input)


def test_parse_row(example):
    answer = aoc.parse_row(example)
    assert list(answer) == [[5, 10, 25], [10, 10, 5], [25, 5, 10]]


def test_parse_column(example):
    answer = aoc.parse_column(example)
    assert list(answer) == [[5, 10, 25], [10, 10, 5], [25, 5, 10]]


@pytest.mark.parametrize("input, expected", [((5, 10, 25), False), ((10, 10, 5), True)])
def test_triangle(input, expected):
    assert aoc.is_triangle(input) is expected
