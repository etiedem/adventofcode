import pathlib
import pytest
import day08 as aoc

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example():
    puzzle_input = PUZZLE_DIR / "example1.txt"
    return aoc.get_data(puzzle_input)


@pytest.fixture
def example2():
    puzzle_input = PUZZLE_DIR / "example2.txt"
    return aoc.get_data(puzzle_input)


@pytest.fixture
def example3():
    puzzle_input = PUZZLE_DIR / "example3.txt"
    return aoc.get_data(puzzle_input)


def test_parse_example(example):
    assert aoc.solve(*aoc.parse(example)) == 2


def test_parse_example1(example2):
    assert aoc.solve(*aoc.parse(example2)) == 6


def test_parse_example2(example3):
    assert aoc.part2(*aoc.parse(example3)) == 6
