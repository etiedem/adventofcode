from rich import print


def get_data(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        return [x.strip().split('\n') for x in f.read().split('\n\n')]


def process_cards(cards):
    return [[list(map(int, line.split())) for line in card] for card in cards]


def mark_cards(cards, d):
    for card in cards:
        for line in card:
            for idx, num in enumerate(line):
                if num == d:
                    line[idx] = 'x'


def get_column(pos, card):
    return [line[pos] for line in card]


def check_cards(cards, d):
    for idx, card in enumerate(cards):
        for line in card:
            if all(num == 'x' for num in line):
                yield idx

    length = len(cards[0]) if cards else 0
    for idx, card in enumerate(cards):
        for pos in range(length):
            if all(num == 'x' for num in get_column(pos, card)):
                yield idx


def get_score(card, d):
    result = 0
    for line in card:
        for num in line:
            if num == 'x':
                continue
            result += num
    return result * d


def play_game(draw, cards):
    results = []
    for d in draw:
        mark_cards(cards, d)
        for idx in check_cards(cards, d):
            results.append([cards.pop(idx), d])
    return results[-1]


def main():
    data = get_data(r'day4.txt')
    draw = list(map(int, data[0][0].split(',')))
    cards = process_cards(data[1:])
    winner = play_game(draw, cards)
    print(get_score(*winner))


if __name__ == "__main__":
    main()
