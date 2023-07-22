import pathlib

import day03 as aoc
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1():
    puzzle_input = PUZZLE_DIR / "example1.txt"
    return aoc.get_data(puzzle_input)


@pytest.mark.skip(reason="Not implemented")
def test_parse_example1(example1):
    assert aoc.parse(example1) == None


@pytest.mark.parametrize("input, expected", [(">", 2), ("^>v<", 4), ("^v^v^v^v^v", 2)])
def test_answer_part1(input, expected):
    answer = aoc.part1(input)
    assert answer == expected


@pytest.mark.parametrize("input, expected", [("^v", 3), ("^>v<", 3), ("^v^v^v^v^v", 11)])
def test_answer_part2(input, expected):
    answer = aoc.part2(input)
    assert answer == expected
