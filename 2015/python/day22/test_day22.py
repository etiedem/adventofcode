import pathlib

import day22 as aoc
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example():
    boss = aoc.Boss(13, 0, [], 8)
    player = aoc.Player(10, 0, [], 250)
    return player, boss


def test_answer_example(example):
    state = aoc.State(*example)
    state = state(aoc.spells[3])
    state = state(aoc.spells[0])
    # print(state)
    answer = state
    print(state)
    # answer = aoc.search(aoc.State(*example), sorted(aoc.spells))
    # print(answer)
    assert (answer.player.health, answer.boss.health) == (2, 0)


@pytest.mark.skip(reason="Not implemented")
@pytest.mark.parametrize("input, expected", [("", "")])
def test_answer_example1(input, expected):
    answer = aoc.part2(input)
    assert answer == expected
