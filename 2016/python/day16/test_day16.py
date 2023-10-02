import pathlib

import day16 as aoc
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example():
    puzzle_input = PUZZLE_DIR / "example.txt"
    return aoc.get_data(puzzle_input)


@pytest.mark.parametrize(
    "input, expected",
    [
        ("1", "100"),
        ("0", "001"),
        ("11111", "11111000000"),
        ("111100001010", "1111000010100101011110000"),
    ],
)
def test_double(input, expected):
    assert aoc.double(input) == expected


@pytest.mark.parametrize("input, expected", [("110010110100", "100")])
def test_checksum(input, expected):
    assert aoc.checksum(input) == expected


@pytest.mark.parametrize("input, expected", [(("10000", 20), "01100")])
def test_solve(input, expected):
    assert aoc.solve(*input) == expected
