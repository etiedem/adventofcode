use std::{
    collections::HashSet,
    ops::{AddAssign, Sub, SubAssign, Add},
};

fn parse_data(data: &str) -> Vec<Vec<&str>> {
    data.lines()
        .map(|line| line.split_whitespace().collect())
        .collect()
}

#[derive(Debug, Clone, PartialEq, Eq, Copy, Hash)]
struct Coord(i32, i32);

impl AddAssign for Coord {
    fn add_assign(&mut self, other: Self) {
        *self = Self(self.0 + other.0, self.1 + other.1)
    }
}
impl SubAssign for Coord {
    fn sub_assign(&mut self, other: Self) {
        *self = Self(self.0 - other.0, self.1 - other.1)
    }
}
impl Add for &Coord {
    type Output = Coord;
    fn add(self, other: &Coord) -> Self::Output {
        Coord(self.0 + other.0, self.1 + other.1)
    }
}
impl Sub for &Coord {
    type Output = Coord;
    fn sub(self, other: &Coord) -> Self::Output {
        Coord(self.0 - other.0, self.1 - other.1)
    }
}

fn move_segment(prev: &Coord, cur: &mut Coord, head: bool) -> HashSet<Coord> {
    let mut map = HashSet::new();
    let mut diff = &prev.clone() - &cur.clone();
    let distance = if head { 0 } else { 1 };
    while diff.0.abs() > distance || diff.1.abs() > distance {
        let x = if diff.0 > 0 { 1 } else if diff.0 < 0 { -1 } else { 0 };
        let y = if diff.1 > 0 { 1 } else if diff.1 < 0 { -1 } else { 0 };
        *cur = Coord(cur.0 + x, cur.1 + y);
        diff = &prev.clone() - &cur.clone();
        map.insert(*cur);
    }
    map
}

fn move_all(end: Coord, segments: &mut Vec<Coord>) -> HashSet<Coord> {
    let mut map = HashSet::new();
    let mut prev = end;
    let mut new_segments = Vec::new();

    for (count, mut segment) in (0..segments.len()).zip(segments) {
        map = move_segment(&prev, &mut segment, count==0);
        prev = *segment;
        new_segments.push(*segment);
    }
    map
}

fn run(moves: &Vec<Vec<&str>>, num_seg: u32) -> u32 {
    let mut segments = vec![Coord(0, 0); num_seg as usize];
    let mut seen: HashSet<Coord> = HashSet::new();
    seen.insert(Coord(0, 0));

    for m in moves {
        let (dir, steps) = (m[0], m[1].parse::<i32>().unwrap());
        let update = match dir {
            "R" => { let end = &segments[0] + &Coord(steps, 0); move_all(end, &mut segments) }
            "L" => { let end = &segments[0] + &Coord(-steps,0); move_all(end, &mut segments) },
            "U" => { let end = &segments[0] + &Coord(0,steps);  move_all(end, &mut segments) },
            "D" => { let end = &segments[0] + &Coord(0,-steps); move_all(end, &mut segments) },
            _ => panic!("Unknown Movement"),
        };
        seen.extend(&update);
    }
    seen.len() as u32
}
fn main() {
    let data = include_str!("data.txt");
    let moves = parse_data(data);
    println!("PART1: {} ", run(&moves, 2));
    println!("PART2: {} ", run(&moves, 10));
}

// your answer is too low
// You guessed 2345
