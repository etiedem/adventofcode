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
        let (x, y) = s.split_once(",").ok_or(ParsePointError)?;
        Ok(Point(
            x.parse().map_err(|_| ParsePointError)?,
            y.parse().map_err(|_| ParsePointError)?,
        ))
    }
}

#[derive(Debug, Default)]
enum Item {
    #[default]
    Air,
    Rock,
    Sand,
    Generator,
}

#[derive(Debug, Default)]
struct Grid(Vec<Vec<Item>>);

impl Grid {
    fn show(self) {
        for row in self.0 {
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

fn create_grid(data: Vec<Vec<Point>>) -> Grid {
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
    let rocks: Vec<Point> = data.iter().flat_map(fill_in_points).collect();
    let mut grid: Vec<Vec<Item>> = Vec::with_capacity((ymax - ymin) as usize);
    for y in 0..=ymax - ymin {
        let mut row: Vec<Item> = Vec::with_capacity((xmax - xmin) as usize);
        for x in 0..=xmax - xmin {
            if (x, y) == (500 - xmin, 0) {
                row.push(Item::Generator);
            } else if rocks.contains(&Point(x + xmin, y + ymin)) {
                row.push(Item::Rock);
            } else {
                row.push(Item::Air);
            }
        }
        grid.push(row);
    }
    Grid(grid)
}

fn main() {
    let data = parse_data(include_str!("data.txt"));
    let grid = create_grid(data);
    grid.show();
}
