use std::fs::File;
use std::io::Read;
#[derive(Debug, Copy, Clone, PartialEq)]
struct Interval {
    start: u32,
    end: u32,
}

fn fully_contains(slf: &Interval, other: &Interval) -> bool {
    other.start >= slf.start && other.end <= slf.end
}

fn contains(slf: &Interval, other: &Interval) -> bool {
    (slf.start ..=slf.end).any(|x| (other.start ..=other.end).contains(&x))
}

fn get_data(filename: &str) -> String {
    let mut file = File::open(filename).expect("file not found");
    let mut contents = String::new();
    file.read_to_string(&mut contents).expect("something went wrong reading the file");
    contents
}

fn parse_data(data: String) -> Vec<Vec<Interval>>  {

    data.split_whitespace()
        .map(|line|
            line.split(',').
                map(|pair|
                    {
                        let mut iter = pair.split('-');
                        let start = iter.next().unwrap().parse::<u32>().unwrap();
                        let end = iter.next().unwrap().parse::<u32>().unwrap();
                        Interval{start, end}
                    }
                ).collect()
        ).collect()
}



fn part1(data: &Vec<Vec<Interval>>) -> u32 {
    let mut count = 0;
    for pair in data {
        let (a, b) = (&pair[0], &pair[1]);
        if fully_contains(a, b) || fully_contains(b, a) {
            count += 1;
        }
    }
    count
}

fn part2(data: &Vec<Vec<Interval>>) -> u32 {
    let mut count = 0;
    for pair in data {
        let (a, b) = (&pair[0], &pair[1]);
        if contains(a, b) || contains(b, a) {
            count += 1;
        }
    }
    count
}

fn main() {
    let data = parse_data(get_data("data.txt"));
    println!("PART1: {:?}", part1(&data));
    println!("PART2: {:?}", part2(&data));
}
