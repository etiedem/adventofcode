import pathlib

import pytest

import day16 as aoc

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example():
    puzzle_input = PUZZLE_DIR / "example.txt"
    return aoc.Cave(aoc.parse(aoc.get_data(puzzle_input)))


def test_parse_example(example):
    answer = aoc.dfs(example)
    answer = len({p[0:2] for p in answer})
    assert answer == 46


def test_parse_example1(example):
    answer = aoc.part2(example)
    assert answer == 51

