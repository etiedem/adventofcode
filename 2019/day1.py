from rich import print


def get_data(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        return list(map(int, f.read().splitlines()))


def get_fuel(mass):
    return mass // 3 - 2


def get_complex_fuel(mass):
    new_mass = mass
    fuel = 0
    while new_mass > 0:
        new_mass = get_fuel(new_mass)
        if new_mass < 0:
            break
        fuel += new_mass
    return fuel


def main():
    data = get_data('day1.txt')
    print(f'PART 1: {sum(get_fuel(x) for x in data)}')
    print(f'PART 2: {sum(get_complex_fuel(x) for x in data)}')


if __name__ == "__main__":
    main()
