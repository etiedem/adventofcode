import pathlib

import day07 as aoc
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example():
    puzzle_input = PUZZLE_DIR / "example.txt"
    return aoc.get_data(puzzle_input)


@pytest.fixture
def example_tree(example):
    return aoc.create_tree(example)


def test_parse_example(example):
    nodes = {}
    for line in example.splitlines():
        node = aoc.Node.from_str(line)
        nodes[node.name] = node

    answers = [
        ("pbga", 66),
        ("xhth", 57),
        ("ebii", 61),
        ("havc", 66),
        ("ktlj", 57),
        ("fwft", 72),
        ("qoyq", 66),
        ("padx", 45),
        ("tknk", 41),
        ("jptl", 61),
        ("ugml", 68),
        ("gyxo", 61),
        ("cntj", 57),
    ]
    result = {name: aoc.Node(name, weight) for name, weight in answers}
    assert nodes == result


def test_answer_example(example_tree):
    assert example_tree.name == "tknk"


@pytest.mark.skip(reason="Not implemented")
@pytest.mark.parametrize("input, expected", [("", "")])
def test_answer_example1(input, expected):
    answer = aoc.part2(input)
    assert answer == expected
