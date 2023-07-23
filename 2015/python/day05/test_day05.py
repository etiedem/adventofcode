import pathlib

import day05 as aoc
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example():
    puzzle_input = PUZZLE_DIR / "example.txt"
    return aoc.get_data(puzzle_input)


@pytest.mark.skip(reason="Not implemented")
def test_parse_example(example):
    assert aoc.parse(example) == None


@pytest.mark.parametrize(
    "input, expected",
    [
        ("ugknbfddgicrmopn", True),
        ("aaa", True),
        ("jchzalrnumimnmhp", False),
        ("haegwjzuvuyypxyu", False),
        ("dvszwmarrgswjxmb", False),
    ],
)
def test_answer_example(input, expected):
    answer = aoc.part1(input)
    assert answer is expected


@pytest.mark.parametrize(
    "input, expected",
    [
        ("qjhvhtzxzqqjkmpb", True),
        ("xxyxx", True),
        ("uurcxstgmygtbstg", False),
        ("ieodomkazucvgmuy", False),
    ],
)
def test_answer_example1(input, expected):
    answer = aoc.part2(input)
    assert answer is expected
