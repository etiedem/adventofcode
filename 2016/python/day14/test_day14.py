import pathlib

import day14 as aoc
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example():
    return aoc.next_pad("abc")


def test_next_key(example):
    assert example[0][0] == 39


def test_next_key_part2():
    assert aoc.next_pad("abc", True)[0][0] == 10


@pytest.mark.skip(reason="Not implemented")
@pytest.mark.parametrize("input, expected", [("", "")])
def test_answer_example(input, expected):
    answer = aoc.part1(input)
    assert answer == expected


@pytest.mark.skip(reason="Not implemented")
@pytest.mark.parametrize("input, expected", [("", "")])
def test_answer_example1(input, expected):
    answer = aoc.part2(input)
    assert answer == expected
