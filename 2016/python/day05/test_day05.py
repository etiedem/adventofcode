import pathlib

import day05 as aoc
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example():
    puzzle_input = "abc"
    return puzzle_input


def test_next_hash(example):
    h = aoc.next_hash(example)
    assert next(h)[0] == "abc3231929"
    assert next(h)[0] == "abc5017308"
    assert next(h)[0] == "abc5278568"


def test_answer_part1(example):
    answer = aoc.part1(example)
    assert answer == "18f47a30"


@pytest.mark.skip(reason="Not implemented")
@pytest.mark.parametrize("input, expected", [("", "")])
def test_answer_example1(input, expected):
    answer = aoc.part2(input)
    assert answer == expected
