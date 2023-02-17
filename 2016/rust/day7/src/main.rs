use std::fmt::Display;

#[derive(Debug)]
struct Ip {
    left: String,
    right: String,
    net: String,
}

impl Display for Ip {
    fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        write!(
            f,
            "left:  {}\nright: {}\nnet:   {}",
            self.left, self.right, self.net
        )
    }
}

impl From<&str> for Ip {
    fn from(input: &str) -> Self {
        let (left, rest) = input.split_once('[').unwrap();
        let (net, right) = rest.split_once(']').unwrap();
        Ip {
            left: left.to_string(),
            right: right.to_string(),
            net: net.to_string(),
        }
    }
}

impl Ip {
    fn check(input: &str) -> bool {
        for item in input.chars().collect::<Vec<char>>().windows(4) {
            if item[0] == item[3] && item[1] == item[2] && item[0] != item[1] {
                return true;
            }
        }
        false
    }

    fn supports_tls(&self) -> bool {
        if !Ip::check(&self.net) && (Ip::check(&self.left) || Ip::check(&self.right)) {
            return true;
        }
        false
    }
}

fn solve(input: &str) -> u32 {
    input.lines().map(Ip::from).filter(Ip::supports_tls).count() as u32
}

fn main() {
    let data = include_str!("input.txt").trim();
    println!("Part 1: {}", solve(data));
}

// 157 is too high
