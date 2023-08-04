import pathlib
from copy import deepcopy

import day14 as aoc
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example():
    puzzle_input = PUZZLE_DIR / "example.txt"
    return aoc.get_data(puzzle_input)


def test_parse_example(example):
    assert aoc.parse(example) == [
        aoc.Deer(name="Comet", dist_per_second=14, dist_time=10, rest_time=127),
        aoc.Deer(name="Dancer", dist_per_second=16, dist_time=11, rest_time=162),
    ]


def test_answer_example_10s(example):
    deer = aoc.parse(example)
    aoc.step(deer, 10)
    answer = {d.name: d.cur_dist for d in deer}
    assert answer == {"Comet": 140, "Dancer": 160}


def test_answer_example_11s(example):
    deer = aoc.parse(example)
    aoc.step(deer, 11)
    answer = {d.name: d.cur_dist for d in deer}
    assert answer == {"Comet": 140, "Dancer": 176}


def test_answer_example_12s(example):
    deer = aoc.parse(example)
    aoc.step(deer, 12)
    answer = {d.name: d.cur_dist for d in deer}
    assert answer == {"Comet": 140, "Dancer": 176}


def test_answer_example_1000s(example):
    deer = aoc.parse(example)
    aoc.step(deer, 1000)
    answer = {d.name: d.cur_dist for d in deer}
    assert answer == {"Comet": 1120, "Dancer": 1056}


def test_answer_points_1000s(example):
    deer = aoc.parse(example)
    aoc.step(deer, 1000)
    points = {d.name: d.points for d in deer}
    assert points == {"Comet": 312, "Dancer": 689}


@pytest.mark.skip(reason="Not implemented")
@pytest.mark.parametrize("input, expected", [("", "")])
def test_answer_example1(input, expected):
    answer = aoc.part2(input)
    assert answer == expected
