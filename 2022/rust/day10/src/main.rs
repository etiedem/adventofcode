#[derive(Debug)]
struct Command {
    number: i32,
    cycles: i32,
}

fn parse_data(data: &str) -> Vec<Command> {
    data.lines()
        .map(|line| {
            let mut parts = line.split_whitespace();
            let command = parts.next().unwrap();
            let cycles = match command {
                "addx" => 2,
                _ => 1
            };
            let number = parts.next().unwrap_or("0").parse().unwrap();
            Command { number, cycles }
        }).collect()
}

fn execute(commands: &Vec<Command>) -> Vec<i32> {
    let mut x = 1;
    let mut cycle = 0;
    let mut register = Vec::new();

    let mut get = 20;
    for command in commands {
        for c in 0..command.cycles {
            cycle += 1;
            if cycle == get {
                get += 40;
                register.push(x * cycle);
            }
            if c == command.cycles-1 {
                x += command.number;
            }
        }
    }
    register
}

fn main() {
    let data = parse_data(include_str!("data.txt"));
    println!("Part 1: {:?}", execute(&data).iter().sum::<i32>());
}

