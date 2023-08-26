import pathlib

import day01 as aoc
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example():
    puzzle_input = PUZZLE_DIR / "example.txt"
    return aoc.get_data(puzzle_input)


@pytest.mark.skip(reason="Not implemented")
def test_parse_example(example):
    assert aoc.parse(example) == None


@pytest.mark.parametrize(
    "input, expected",
    [
        (["R2", "L3"], [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2), (2, 3)]),
        (["R2", "R2", "R2"], [(0, 0), (1, 0), (2, 0), (2, -1), (2, -2), (1, -2), (0, -2)]),
    ],
)
def test_expand(input, expected):
    answer = aoc.expand(input)
    assert answer == expected


@pytest.mark.parametrize(
    "input, expected", [("R2, L3", 5), ("R2, R2, R2", 2), ("R5, L5, R5, R3", 12)]
)
def test_answer_example(input, expected):
    answer = aoc.get_distance(*aoc.expand(aoc.parse(input))[-1])
    assert answer == expected


@pytest.mark.parametrize("input, expected", [("R8, R4, R4, R8", (4, 0))])
def test_twice(input, expected):
    answer = aoc.get_twice(aoc.expand(aoc.parse(input)))
    assert answer == expected
