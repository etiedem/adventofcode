import pathlib

import day02 as aoc
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example():
    return aoc.Grid(aoc.part1_raw)


@pytest.fixture
def example2():
    return aoc.Grid(aoc.part2_raw)


def test_parse_example(example):
    assert example.grid == [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]
    assert example.pos == (1, 1)


def test_parse_example2(example2):
    assert example2.grid == [
        [" ", " ", "1", " ", " "],
        [" ", "2", "3", "4", " "],
        ["5", "6", "7", "8", "9"],
        [" ", "A", "B", "C", " "],
        [" ", " ", "D", " ", " "],
    ]
    assert example2.pos == (0, 2)


def test_up(example):
    example.move("U")
    assert example.pos == (1, 0)


def test_up_bounds(example):
    example.move("U").move("U").move("U")
    assert example.pos == (1, 0)


def test_right(example):
    example.move("R")
    assert example.pos == (2, 1)


def test_right_bounds(example):
    example.move("R").move("R").move("R")
    assert example.pos == (2, 1)


def test_down(example):
    example.move("D")
    assert example.pos == (1, 2)


def test_down_bounds(example):
    example.move("D").move("D").move("D")
    assert example.pos == (1, 2)


def test_left(example):
    example.move("L")
    assert example.pos == (0, 1)


def test_left_bounds(example):
    example.move("L").move("L").move("L")
    assert example.pos == (0, 1)


@pytest.mark.parametrize(
    "input, expected",
    [
        (
            """ULL
RRDDD
LURDL
UUUUD""",
            "1985",
        )
    ],
)
def test_sample(example, input, expected):
    assert aoc.solve(input, example) == expected


@pytest.mark.skip(reason="Not implemented")
@pytest.mark.parametrize("input, expected", [("", "")])
def test_answer_example(input, expected):
    answer = aoc.solve(input)
    assert answer == expected


@pytest.mark.skip(reason="Not implemented")
@pytest.mark.parametrize("input, expected", [("", "")])
def test_answer_example1(input, expected):
    answer = aoc.part2(input)
    assert answer == expected
