use itertools::Itertools;
use itertools::MinMaxResult::{MinMax, OneElement};

use nom::bytes::complete::{tag, take_until};
use nom::combinator::rest;
use nom::sequence::preceded;
use nom::IResult;

#[derive(Debug)]
struct Position(i32, i32);

#[derive(Debug)]
struct Sensor {
    pos: Position,
    beacon: Position,
    manhattan: i32,
}

impl Sensor {
    fn search_area(&self) -> Vec<Position> {
        vec![
            Position(self.pos.0, self.pos.1 + self.manhattan),
            Position(self.pos.0 + self.manhattan, self.pos.1),
            Position(self.pos.0, self.pos.1 - self.manhattan),
            Position(self.pos.0 - self.manhattan, self.pos.1),
        ]
    }

    fn search_fill(&self) -> Vec<Position> {
        let mut count = 1;
        let mut result = Vec::new();
        let mut current = Position(self.pos.0, self.pos.1 + self.manhattan);
        while count != 0 {
            for x in 0..count {
                result.push(Position(current.0 - x, current.1));
                result.push(Position(current.0 + x, current.1));
            }
            if current.1 > self.pos.1 {
                count += 1;
            } else {
                count -= 1;
            }
            current.1 -= 1;
        }
        result
    }
}

#[derive(Debug, Clone, PartialEq, Eq)]
enum Item {
    Sensor,
    Beacon,
    Air,
    Searched,
}

#[derive(Debug)]
struct Map {
    grid: Vec<Vec<Item>>,
    height: usize,
    width: usize,
    ymin: i32,
}

impl Map {
    fn show(&self) {
        for row in &self.grid {
            for item in row {
                let i = match item {
                    Item::Air => ".",
                    Item::Beacon => "B",
                    Item::Sensor => "S",
                    Item::Searched => "#",
                };
                print!("{i}");
            }
            println!()
        }
    }

    fn new(data: &Vec<Sensor>) -> Self {
        let (xmin, xmax, ymin, ymax) = get_bounds(data);
        let height = (ymax - ymin) as usize;
        let width = (xmax - xmin) as usize;

        let mut grid = vec![vec![Item::Air; width + 1]; height + 1];
        for sensor in data {
            for search in sensor.search_fill() {
                grid[(search.1 - ymin) as usize][(search.0 - xmin) as usize] = Item::Searched;
            }
            grid[(sensor.pos.1 - ymin) as usize][(sensor.pos.0 - xmin) as usize] = Item::Sensor;
            grid[(sensor.beacon.1 - ymin) as usize][(sensor.beacon.0 - xmin) as usize] =
                Item::Beacon;
        }

        Map {
            grid,
            height,
            width,
            ymin,
        }
    }
}

fn parse_position(input: &str) -> IResult<&str, Position> {
    let (input, _) = take_until("x=")(input)?;
    let (input, x) = preceded(tag("x="), take_until(","))(input)?;
    let (input, _) = take_until("y=")(input)?;
    let (input, y) = preceded(tag("y="), rest)(input)?;
    let x = x.parse().unwrap();
    let y = y.parse().unwrap();
    Ok((input, Position(x, y)))
}

fn parse_sensor(input: &str) -> IResult<&str, Sensor> {
    let (second, first) = take_until(": ")(input)?;
    let (_, fxy) = parse_position(first)?;
    let (_, sxy) = parse_position(second)?;
    let manhattan = (&fxy.0 - &sxy.0).abs() + (&fxy.1 - &sxy.1).abs();
    Ok((
        input,
        Sensor {
            pos: fxy,
            beacon: sxy,
            manhattan,
        },
    ))
}

fn parse_data(data: &str) -> Vec<Sensor> {
    data.lines()
        .map(|line| parse_sensor(line).unwrap().1)
        .collect()
}

fn get_bounds(data: &Vec<Sensor>) -> (i32, i32, i32, i32) {
    let base = data
        .iter()
        .flat_map(|sensor| sensor.search_area())
        .collect::<Vec<_>>();

    let (xmin, xmax) = match base.iter().skip(1).step_by(2).map(|pos| pos.0).minmax() {
        MinMax(min, max) => (min, max),
        OneElement(x) => (x, x),
        _ => unreachable!(),
    };

    let (ymin, ymax) = match base.iter().step_by(2).map(|pos| pos.1).minmax() {
        MinMax(min, max) => (min, max),
        OneElement(x) => (x, x),
        _ => unreachable!(),
    };

    (xmin, xmax, ymin, ymax)
}

fn main() {
    let data = parse_data(include_str!("data.txt"));
    let map = Map::new(&data);
    // map.show();
    println!(
        "PART 1: {:?}",
        map.grid[(2_000_000 - map.ymin) as usize]
            .iter()
            .filter(|x| *x != &Item::Air)
            .filter(|x| *x != &Item::Beacon)
            .count()
    );
}
