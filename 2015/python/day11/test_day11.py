import pathlib

import day11 as aoc
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
        ("hijklmmn", False),
        ("abbceffg", False),
        ("abbcegjk", False),
        ("abcdffaa", True),
        ("ghjaabcc", True),
    ],
)
def test_is_valid(input, expected):
    answer = aoc.is_valid(input)
    assert answer == expected


@pytest.mark.parametrize(
    "input, expected",
    [
        ("abcdefgh", "abcdffaa"),
        ("ghijklmn", "ghjaabcc"),
    ],
)
def test_next_password(input, expected):
    answer = aoc.solve(input)
    assert answer == expected


@pytest.mark.skip(reason="Not implemented")
@pytest.mark.parametrize("input, expected", [("", "")])
def test_answer_example1(input, expected):
    answer = aoc.part2(input)
    assert answer == expected
