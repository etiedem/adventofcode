use std::collections::HashMap;

fn parse(input: &str) -> Vec<HashMap<String, u16>> {
    input
        .lines()
        .map(|line| {
            let line = line.replacen(':', ",", 1);
            let line = line.replacen(' ', ":", 1);
            let line = line.replace(' ', "");
            line.split(',')
                .map(|pair| {
                    let (key, value) = pair.split_once(':').unwrap();
                    (key.to_string(), value.parse().unwrap())
                })
                .collect()
        })
        .collect()
}

fn part1(aunt: &HashMap<String, u16>, clue: &HashMap<String, u16>) -> bool {
    for (key, value) in aunt {
        if key == "Sue" {
            continue;
        }
        if clue.get(key) != Some(value) {
            return false;
        }
    }
    true
}

fn part2(aunt: &HashMap<String, u16>, clue: &HashMap<String, u16>) -> bool {
    for (key, value) in aunt {
        if key == "Sue" {
            continue;
        } else if key == "cats" || key == "trees" {
            if clue.get(key) >= Some(value) {
                return false;
            }
        } else if key == "pomeranians" || key == "goldfish" {
            if clue.get(key) <= Some(value) {
                return false;
            }
        } else if clue.get(key) != Some(value) {
            return false;
        }
    }
    true
}
fn main() {
    let data = include_str!("input.txt");
    let aunts = parse(data);
    let aunt_clue = HashMap::from([
        ("children".to_owned(), 3),
        ("cats".to_owned(), 7),
        ("samoyeds".to_owned(), 2),
        ("pomeranians".to_owned(), 3),
        ("akitas".to_owned(), 0),
        ("vizslas".to_owned(), 0),
        ("goldfish".to_owned(), 5),
        ("trees".to_owned(), 3),
        ("cars".to_owned(), 2),
        ("perfumes".to_owned(), 1),
    ]);

    let p1 = aunts
        .iter()
        .filter(|x| part1(x, &aunt_clue))
        .last()
        .unwrap();
    println!("Part 1: {:?}", p1.get("Sue").unwrap());

    let p2 = aunts
        .iter()
        .filter(|x| part2(x, &aunt_clue))
        .last()
        .unwrap();
    println!("Part 2: {:?}", p2.get("Sue").unwrap());
}
