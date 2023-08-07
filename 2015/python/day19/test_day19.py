import pathlib

import day19 as aoc
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example():
    puzzle_input = PUZZLE_DIR / "example.txt"
    return aoc.get_data(puzzle_input)


@pytest.fixture
def example2():
    puzzle_input = PUZZLE_DIR / "example2.txt"
    return aoc.get_data(puzzle_input)


def test_parse_example(example):
    assert aoc.parse_forward(example) == ({"H": ["HO", "OH"], "O": ["HH"]}, "HOH")


def test_answer_example(example):
    answer = aoc.get_options(*aoc.parse_forward(example))
    assert answer == {"HOOH", "HOHO", "OHOH", "HHHH"}


def test_answer_part2(example2):
    c, i = aoc.parse_backward(example2)
    answer = aoc.find_sequence(c, "HOHOHO", i)
    assert answer == 6
