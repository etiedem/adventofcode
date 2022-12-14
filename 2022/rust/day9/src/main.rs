use std::{ops::{AddAssign, Sub, SubAssign}, collections::HashSet};

fn parse_data(data: &str) -> Vec<Vec<&str>> {
    data.lines()
        .map(|line| line.split_whitespace().collect())
        .collect()
}

#[derive(Debug, Clone, PartialEq, Eq, Copy, Hash)]
struct Coord(i32, i32);

impl AddAssign for Coord {
    fn add_assign(&mut self, other: Self) {
        *self = Self ( self.0 + other.0, self.1 + other.1 )
    }
}
impl SubAssign for Coord {
    fn sub_assign(&mut self, other: Self) {
        *self = Self ( self.0 - other.0, self.1 - other.1 )
    }
}
impl Sub for &Coord {
    type Output = Coord;
    fn sub(self, other: &Coord) -> Self::Output {
        Coord (self.0 - other.0, self.1 - other.1)
    }
}

fn move_tail(head: Coord, tail: &mut Coord) -> HashSet<Coord> {
    let mut map = HashSet::new();
    let mut diff = &head.clone() - &tail.clone();
    if (diff.0.abs() > 1 && diff.1.abs() != 0) || (diff.1.abs() > 1 && diff.0.abs() != 0) {
        let x = if diff.0 > 0 { 1 } else { -1 };
        let y = if diff.1 > 0 { 1 } else { -1 };
        *tail = Coord(tail.0 + x, tail.1 + y);
        diff = &head.clone() - &tail.clone();
        map.insert(*tail);
    }
    if diff.0.abs() > 1 {
        let x = if diff.0 > 0 { 1 } else { -1 };

        for _ in 0..diff.0.abs()-1 {
            *tail = Coord(tail.0 + x, tail.1);
            map.insert(*tail);
        }
    }
    if diff.1.abs() > 1 {
        let y = if diff.1 > 0 { 1 } else { -1 };

        for _ in 0..diff.1.abs()-1 {
            *tail = Coord(tail.0, tail.1 + y);
            map.insert(*tail);
        }
    }
    map
}

fn run(moves: Vec<Vec<&str>>) -> u32 {
    let mut head = Coord(0,0);
    let mut tail = Coord(0,0);
    let mut seen:HashSet<Coord> = HashSet::new();
    seen.insert(Coord(0,0));

    for m in moves {
        let (dir, steps) = (m[0], m[1].parse::<i32>().unwrap());
        let update = match dir {
            "R" => {head += Coord(steps,0); move_tail(head, &mut tail)},
            "L" => {head += Coord(-steps,0); move_tail(head, &mut tail)},
            "U" => {head += Coord(0,steps); move_tail(head, &mut tail)},
            "D" => {head += Coord(0,-steps); move_tail(head, &mut tail)},
            _ => panic!("Unknown Movement")
        };
        seen.extend(&update);
    }
    seen.len() as u32
}
fn main() {
    let data = include_str!("data.txt");
    let moves = parse_data(data);
    let count = run(moves);
    println!("PART1: {} ", count);
}
