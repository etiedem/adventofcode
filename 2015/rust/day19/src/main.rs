use std::collections::{BinaryHeap, HashMap, HashSet};

#[derive(Clone, Eq, PartialEq)]
struct State {
    molecule: String,
    steps: usize,
}

impl Ord for State {
    fn cmp(&self, other: &Self) -> std::cmp::Ordering {
        if self.molecule.len() < other.molecule.len() {
            std::cmp::Ordering::Greater
        } else if self.molecule.len() > other.molecule.len() {
            std::cmp::Ordering::Less
        } else {
            std::cmp::Ordering::Equal
        }
    }
}

impl PartialOrd for State {
    fn partial_cmp(&self, other: &Self) -> Option<std::cmp::Ordering> {
        Some(self.cmp(other))
    }
}

fn parse(data: &str) -> HashMap<&str, &str> {
    let mut backward: HashMap<&str, &str> = HashMap::new();
    for line in data.lines() {
        let (key, value) = line.split_once(" => ").unwrap();
        backward.insert(value, key);
    }
    backward
}

fn replacement(molecule: &str, mapping: &HashMap<&str, &str>) -> HashSet<String> {
    let mut result = HashSet::new();
    for (key, value) in mapping {
        for (pos, _) in molecule.match_indices(value) {
            let mut new_molecule = molecule.to_owned();
            new_molecule.replace_range(pos..pos + value.len(), key);
            result.insert(new_molecule);
        }
    }
    result
}

fn find_molecule(molecule: &str, mapping: &HashMap<&str, &str>) -> usize {
    let mut queue = BinaryHeap::new();
    queue.push(State {
        molecule: molecule.to_owned(),
        steps: 0,
    });

    while let Some(candidate) = queue.pop() {
        if candidate.molecule == "e" {
            return candidate.steps;
        }
        for (key, value) in mapping {
            if let Some(pos) = candidate.molecule.find(key) {
                let mut new = candidate.molecule.clone();
                new.replace_range(pos..pos + key.len(), value);
                queue.push(State {
                    molecule: new,
                    steps: candidate.steps + 1,
                });
            }
        }
    }
    0
}

fn main() {
    let data = include_str!("input.txt");
    let (data, molecule) = data.split_once("\n\n").unwrap();
    let mapping = parse(data);

    let p1 = replacement(molecule, &mapping).len();
    println!("Part 1: {:#?}", p1);

    let p2 = find_molecule(molecule, &mapping);
    println!("Part 2: {:#?}", p2);
}
