
fn parse_crates(data: &str) -> Vec<Vec<char>> {
    let mut diagram = data.lines().rev();
    let length: usize = diagram.next()
                        .unwrap()
                        .split_whitespace()
                        .last()
                        .unwrap()
                        .parse()
                        .unwrap();
    let mut stacks: Vec<Vec<char>> = vec![vec![]; length];

    for row in diagram {
        for (i, c) in row.chars().skip(1).step_by(4).enumerate().filter(|&(_, c)| c != ' ') {
            stacks[i].insert(0, c);
        }
    }

    stacks
}

fn parse_moves(data: &str) -> Vec<Vec<u8>> {
    data
        .lines()
        .map(|x| x.split_whitespace()
            .skip(1)
            .step_by(2)
            .map(|s| s.parse().unwrap())
            .collect()
        ).collect()
}

fn part1(mut stacks: Vec<Vec<char>>, moves: Vec<Vec<u8>>) -> String {
    for m in moves {
        for _ in 0..m[0] {
            let c = stacks[(m[1]-1) as usize].remove(0);
            stacks[(m[2]-1) as usize].insert(0, c);
        }
    }

    stacks
        .iter()
        .filter_map(|x| x.first())
        .collect()
}

fn part2(mut stacks: Vec<Vec<char>>, moves: Vec<Vec<u8>>) -> String {
    for m in moves {
        let c = stacks[(m[1]-1) as usize]
            .drain(0..m[0] as usize)
            .collect::<Vec<char>>();
        stacks[(m[2]-1) as usize].splice(0..0, c);
    }

    stacks
        .iter()
        .filter_map(|x| x.first())
        .collect()
}

fn main() {
    let (crates, raw_moves) = include_str!("data.txt").split_once("\n\n").unwrap();
    let stacks = parse_crates(crates);
    let moves = parse_moves(raw_moves);
    println!("PART1: {:?}", part1(stacks.clone(), moves.clone()));
    println!("PART2: {:?}", part2(stacks.clone(), moves.clone()));
}
