#[derive(Debug, Copy, Clone, PartialEq)]
struct Interval {
    start: u32,
    end: u32,
}

impl Interval {
    fn fully_contains(self: &Interval, other: &Interval) -> bool {
        other.start >= self.start && other.end <= self.end
    }

    fn contains(self: &Interval, other: &Interval) -> bool {
        (self.start..=self.end).any(|x| (other.start..=other.end).contains(&x))
    }
}

fn parse_data(data: &str) -> Vec<Vec<Interval>> {
    data.split_whitespace()
        .map(|line| {
            line.split(',')
                .map(|pair| {
                    let mut iter = pair.split('-');
                    let start = iter.next().unwrap().parse::<u32>().unwrap();
                    let end = iter.next().unwrap().parse::<u32>().unwrap();
                    Interval { start, end }
                })
                .collect()
        })
        .collect()
}

fn part1(data: &Vec<Vec<Interval>>) -> u32 {
    let mut count = 0;
    for pair in data {
        let (a, b) = (&pair[0], &pair[1]);
        if a.fully_contains(b) || b.fully_contains(a) {
            count += 1;
        }
    }
    count
}

fn part2(data: &Vec<Vec<Interval>>) -> u32 {
    let mut count = 0;
    for pair in data {
        let (a, b) = (&pair[0], &pair[1]);
        if a.contains(b) || b.contains(a) {
            count += 1;
        }
    }
    count
}

fn main() {
    let data = parse_data(include_str!("data.txt"));
    println!("PART1: {:?}", part1(&data));
    println!("PART2: {:?}", part2(&data));
}
