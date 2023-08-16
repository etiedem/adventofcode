#[derive(Debug, Default, PartialEq, PartialOrd, Eq, Ord)]
struct Deer {
    cur_dist: u32,
    name: String,
    dist_per_second: u32,
    dist_time: u32,
    rest_time: u32,
    total_time: u32,
    points: u32,
}

impl From<&str> for Deer {
    fn from(input: &str) -> Deer {
        let words: Vec<_> = input.split_whitespace().collect();
        Deer {
            name: words[0].to_string(),
            dist_per_second: words[3].parse().unwrap(),
            dist_time: words[6].parse().unwrap(),
            rest_time: words[13].parse().unwrap(),
            ..Default::default()
        }
    }
}

impl Deer {
    fn step(&mut self) {
        self.total_time += 1;
        let move_cycles = self.total_time / (self.dist_time + self.rest_time);
        let mut cur_dist = self.dist_per_second * self.dist_time * move_cycles;
        let time_left = self.total_time - (move_cycles * (self.dist_time + self.rest_time));
        if time_left >= self.dist_time {
            cur_dist += self.dist_per_second * self.dist_time;
        } else {
            cur_dist += self.dist_per_second * time_left;
        }
        self.cur_dist = cur_dist;
    }
}

fn step(deer: &mut [Deer], steps: u32) {
    for _ in 0..steps {
        for d in deer.iter_mut() {
            d.step();
        }
        let largest = deer.iter().max().unwrap().cur_dist;
        for d in deer.iter_mut() {
            if d.cur_dist == largest {
                d.points += 1;
            }
        }
    }
}

fn main() {
    let data = include_str!("input.txt");
    let mut deer: Vec<Deer> = data.lines().map(|line| line.into()).collect();
    step(&mut deer, 2503);

    let p1 = deer.iter().max().unwrap();
    println!("Part 1: {}", p1.cur_dist);

    let p2 = deer.iter().max_by_key(|x| x.points).unwrap();
    println!("Part 2: {}", p2.points);
}
