import pathlib

import pytest

import day16 as aoc

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example():
    puzzle_input = list("abcde")
    return puzzle_input


@pytest.mark.parametrize(
    "input, task, expected",
    [
        ("abcde", "s1", "eabcd"),
        ("eabcd", "x3/4", "eabdc"),
        ("eabdc", "pe/b", "baedc"),
    ],
)
def test_answer_example(input, task, expected):
    answer = aoc.solve(task, input)
    assert answer == expected


@pytest.mark.parametrize(
    "input, task, expected",
    [
        ("abcde", "s1,x3/4,pe/b", "ceadb"),
    ],
)
def test_answer_example1(input, task, expected):
    answer = aoc.run(task, input, 2)
    assert answer == expected
