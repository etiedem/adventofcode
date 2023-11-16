import pathlib

import pytest

import day12 as aoc

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example():
    puzzle_input = PUZZLE_DIR / "example.txt"
    return aoc.get_data(puzzle_input)


@pytest.fixture
def graph(example):
    return aoc.parse_data(example)


def test_answer_example(graph):
    answer = len(aoc.find_connections(graph, 0))
    assert answer == 6


def test_answer_example1(graph):
    answer = aoc.count_groups(graph)
    assert answer == 2
