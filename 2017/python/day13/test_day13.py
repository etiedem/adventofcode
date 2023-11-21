import pathlib
import pytest
import day13 as aoc

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example():
    puzzle_input = PUZZLE_DIR / "example.txt"
    return aoc.get_data(puzzle_input)


def test_parse_example(example):
    game = aoc.Game.from_str(example)
    game.run()
    print(game)
    answer = game.severity
    assert answer == 24
