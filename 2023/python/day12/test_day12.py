import pathlib

import pytest

import day12 as aoc

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example():
    puzzle_input = PUZZLE_DIR / "example.txt"
    return aoc.get_data(puzzle_input)


def test_answer_example(example):
    answer = aoc.solve(aoc.parse(example))
    assert answer == 21


def test_answer_example1(example):
    answer = aoc.solve(aoc.parse(example, True))
    assert answer == 525152

