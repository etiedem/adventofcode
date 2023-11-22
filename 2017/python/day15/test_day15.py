import pathlib
import pytest
import day15 as aoc

PUZZLE_DIR = pathlib.Path(__file__).parent


def test_parse_example():
    assert aoc.part1(65, 8921) == 588
