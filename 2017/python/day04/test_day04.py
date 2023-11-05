import pathlib

import day04 as aoc
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.mark.parametrize(
    "input, expected",
    [("aa bb cc dd ee", True), ("aa bb cc dd aa", False), ("aa bb cc dd aaa", True)],
)
def test_answer_example(input, expected):
    answer = aoc.is_valid(input)
    assert answer == expected


@pytest.mark.parametrize(
    "input, expected",
    [
        ("abcde fghij", True),
        ("abcde xyz ecdab", False),
        ("a ab abc abd abf abj", True),
        ("iiii oiii ooii oooi oooo", True),
        ("oiii ioii iioi iiio", False),
    ],
)
def test_answer_example1(input, expected):
    answer = aoc.is_valid(input, True)
    assert answer == expected
