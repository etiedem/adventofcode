use std::collections::HashMap;

fn move_pos(char: char, mut pos: (i32, i32)) -> (i32, i32) {
    let (x, y) = match char {
        '^' => (0, 1),
        'v' => (0, -1),
        '>' => (1, 0),
        '<' => (-1, 0),
        _ => (0, 0),
    };
    pos.0 += x;
    pos.1 += y;
    pos
}

fn part1(data: &str) -> u32 {
    let mut houses: HashMap<(i32, i32), u32> = HashMap::new();
    let mut santa = (0, 0);
    houses.insert(santa, 1);
    houses = data.chars().fold(houses, |mut houses, c| {
        santa = move_pos(c, santa);
        *houses.entry(santa).or_insert(0) += 1;
        houses
    });
    houses.len() as u32
}

fn part2(data: &str) -> u32 {
    let mut houses: HashMap<(i32, i32), u32> = HashMap::new();
    let mut santa = (0, 0);
    let mut robot = (0, 0);
    let mut current: &mut (i32, i32);
    houses.insert(santa, 2);

    for (i, c) in data.chars().enumerate() {
        if i % 2 == 0 {
            current = &mut santa;
        } else {
            current = &mut robot;
        }
        *current = move_pos(c, *current);
        *houses.entry(*current).or_insert(0) += 1;
    }
    houses.len() as u32
}

fn main() {
    let data = include_str!("input.txt");

    println!("Part 1: {}", part1(data));
    println!("Part 2: {}", part2(data));
}
