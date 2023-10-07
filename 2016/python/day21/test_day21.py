import pathlib

import day21 as aoc
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example():
    puzzle_input = "abcde"
    return puzzle_input


@pytest.fixture
def example1():
    puzzle_input = aoc.get_data("example.txt")
    return puzzle_input


def test_parse_example(example):
    assert aoc.InstrSet([], example).base == list(example)


@pytest.mark.parametrize(
    "input, output",
    [
        (0, "abcde"),
        (1, "eabcd"),
        (2, "deabc"),
        (3, "cdeab"),
        (4, "bcdea"),
        (5, "abcde"),
        (6, "eabcd"),
    ],
)
def test_rotate_right(example, input, output):
    answer = aoc.InstrSet([], example).rotate_right(input).base
    assert answer == list(output)


@pytest.mark.parametrize(
    "input, output",
    [
        (0, "abcde"),
        (1, "bcdea"),
        (2, "cdeab"),
        (3, "deabc"),
        (4, "eabcd"),
        (5, "abcde"),
        (6, "bcdea"),
    ],
)
def test_rotate_left(example, input, output):
    answer = aoc.InstrSet([], example).rotate_left(input).base
    assert answer == list(output)


@pytest.mark.parametrize("input, output", [("b", "deabc"), ("c", "cdeab"), ("d", "bcdea")])
def test_rotate_based(example, input, output):
    answer = aoc.InstrSet([], example).rotate_based(input).base
    assert answer == list(output)


def test_reverse_pos(example):
    answer = aoc.InstrSet([], example).reverse_pos(0, 4).base
    assert answer == list("edcba")


def test_swap_pos(example):
    answer = aoc.InstrSet([], example).swap_pos(0, 2).base
    assert answer == list("cbade")


def test_swap_letter(example):
    answer = aoc.InstrSet([], example).swap_letter("a", "e").base
    assert answer == list("ebcda")


def test_example1(example, example1):
    answer = aoc.InstrSet(example1, example).scramble()
    assert answer == "decab"
