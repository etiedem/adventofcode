use itertools::Itertools;
use itertools::MinMaxResult::{MinMax, OneElement};
use std::str::FromStr;

#[derive(Debug)]
struct ParsePointError;

#[derive(Debug, Default, Clone, Ord, PartialOrd, PartialEq, Eq)]
struct Point(i32, i32);

impl FromStr for Point {
    type Err = ParsePointError;
    fn from_str(s: &str) -> Result<Self, Self::Err> {
        let (x, y) = s.split_once(',').ok_or(ParsePointError)?;
        Ok(Point(
            x.parse().map_err(|_| ParsePointError)?,
            y.parse().map_err(|_| ParsePointError)?,
        ))
    }
}

#[derive(Debug, Default, Eq, PartialEq, Clone)]
enum Item {
    #[default]
    Air,
    Rock,
    Sand,
    Generator,
}

#[derive(Debug, Default, Clone)]
struct Map {
    grid: Vec<Vec<Item>>,
    generator: Point,
    width: i32,
    length: i32,
    done: bool,
}

impl Map {
    fn show(self) {
        for row in self.grid {
            for item in row {
                let symbol = match item {
                    Item::Air => '.',
                    Item::Rock => '#',
                    Item::Sand => 'O',
                    Item::Generator => '+',
                };
                print!("{symbol}");
            }
            println!();
        }
    }

    fn check_bounds(&self, x: i32, y: i32) -> bool {
        x >= 0 && x <= self.width && y >= 0 && y < self.length
    }

    fn check_ground(&self, x: i32, y: i32) -> bool {
        if !self.check_bounds(x - 1, y) || !self.check_bounds(x, y - 1) {
            return false;
        }
        true
    }

    fn get_move(&self, point: &Point) -> Option<Point> {
        let moves = vec![(0, 1), (-1, 1), (1, 1)];
        for (x, y) in moves {
            let new_x = point.0 + x;
            let new_y = point.1 + y;
            if let Item::Air = self.grid[new_y as usize][new_x as usize] {
                return Some(Point(new_x, new_y));
            }
        }
        None
    }

    fn step(&mut self) {
        let mut current = Point(self.generator.0, self.generator.1 + 1);
        while let Some(next) = self.get_move(&current) {
            if self.check_bounds(next.0, next.1) {
                current = next;
            } else {
                self.done = true;
                return;
            }
        }
        if self.check_ground(current.0, current.1) {
            self.grid[current.1 as usize][current.0 as usize] = Item::Sand;
        }
    }
}

fn parse_data(data: &str) -> Vec<Vec<Point>> {
    data.lines()
        .map(|line| line.split(" -> ").map(|x| x.parse().unwrap()).collect())
        .collect()
}

fn fill_in_points(data: &Vec<Point>) -> Vec<Point> {
    let mut rock_path: Vec<Point> = Vec::new();
    let mut iter = data.iter();
    let mut current = iter.next().unwrap().to_owned();
    rock_path.push(current.clone());
    for point in iter {
        while current != *point {
            let newx = current.0 + (point.0 - current.0).signum();
            let newy = current.1 + (point.1 - current.1).signum();
            let new = Point(newx, newy);
            rock_path.push(new.clone());
            current = new.clone();
        }
    }
    rock_path
}

fn create_map(data: Vec<Vec<Point>>) -> Map {
    let iter = data.iter().flat_map(|x| x.iter());

    let (xmin, xmax) = match iter.clone().map(|point| point.0).minmax() {
        MinMax(min, max) => (min, max),
        OneElement(x) => (x, x),
        _ => unreachable!(),
    };
    let (_, ymax) = match iter.map(|point| point.1).minmax() {
        MinMax(min, max) => (min, max),
        OneElement(x) => (x, x),
        _ => unreachable!(),
    };
    let ymin = 0;
    let width = xmax - xmin;
    let length = 2 + ymax - ymin;

    let generator = Point(500 - xmin, 0);
    let rocks: Vec<Point> = data.iter().flat_map(fill_in_points).collect();
    let mut grid: Vec<Vec<Item>> = Vec::with_capacity((length) as usize);
    for y in 0..=length {
        let mut row: Vec<Item> = Vec::with_capacity((width) as usize);
        for x in 0..=width {
            if (x, y) == (generator.0, generator.1) {
                row.push(Item::Generator);
            } else if rocks.contains(&Point(x + xmin, y + ymin)) {
                row.push(Item::Rock);
            } else {
                row.push(Item::Air);
            }
        }
        grid.push(row);
    }
    Map {
        grid,
        generator,
        length,
        width,
        done: false,
    }
}

fn main() {
    let data = parse_data(include_str!("data.txt"));
    let mut grid = create_map(data);
    let mut count = 0;
    while !grid.done {
        grid.step();
        count += 1;
    }
    // grid.show();
    println!("PART 1: {}", count - 1);
}
