use std::collections::HashSet;

#[derive(Debug)]
enum Instr {
    Left(i32),
    Right(i32),
}

impl Instr {
    fn execute(&self, pos: &Pos) -> Pos {
        match self {
            Instr::Left(x) => {
                let mut degree = (pos.2 - 90) % 360;
                if degree < 0 {
                    degree += 360;
                }
                let new_pos = self.step(&degree, x);
                Pos(pos.0 + new_pos.0, pos.1 + new_pos.1, degree)
            }
            Instr::Right(x) => {
                let mut degree = (pos.2 + 90) % 360;
                if degree < 0 {
                    degree += 360;
                }
                let new_pos = self.step(&degree, x);
                Pos(pos.0 + new_pos.0, pos.1 + new_pos.1, degree)
            }
        }
    }

    fn step(&self, degree: &i32, amount: &i32) -> (i32, i32) {
        match degree {
            90 => (0, *amount),
            180 => (*amount, 0),
            270 => (0, (-amount)),
            0 => ((-amount), 0),
            _ => unreachable!("bad degree: {degree}"),
        }
    }
}

impl From<&str> for Instr {
    fn from(value: &str) -> Self {
        let (dir, rest) = value.split_at(1);
        match dir {
            "R" => Instr::Right(rest.parse().unwrap()),
            "L" => Instr::Left(rest.parse().unwrap()),
            _ => unreachable!(),
        }
    }
}

#[derive(Debug, Clone)]
struct Pos(i32, i32, i32);

fn get_instr(input: &str) -> Vec<Instr> {
    input.split(", ").map(Instr::from).collect()
}

fn expand_pos(old: &Pos, new: &Pos) -> Vec<(i32, i32)> {
    let mut set: Vec<(i32, i32)> = Vec::new();
    let Pos(mut x1, mut y1, _) = old;
    let Pos(x2, y2, _) = new;
    while &x1 != x2 || &y1 != y2 {
        if &x1 < x2 {
            x1 += 1;
        }
        if &x1 > x2 {
            x1 -= 1;
        }
        if &y1 < y2 {
            y1 += 1;
        }
        if &y1 > y2 {
            y1 -= 1;
        }
        set.push((x1, y1));
    }
    set
}

fn solve(pos: &Pos, directions: Vec<Instr>) -> (i32, i32) {
    let mut current = pos.clone();
    let mut seen: HashSet<(i32, i32)> = HashSet::new();
    let mut second: (i32, i32) = (0, 0);
    seen.insert((0, 0));

    for dir in directions {
        let new_pos = dir.execute(&current);
        let new_seen = expand_pos(&current, &new_pos);
        if second == (0, 0) {
            for item in &new_seen {
                if seen.contains(item) {
                    second = *item;
                    break;
                }
            }
        }
        seen.extend(new_seen);
        current = new_pos;
    }
    let answer = current.0.abs() + current.1.abs();
    let answer2 = second.0.abs() + second.1.abs();
    (answer, answer2)
}

fn main() {
    let data = include_str!("input.txt").trim();
    let directions = get_instr(data);
    let pos = Pos(0, 0, 90);
    let (part1, part2) = solve(&pos, directions);
    println!("Part 1: {:#?}", part1);
    println!("Part 2: {:#?}", part2);
}
