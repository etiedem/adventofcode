use std::{
    collections::{HashSet, HashMap},
    ops::{AddAssign, Sub, SubAssign, Add},
};

#[macro_use] extern crate maplit;

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

fn move_segment(prev: &Coord, cur: &mut Coord, head: bool) -> Coord {
    let diff = &prev.clone() - &cur.clone();
    let distance = if head { 0 } else { 1 };
    if diff.0.abs() > distance || diff.1.abs() > distance {
        let x = if diff.0 > 0 { 1 } else if diff.0 < 0 { -1 } else { 0 };
        let y = if diff.1 > 0 { 1 } else if diff.1 < 0 { -1 } else { 0 };
        *cur = Coord(cur.0 + x, cur.1 + y);
    }
    *cur
}

fn move_all(end: Coord, segments: &mut Vec<Coord>) -> HashMap<usize, HashSet<Coord>> {
    let mut map: HashMap<usize, HashSet<Coord>> = HashMap::new();
    let mut prev = end;
    let mut head_diff = &segments[0] - &end;

    while head_diff != Coord(0,0) {
        for idx in 0..segments.len() {
            let pos = move_segment(&prev, &mut segments[idx], idx==0);
            map.entry(idx)
                .and_modify(|e|  {e.insert(pos);})
                .or_insert(hashset![pos]);
            prev = segments[idx];
        }
        head_diff = &segments[0] - &end;
        prev = end;
    }
    map.clone()
}

fn merge(hash1: HashMap<usize, HashSet<Coord>>, hash2: HashMap<usize, HashSet<Coord>>) -> HashMap<usize, HashSet<Coord>> {
    let mut map: HashMap<usize, HashSet<Coord>> = HashMap::new();
    for (k, v) in hash1 {
        map.entry(k)
            .and_modify(|e|  {e.extend(&v);})
            .or_insert(v);
    }
    for (k, v) in hash2 {
        map.entry(k)
            .and_modify(|e|  {e.extend(&v);})
            .or_insert(v);
    }
    map
}

fn run(moves: &Vec<Vec<&str>>, num_seg: u32) -> u32 {
    let mut segments = vec![Coord(0, 0); num_seg as usize];
    let mut seen: HashMap<usize, HashSet<Coord>> = HashMap::new();
    let length = segments.len() - 1;

    for idx in 0..segments.len() {
        seen.insert(idx, hashset![Coord(0,0)]);
    }

    for m in moves {
        let (dir, steps) = (m[0], m[1].parse::<i32>().unwrap());
        let update = match dir {
            "R" => { let end = &segments[0] + &Coord(steps, 0); move_all(end, &mut segments) }
            "L" => { let end = &segments[0] + &Coord(-steps,0); move_all(end, &mut segments) },
            "U" => { let end = &segments[0] + &Coord(0,steps);  move_all(end, &mut segments) },
            "D" => { let end = &segments[0] + &Coord(0,-steps); move_all(end, &mut segments) },
            _ => panic!("Unknown Movement"),
        };
        seen = merge(seen, update);

    }
    seen.get(&length).unwrap().len() as u32
}
fn main() {
    let data = include_str!("data.txt");
    let moves = parse_data(data);
    println!("PART1: {} ", run(&moves, 2));
    println!("PART2: {} ", run(&moves, 10));
}
