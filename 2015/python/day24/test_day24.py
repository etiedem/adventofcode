import pathlib

import day24 as aoc
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example():
    puzzle_input = [*range(1, 6), *range(7, 12)]
    return puzzle_input


def test_parse_example(example):
    print(example)
    print(sum(example) // 3)
    assert True is False


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
