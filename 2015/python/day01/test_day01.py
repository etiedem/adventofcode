import pathlib

import day01 as aoc
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1():
    puzzle_input = PUZZLE_DIR / "example1.txt"
    return aoc.get_data(puzzle_input)


@pytest.mark.skip(reason="Not implemented")
def test_parse_example1(example1):
    assert aoc.parse(example1) == None


@pytest.mark.parametrize(
    "input, expected",
    [
        ("(())", 0),
        ("()()", 0),
        ("(((", 3),
        ("))(((((", 3),
        ("())", -1),
    ],
)
def test_answer_example1(input, expected):
    answer = aoc.part1(input)
    assert answer == expected


@pytest.mark.parametrize(["input", "expected"], [(")", 1), ("()())", 5)])
def test_answer_part2(input, expected):
    answer = aoc.part2(input)
    assert answer == expected
