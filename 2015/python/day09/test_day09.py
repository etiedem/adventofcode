import pathlib

import day09 as aoc
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example():
    puzzle_input = PUZZLE_DIR / "example.txt"
    return aoc.get_data(puzzle_input)


@pytest.fixture
def realdata():
    puzzle_input = PUZZLE_DIR / "day09.txt"
    return aoc.get_data(puzzle_input)


def test_get_names(realdata):
    for line in realdata.splitlines():
        assert line.split()[0] in aoc.KEY
        assert line.split()[2] in aoc.KEY


@pytest.mark.skip(reason="Not implemented")
@pytest.mark.parametrize("input, expected", [("", "")])
def test_answer_example(input, expected):
    answer = aoc.part1(input)
    assert answer == expected


@pytest.mark.skip(reason="Not implemented")
@pytest.mark.parametrize("input, expected", [("", "")])
def test_answer_example1(input, expected):
    answer = aoc.part2(input)
    assert answer == expected
