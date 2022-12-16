use std::{collections::HashSet, ops::{Sub, Add, AddAssign}};

#[macro_use] extern crate maplit;

#[derive(Debug, Clone)]
struct Segment {
    x: i32,
    y: i32,
    seen: HashSet<(i32, i32)>,
}

impl Segment {
    fn new() -> Self {
        Self { x: 0, y: 0, seen: hashset!{ (0,0) } }
    }
    fn follow(&mut self, other: &Self, idx: i32) {
        let diff = other - self;
        let distance = if idx == 0 { 0 } else { 1 };
        if diff.x.abs() > distance || diff.y.abs() > distance {
            let x = if diff.x > 0 { 1 } else if diff.x < 0 { -1 } else { 0 };
            let y = if diff.y > 0 { 1 } else if diff.y < 0 { -1 } else { 0 };
            self.x += x;
            self.y += y;
            self.seen.insert((self.x, self.y));
        }
    }
}

impl PartialEq for Segment {
    fn eq(&self, other: &Self) -> bool {
        self.x == other.x && self.y == other.y
    }
}
impl AddAssign for Segment {
    fn add_assign(&mut self, other: Self) {
    *self = Self{x:self.x + other.x, y:self.y + other.y, seen: self.seen.clone()}
    }
}
impl Add for &Segment {
    type Output = Segment;
    fn add(self, other: &Segment) -> Self::Output {
        Segment{x:self.x + other.x, y:self.y + other.y, seen: self.seen.clone()}
    }
}
impl Sub for &Segment {
    type Output = Segment;
    fn sub(self, other: &Segment) -> Self::Output {
        Segment{x:self.x - other.x, y:self.y - other.y, seen: self.seen.clone()}
    }
}

fn parse_data(data: &str) -> Vec<Vec<&str>> {
    data.lines()
        .map(|line| line.split_whitespace().collect())
        .collect()
}

fn get_end(head: &Segment, dir:&str, dist:i32) -> Segment {
    match dir {
        "U" => head + &Segment{x:0, y:dist , seen: hashset!{}},
        "D" => head + &Segment{x:0, y:-dist, seen: hashset!{}},
        "L" => head + &Segment{x:-dist, y:0, seen: hashset!{}},
        "R" => head + &Segment{x:dist as i32, y:0, seen: hashset!{}},
        _ => panic!("Invalid direction"),
    }
}

fn run(data: &Vec<Vec<&str>>, segments: usize) -> usize {
    let mut segments = vec![Segment::new(); segments];
    for d in data {
        let (dir, dist) = (d[0], d[1].parse::<i32>().unwrap());
        let end = get_end(&segments[0], dir, dist);
        let mut prev = end.clone();
        while segments[0] != end {
            for idx in 0..segments.len() {
                segments[idx].follow(&prev, idx as i32);
                prev = segments[idx].clone();
            }
            prev = end.clone();
        }
    }
    segments[segments.len()-1].seen.len()
}

fn main() {
    let data = parse_data(include_str!("data.txt"));
    println!("PART1: {}", run(&data, 2));
    println!("PART2: {}", run(&data, 10));
}
