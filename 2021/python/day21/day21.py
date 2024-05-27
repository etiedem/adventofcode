from dataclasses import dataclass

from rich import print


@dataclass
class Dice:
    sides: int
    rolls: int = 0

    def roll(self):
        answer = self.rolls % self.sides + 1, (self.rolls + 1) % self.sides + 1, (
            self.rolls + 2
        ) % self.sides + 1
        self.rolls += 3
        return answer


@dataclass
class Player:
    position: int
    score: int = 0

    def move(self, dice):
        roll = dice.roll()
        moves = sum(roll)
        self.position += moves
        self.position %= 10
        self.score += self.position if self.position != 0 else 10


def play(players, dice):
    while True:
        for p in players:
            p.move(dice)
            if p.score >= 1000:
                return


def get_data(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        return f.read().split()[4::5]


def main():
    data = get_data('day21.txt')
    players = [Player(int(position)) for position in data]
    dice = Dice(100)
    play(players, dice)
    print(min(x.score for x in players) * dice.rolls)


if __name__ == "__main__":
    main()
