import pathlib

import pytest

import day15 as aoc

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example():
    puzzle_input = PUZZLE_DIR / "example.txt"
    return aoc.get_data(puzzle_input).strip()


def test_parse_example(example):
    assert aoc.part1(example) == 1320


def test_parse_example1(example):
    assert aoc.calc_total_focal_length(aoc.part2(example)) == 145

