import pathlib

import day03 as aoc
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example():
    puzzle_input = PUZZLE_DIR / "example.txt"
    return aoc.Grid.fromstr(aoc.get_data(puzzle_input))


def test_answer_parts(example):
    answer = example.parts
    assert sorted(answer) == sorted([467, 35, 633, 617, 592, 755, 664, 598])


def test_answer_gears(example):
    answer = example.gears
    assert sorted(answer) == sorted([16345, 451490])
