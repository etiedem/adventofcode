import pathlib

import day06 as aoc
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example():
    puzzle_input = PUZZLE_DIR / "example.txt"
    return aoc.get_data(puzzle_input)


def test_parse_example(example):
    assert list(aoc.parse(example)) == [
        ("turn on", 0, 0, 999, 999),
        ("toggle", 0, 0, 999, 0),
        ("turn off", 499, 499, 500, 500),
    ]


@pytest.mark.parametrize(
    "input, expected",
    [
        (
            ((0, 0), (2, 2)),
            [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)],
        ),
        (((1, 1), (3, 1)), [(1, 1), (2, 1), (3, 1)]),
    ],
)
def test_square(input, expected):
    assert list(aoc.Lights().get_square(input[0], input[1])) == expected


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
