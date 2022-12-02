from enum import IntEnum

from rich import print


class CHOICE(IntEnum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


class RESULT(IntEnum):
    DRAW = 3
    WIN = 6
    LOSE = 0


RPS_HASH = {
    "A": CHOICE.ROCK,
    "B": CHOICE.PAPER,
    "C": CHOICE.SCISSORS,
    "X": CHOICE.ROCK,
    "Y": CHOICE.PAPER,
    "Z": CHOICE.SCISSORS,
}

RPS_RESULT_HASH = {
    "X": RESULT.LOSE,
    "Y": RESULT.DRAW,
    "Z": RESULT.WIN,
}


def get_data(filename):
    with open(filename, "r", encoding="utf-8") as f:
        for x in f:
            yield x.strip().split()


def check_game(player1, player2):
    p1 = RPS_HASH.get(player1)
    p2 = RPS_HASH.get(player2)

    if p1 == p2:
        return RESULT.DRAW + p2
    elif p2 == CHOICE.ROCK and p1 == CHOICE.SCISSORS:
        return RESULT.WIN + p2
    elif p2 == CHOICE.PAPER and p1 == CHOICE.ROCK:
        return RESULT.WIN + p2
    elif p2 == CHOICE.SCISSORS and p1 == CHOICE.PAPER:
        return RESULT.WIN + p2
    else:
        return RESULT.LOSE + p2


def set_game(player1, result):
    p1 = RPS_HASH.get(player1)
    r = RPS_RESULT_HASH.get(result)
    match r:
        case RESULT.WIN:
            match p1:
                case CHOICE.ROCK:
                    return r + CHOICE.PAPER
                case CHOICE.PAPER:
                    return r + CHOICE.SCISSORS
                case CHOICE.SCISSORS:
                    return r + CHOICE.ROCK
        case RESULT.LOSE:
            match p1:
                case CHOICE.ROCK:
                    return r + CHOICE.SCISSORS
                case CHOICE.PAPER:
                    return r + CHOICE.ROCK
                case CHOICE.SCISSORS:
                    return r + CHOICE.PAPER
        case _:
            return r + p1


def main():
    data = list(get_data(r"day2.txt"))
    print(f"PART1: {sum(check_game(*x) for x in data)}")
    print(f"PART2: {sum(set_game(*x) for x in data)}")


if __name__ == "__main__":
    main()
