use std::collections::HashSet;

use nom::bytes::complete::{tag, take_until};
use nom::combinator::rest;
use nom::sequence::preceded;
use nom::IResult;

#[derive(Debug, PartialEq, Eq, Hash)]
struct Position(i32, i32);

#[derive(Debug)]
struct Sensor {
    pos: Position,
    beacon: Position,
    manhattan: i32,
}

impl Sensor {
    fn search_fill(&self, pos: i32) -> Vec<Position> {
        let mut count = 1;
        let mut result = Vec::new();
        let mut current = Position(self.pos.0, self.pos.1 + self.manhattan);
        while count != 0 {
            if current.1 == pos {
                for x in 0..count {
                    result.push(Position(current.0 - x, current.1));
                    result.push(Position(current.0 + x, current.1));
                }
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

fn main() {
    let data = parse_data(include_str!("data.txt"));
    let line = 2_000_000;
    let mut count = data
        .iter()
        .flat_map(|x| x.search_fill(line))
        .collect::<HashSet<Position>>()
        .len();
    count -= data
        .iter()
        .map(|x| &x.beacon)
        .filter(|x| x.1 == line)
        .collect::<HashSet<_>>()
        .len();

    println!("PART 1: {}", count);
}
