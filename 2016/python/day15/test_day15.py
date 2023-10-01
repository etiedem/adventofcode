import pathlib

import day15 as aoc
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example():
    puzzle_input = PUZZLE_DIR / "example.txt"
    return aoc.get_data(puzzle_input)


@pytest.fixture
def game(example):
    return aoc.Game.from_str(example)


def test_parse_example(example):
    assert aoc.Game.from_str(example).disks == [aoc.Disk(4, 5), aoc.Disk(1, 2)]


def test_exmple_zero(game):
    game.set_zero()
    first = game.disks[0]
    assert first.cur_pos == first.max_pos - 1


def test_example_answer(game):
    assert aoc.find_answer(game).time == 5
