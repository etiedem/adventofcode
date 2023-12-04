import pathlib

import day04 as aoc
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example():
    puzzle_input = PUZZLE_DIR / "example.txt"
    return [aoc.Card.from_str(line) for line in aoc.get_data(puzzle_input).splitlines()]


@pytest.mark.parametrize("expected", [(8, 2, 2, 1, 0, 0)])
def test_answer_example(example, expected):
    answer = tuple(card.points for card in example)
    assert answer == expected


def test_answer_example1(example):
    answer = aoc.count_cards(example)
    assert answer == 30
