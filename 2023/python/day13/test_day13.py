import pathlib

import pytest

import day13 as aoc

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example():
    puzzle_input = PUZZLE_DIR / "example.txt"
    return aoc.parse(aoc.get_data(puzzle_input))


def test_answer_example(example):
    answer = aoc.solve(example)
    assert answer == 405


def test_answer_example1(example):
    answer = aoc.solve(example, part2=True)
    assert answer == 400

