from dataclasses import dataclass
from operator import attrgetter

from rich import print


def get_data(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        return [x.strip().split('\n') for x in f.read().split('\n\n')]


@dataclass
class Card:
    card: list[list[int]]
    solved: bool = False
    score: int = 0
    marks: int = 0
    draw: int = -1

    def mark(self, draw):
        for line in self.card:
            for idx, num in enumerate(line):
                if num == draw:
                    line[idx] = 'x'
                    self.marks += 1
                    self.draw = draw
                    return True

    def check(self):
        for line in self.card:
            if all(num == 'x' for num in line):
                self.solved = True
                self.calc_score()
                return True

        for pos in range(len(self.card)):
            if all(num == 'x' for num in self.get_column(pos)):
                self.solved = True
                self.calc_score()
                return True

    def calc_score(self):
        result = 0
        for line in self.card:
            for num in line:
                if num == 'x':
                    continue
                result += num
        self.score = result * self.draw

    def get_column(self, col):
        return [line[col] for line in self.card]

    @property
    def show(self):
        for line in self.card:
            for item in line:
                print(f'{str(item):>2s}', end=' ')
            print()


def main():
    draws_data, *card_data = get_data('day4.txt')
    draws = list(map(int, draws_data[0].split(',')))
    cards = [
        Card([list(map(int, line.split())) for line in card]) for card in card_data
    ]

    winners = []
    for draw in draws:
        for card in cards:
            if not card.solved and card.mark(draw) and card.marks > 4 and card.check():
                winners.append(card)

    print('PART 1:')
    winners[0].show
    print(f'score: {winners[0].score}')
    print()
    print('PART 2:')
    winners[-1].show
    print(f'score: {winners[-1].score}')


if __name__ == "__main__":
    main()
