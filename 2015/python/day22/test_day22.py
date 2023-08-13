import pathlib

import day22_2 as aoc
import pytest
from rich import print

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example():
    boss = aoc.Character("Boss", 13, 0, 8)
    player = aoc.Character("Player", 10, 250, 0)
    return player, boss


def test_answer_example(example):
    state = aoc.State(*example)
    state = next(state([aoc.spells[3]]))
    state = next(state([aoc.spells[0]]))
    answer = state
    assert (answer.player.hp, answer.boss.hp) == (2, 0)


def test_answer_run(example):
    state = aoc.State(*example)
    answer = aoc.search(state)
    assert (answer.player.hp, answer.boss.hp) == (2, 0)


def test_answer_example_hard(example):
    state = aoc.State(*example, hard=True)
    state = next(state([aoc.spells[3]]))
    answer = state
    assert (answer.player.hp, answer.boss.hp) == (1, 10)


@pytest.mark.skip(reason="Not implemented")
@pytest.mark.parametrize("input, expected", [("", "")])
def test_answer_example1(input, expected):
    answer = aoc.part2(input)
    assert answer == expected
