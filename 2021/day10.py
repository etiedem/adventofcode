from rich import print


match_map = {']': '[', ')': '(', '}': '{', '>': '<'}


def get_data(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        return [list(line.strip()) for line in f.readlines()]


def is_corrupt(line):
    stack = []
    for item in line:
        if item in ('[', '(', '{', '<'):
            stack.append(item)
        elif stack[-1] == match_map.get(item):
            stack.pop()
        elif item == ')':
            return 3
        elif item == ']':
            return 57
        elif item == '}':
            return 1197
        elif item == '>':
            return 25137


def repair(line):
    stack = []
    for item in line:
        if item in ('[', '(', '{', '<'):
            stack.append(item)
        elif stack[-1] == match_map.get(item):
            stack.pop()

    result = 0
    stack.reverse()
    for item in stack:
        result *= 5
        if item == '(':
            result += 1
        elif item == '[':
            result += 2
        elif item == '{':
            result += 3
        elif item == '<':
            result += 4
        else:
            raise ValueError
    return result


def main():
    data = get_data('day10.txt')
    answer = sum(ans for line in data if (ans := is_corrupt(line)))
    print(f'PART 1: {answer}')

    completions = sorted([repair(line) for line in data if not is_corrupt(line)])
    print(f'PART 2: {completions[len(completions) // 2]}')


if __name__ == "__main__":
    main()
