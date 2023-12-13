import pathlib
import pytest
import day09 as aoc

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example():
    puzzle_input = PUZZLE_DIR / "example.txt"
    return aoc.parse(aoc.get_data(puzzle_input))


def test_parse_example(example):
    assert aoc.solve(example) == (114, 2)
