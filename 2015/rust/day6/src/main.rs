use nom::IResult;

#[derive(Debug)]
enum Action {
    TurnOn,
    TurnOff,
    Toggle,
}

#[derive(Debug)]
struct Instr {
    action: Action,
    x1: usize,
    y1: usize,
    x2: usize,
    y2: usize,
}

impl From<&str> for Instr {
    fn from(value: &str) -> Self {
        parse_instruction(value)
    }
}

fn parse_action(input: &str) -> IResult<&str, Action> {
    let (input, text) = nom::bytes::complete::take_till1(|c: char| c.is_ascii_digit())(input)?;
    match text.trim() {
        "turn on" => Ok((input, Action::TurnOn)),
        "turn off" => Ok((input, Action::TurnOff)),
        "toggle" => Ok((input, Action::Toggle)),
        _ => Err(nom::Err::Error(nom::error::Error::new(
            input,
            nom::error::ErrorKind::Tag,
        ))),
    }
}

fn parse_coord(input: &str) -> (usize, usize) {
    let (x, y) = input.split_once(',').unwrap();
    (x.parse().unwrap(), y.parse().unwrap())
}

fn parse_instruction(input: &str) -> Instr {
    let (input, action) = parse_action(input).expect("Failed to parse action");
    let (first, second) = input.split_once(" through ").unwrap();
    let (x1, y1) = parse_coord(first);
    let (x2, y2) = parse_coord(second);
    Instr {
        action,
        x1,
        y1,
        x2,
        y2,
    }
}

fn part1(instructions: &Vec<Instr>) -> usize {
    let mut grid = [[0; 1000]; 1000];
    for instr in instructions {
        for x in instr.x1..=instr.x2 {
            for y in instr.y1..=instr.y2 {
                match instr.action {
                    Action::TurnOn => grid[x][y] = 1,
                    Action::TurnOff => grid[x][y] = 0,
                    Action::Toggle => grid[x][y] = 1 - grid[x][y],
                }
            }
        }
    }
    grid.iter().flatten().sum()
}

fn part2(instructions: &Vec<Instr>) -> usize {
    let mut grid = [[0usize; 1000]; 1000];
    for instr in instructions {
        for x in instr.x1..=instr.x2 {
            for y in instr.y1..=instr.y2 {
                match instr.action {
                    Action::TurnOn => grid[x][y] += 1,
                    Action::TurnOff => grid[x][y] = grid[x][y].saturating_sub(1),
                    Action::Toggle => grid[x][y] += 2,
                }
            }
        }
    }
    grid.iter().flatten().sum()
}

fn main() {
    let data = include_str!("input.txt").trim();
    let instructions: Vec<Instr> = data.lines().map(|line| line.into()).collect();

    println!("Part1: {:?}", part1(&instructions));
    println!("Part2: {:?}", part2(&instructions));
}
