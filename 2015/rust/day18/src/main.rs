use itertools::iproduct;
use std::iter::repeat;

fn parse(input: &str) -> [[u8; 100]; 100] {
    let mut grid = [[0; 100]; 100];
    for (y, line) in input.lines().enumerate() {
        for (x, c) in line.chars().enumerate() {
            grid[y][x] = match c {
                '#' => 1,
                _ => 0,
            };
        }
    }
    grid
}

fn step(grid: [[u8; 100]; 100], part2: bool) -> [[u8; 100]; 100] {
    let mut new_grid = [[0; 100]; 100];
    for (y, x) in iproduct!(0..100, 0..100) {
        let mut nei = 0;
        for (dy, dx) in iproduct!(-1..=1, -1..=1) {
            if dy == 0 && dx == 0 {
                continue;
            }
            let ny = y as i16 + dy;
            let nx = x as i16 + dx;
            if ny < 0 || ny >= 100 || nx < 0 || nx >= 100 {
                continue;
            }
            nei += grid[ny as usize][nx as usize];
        }
        match grid[y][x] {
            1 => {
                if nei == 2 || nei == 3 {
                    new_grid[y][x] = 1;
                }
            }
            0 => {
                if nei == 3 {
                    new_grid[y][x] = 1;
                }
            }
            _ => unreachable!(),
        }
    }
    if part2 {
        new_grid[0][0] = 1;
        new_grid[0][99] = 1;
        new_grid[99][0] = 1;
        new_grid[99][99] = 1;
    }
    new_grid
}

fn main() {
    let grid = parse(include_str!("input.txt"));

    let part1 = repeat(grid).take(100).fold(grid, |acc, _| step(acc, false));
    println!(
        "Part 1: {}",
        part1.iter().flatten().filter(|&&x| x == 1).count()
    );

    let part2 = repeat(grid).take(100).fold(grid, |acc, _| step(acc, true));
    println!(
        "Part 2: {}",
        part2.iter().flatten().filter(|&&x| x == 1).count()
    );
}
