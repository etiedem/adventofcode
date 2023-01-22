use std::collections::HashMap;

fn part1(data: &str) -> u32 {
    let mut houses: HashMap<(i32, i32), u32> = HashMap::new();
    let mut cx = 0;
    let mut cy = 0;
    houses.insert((cx, cy), 1);
    houses = data.chars().fold(houses, |mut houses, c| {
        let (x, y) = match c {
            '^' => (0, 1),
            'v' => (0, -1),
            '>' => (1, 0),
            '<' => (-1, 0),
            _ => (0, 0),
        };
        cx += x;
        cy += y;
        *houses.entry((cx, cy)).or_insert(0) += 1;
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
        let (x, y) = match c {
            '^' => (0, 1),
            'v' => (0, -1),
            '>' => (1, 0),
            '<' => (-1, 0),
            _ => (0, 0),
        };

        if i % 2 == 0 {
            current = &mut santa;
        } else {
            current = &mut robot;
        }
        current.0 += x;
        current.1 += y;
        *houses.entry(*current).or_insert(0) += 1;
    }
    houses.len() as u32
}

fn main() {
    let data = include_str!("input.txt");

    println!("Part 1: {}", part1(data));
    println!("Part 2: {}", part2(data));
}
