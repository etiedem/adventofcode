import pathlib
import pytest
import day07 as aoc

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example():
    puzzle_input = PUZZLE_DIR / "example.txt"
    return aoc.get_data(puzzle_input)


@pytest.mark.parametrize(
    "input, expected",
    [
        ("AAAAA 1", aoc.HandType.FIVE_OF_A_KIND),
        ("AAAAK 1", aoc.HandType.FOUR_OF_A_KIND),
        ("AAKAK 1", aoc.HandType.FULL_HOUSE),
        ("AAQAK 1", aoc.HandType.THREE_OF_A_KIND),
        ("AAQKK 1", aoc.HandType.TWO_PAIR),
        ("AAQJK 1", aoc.HandType.PAIR),
        ("A2QJK 1", aoc.HandType.HIGH_CARD),
    ],
)
def test_answer_example(input, expected):
    answer = list(aoc.parse(input))[0]
    assert answer.htype == expected


@pytest.mark.parametrize(
    "input, expected",
    [
        ("AAAJA 1", aoc.HandType.FIVE_OF_A_KIND),
        ("AAJJA 1", aoc.HandType.FIVE_OF_A_KIND),
        ("AAJJJ 1", aoc.HandType.FIVE_OF_A_KIND),
        ("AJJJJ 1", aoc.HandType.FIVE_OF_A_KIND),
        ("AAAJK 1", aoc.HandType.FOUR_OF_A_KIND),
        ("AAJJK 1", aoc.HandType.FOUR_OF_A_KIND),
        ("AAQJK 1", aoc.HandType.THREE_OF_A_KIND),
        ("AJQJK 1", aoc.HandType.THREE_OF_A_KIND),
        ("AAKJK 1", aoc.HandType.FULL_HOUSE),
        ("A2QJK 1", aoc.HandType.PAIR),
    ],
)
def test_answer_example1(input, expected):
    answer = list(aoc.parse(input, True))[0]
    assert answer.htype == expected
