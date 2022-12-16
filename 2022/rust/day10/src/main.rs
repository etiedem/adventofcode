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

fn run(commands: &Vec<Command>) -> (Vec<i32>, Vec<&str>) {
    let mut x = 1;
    let mut cycle = 0;
    let mut signal_strength = Vec::new();
    let mut image = Vec::new();

    let mut get = 20;
    for command in commands {
        for c in 0..command.cycles {
            if [x-1,x,x+1].contains(&(cycle%40)) {
                image.push("#");
            } else {
                image.push(" ");
            }
            cycle += 1;
            if cycle == get {
                get += 40;
                signal_strength.push(x * cycle);
            }
            if c == command.cycles-1 {
                x += command.number;
            }
        }
    }
    (signal_strength, image)
}

fn main() {
    let data = parse_data(include_str!("data.txt"));
    let (signal_strength, image) = run(&data);
    println!("Part 1: {:?}", signal_strength.iter().sum::<i32>());
    println!("Part 2:");
    for chunk in image.chunks(40) {
        println!("{}", chunk.join(""));
    }
}

