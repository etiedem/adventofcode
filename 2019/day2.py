from copy import deepcopy

from rich import print


def get_data(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        return list(map(int, f.read().strip().split(',')))


def process_op(op_sequence):
    new_op = deepcopy(op_sequence)
    for idx in range(0, len(new_op) - 4, 4):
        op, num1, num2, store = new_op[idx:idx + 4]
        if op == 1:
            new_op[store] = new_op[num1] + new_op[num2]
        elif op == 2:
            new_op[store] = new_op[num1] * new_op[num2]
        elif op == 99:
            break
    return new_op


def find(value, data):
    for noun in range(99):
        for verb in range(99):
            new_data = deepcopy(data)
            new_data[1] = noun
            new_data[2] = verb
            if process_op(new_data)[0] == value:
                return 100 * noun + verb


def main():
    data = get_data('day2.txt')
    data[1] = 12
    data[2] = 2
    print(f'PART 1: {process_op(data)[0]}')
    print(f'PART 2: {find(19690720, data)}')


if __name__ == "__main__":
    main()
