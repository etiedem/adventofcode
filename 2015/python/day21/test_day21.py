import pathlib

import day21 as aoc
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example():
    puzzle_input = PUZZLE_DIR / "example.txt"
    return aoc.get_data(puzzle_input)


def test_parse_example(example):
    assert aoc.parse(example) == (12, 7, 2)


def test_answer_battle(example):
    player = (8, 5, 5)
    boss = aoc.parse(example)
    answer = aoc.player_win(boss=boss, player=player)
    assert answer == True


@pytest.mark.skip(reason="Not implemented")
@pytest.mark.parametrize("input, expected", [("", "")])
def test_answer_example1(input, expected):
    answer = aoc.part2(input)
    assert answer == expected
