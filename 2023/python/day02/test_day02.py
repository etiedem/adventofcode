import pathlib

import day02 as aoc
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example():
    puzzle_input = PUZZLE_DIR / "example.txt"
    return aoc.get_data(puzzle_input)


@pytest.fixture
def games(example):
    return aoc.parse_input(example)


def test_answer_example(games):
    answer = [game.is_valid({"red": 12, "green": 13, "blue": 14})
              for game in games]
    assert answer == [True, True, False, False, True]


def test_answer_example1(games):
    answer = aoc.part2(games)
    assert answer == 2286
