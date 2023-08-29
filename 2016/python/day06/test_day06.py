import pathlib

import day06 as aoc
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example():
    puzzle_input = PUZZLE_DIR / "example.txt"
    return aoc.get_data(puzzle_input)


def test_answer_example(example):
    answer1, answer2 = aoc.solve(example)
    assert answer1 == "easter"
    assert answer2 == "advent"
