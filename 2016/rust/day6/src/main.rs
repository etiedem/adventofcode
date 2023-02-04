use counter::Counter;

fn parse_data(input: &str) -> Vec<String> {
    let mut output: Vec<String> = Vec::new();

    for _ in 0..input.lines().next().unwrap().len() {
        output.push(String::new());
    }

    for line in input.lines() {
        for (idx, c) in line.chars().enumerate() {
            output[idx].push(c);
        }
    }
    output
}

fn solve(input: &Vec<String>, most: bool) -> String {
    let mut output = String::new();
    for x in input {
        let common = x.chars().collect::<Counter<_>>().most_common();
        if most {
            output.push(common[0].0);
        } else {
            output.push(common[common.len() - 1].0)
        }
    }
    output
}

fn main() {
    let data = parse_data(include_str!("input.txt"));
    println!("Part 1: {:#?}", solve(&data, true));
    println!("Part 2: {:#?}", solve(&data, false));
}
