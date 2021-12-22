from rich import print


def get_data(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        return [[[set(i)
                  for i in item.split()]
                 for item in line.split(' | ')]
                for line in f.readlines()]


def get_number(data, keys):
    output = ''
    for d in data:
        for k, v in keys.items():
            if d == v:
                output += k
                continue
    return int(output)


def get_keys_and_remaining(data):
    keys, fives, sixes = {}, [], []
    for d in data:
        match len(d):
            case 5:
                fives.append(d)
            case 6:
                sixes.append(d)
            case 2:
                keys['1'] = d
            case 4:
                keys['4'] = d
            case 3:
                keys['7'] = d
            case 7:
                keys['8'] = d
    return keys, fives, sixes


def main():
    num = 0
    data = get_data('day8.txt')
    for signal, output in data:
        signal = sorted(signal, key=len)
        keys, fives, sixes = get_keys_and_remaining(signal)
        keys['3'] = next(x for x in fives if not keys['1'] - x)
        fives.remove(keys['3'])
        keys['9'] = keys['3'] | keys['4']
        sixes.remove(keys['9'])
        keys['6'] = next(x for x in sixes if not (keys['4'] - keys['1']) - x)
        sixes.remove(keys['6'])
        keys['0'] = sixes.pop()
        keys['5'] = next(x for x in fives if len(keys['6'] - x) == 1)
        fives.remove(keys['5'])
        keys['2'] = fives.pop()
        num += get_number(output, keys)
    print(num)


if __name__ == "__main__":
    main()
