use lazy_static::lazy_static;
use regex::Regex;
use std::fmt::Display;

#[derive(Debug)]
struct Ip {
    rest: Vec<String>,
    net: Vec<String>,
}

impl Display for Ip {
    fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        write!(f, "rest:\n")?;
        for r in &self.rest {
            write!(f, "{}\n", r)?;
        }
        write!(f, "nets:\n")?;
        for net in &self.net {
            write!(f, "{}\n", net)?;
        }
        write!(f, "")
    }
}

impl From<&str> for Ip {
    fn from(input: &str) -> Self {
        lazy_static! {
            static ref RE: Regex = Regex::new(r"\[(\w+)\]").unwrap();
        }
        let mut net = Vec::new();
        for capture in RE.captures_iter(input) {
            net.push(
                capture
                    .get(0)
                    .unwrap()
                    .as_str()
                    .trim_matches('[')
                    .trim_matches(']')
                    .to_string(),
            );
        }
        let rest = RE.split(input).map(String::from).collect();
        Ip {
            rest: rest,
            net: net,
        }
    }
}

impl Ip {
    fn check_abba(input: &str) -> bool {
        for item in input.chars().collect::<Vec<char>>().windows(4) {
            if item[0] == item[3] && item[1] == item[2] && item[0] != item[1] {
                return true;
            }
        }
        false
    }
    fn check_bab(input: &str, aba: &str) -> bool {
        for item in input.chars().collect::<Vec<char>>().windows(3) {
            if item[0] == aba.chars().nth(1).unwrap()
                && item[1] == aba.chars().nth(0).unwrap()
                && item[2] == aba.chars().nth(1).unwrap()
            {
                return true;
            }
        }
        false
    }
    fn check_aba(input: &str) -> Vec<String> {
        let mut result = Vec::new();
        for item in input.chars().collect::<Vec<char>>().windows(3) {
            if item[0] == item[2] && item[0] != item[1] {
                result.push(item.iter().collect());
            }
        }
        result
    }

    fn supports_ssl(&self) -> bool {
        for rest in &self.rest {
            for item in Ip::check_aba(rest) {
                for net in &self.net {
                    if Ip::check_bab(net, &item) {
                        return true;
                    }
                }
            }
        }
        false
    }

    fn supports_tls(&self) -> bool {
        for net in &self.net {
            if Ip::check_abba(net) {
                return false;
            }
        }
        for rest in &self.rest {
            if Ip::check_abba(rest) {
                return true;
            }
        }
        false
    }
}

fn tls(input: &Vec<Ip>) -> u32 {
    input.iter().filter(|x| x.supports_tls()).count() as u32
}

fn ssl(input: &Vec<Ip>) -> u32 {
    input.iter().filter(|x| x.supports_ssl()).count() as u32
}

fn main() {
    let data = include_str!("input.txt").trim();
    let ip: Vec<_> = data.lines().map(Ip::from).collect();
    println!("Part 1: {}", tls(&ip));
    println!("Part 2: {}", ssl(&ip));
}
