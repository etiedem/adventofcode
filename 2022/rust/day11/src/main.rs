use nom::{
    self,
    bytes::complete::tag,
    character::complete::{alphanumeric1, digit1, newline, not_line_ending, one_of},
    combinator::opt,
    multi::{many1, separated_list1},
    sequence::{preceded, separated_pair, terminated},
    IResult,
};
#[derive(Debug, Clone)]
enum Operation {
    Multiply(i64),
    MultiplySelf,
    Add(i64),
    AddSelf,
}

impl Operation {
    fn calc(&self, val: i64) -> i64 {
        match self {
            Self::Multiply(n) => val * *n,
            Self::MultiplySelf => val * val,
            Self::Add(n) => val + *n,
            Self::AddSelf => val + val,
        }
    }
}
#[derive(Debug, Clone)]
struct Monkey {
    number: i32,
    items: Vec<i64>,
    operation: Operation,
    test: i64,
    itrue: i64,
    ifalse: i64,
    count: i64,
}

fn parse_monkey_number(input: &str) -> IResult<&str, i32> {
    let (input, num) = preceded(tag("Monkey "), digit1)(input)?;
    let (input, _) = terminated(not_line_ending, newline)(input)?;
    Ok((input, num.parse().unwrap()))
}

fn parse_starting_items(input: &str) -> IResult<&str, Vec<i64>> {
    let (input, items) = preceded(
        tag("  Starting items: "),
        separated_list1(tag(", "), digit1),
    )(input)?;
    let (input, _) = newline(input)?;
    Ok((input, items.iter().map(|x| x.parse().unwrap()).collect()))
}

fn parse_operation(input: &str) -> IResult<&str, Operation> {
    let (input, operation_raw) = preceded(tag("  Operation: new = old "), not_line_ending)(input)?;
    let (input, _) = newline(input)?;
    let (_, (operation, num_raw)) =
        separated_pair(one_of("*+"), tag(" "), alphanumeric1)(operation_raw)?;
    let num = num_raw.parse().unwrap_or(-1);

    let op = if num == -1 {
        match operation {
            '*' => Operation::MultiplySelf,
            '+' => Operation::AddSelf,
            _ => unreachable!(),
        }
    } else {
        match operation {
            '*' => Operation::Multiply(num),
            '+' => Operation::Add(num),
            _ => unreachable!(),
        }
    };
    Ok((input, op))
}

fn parse_test(input: &str) -> IResult<&str, i64> {
    let (input, test) = preceded(tag("  Test: divisible by "), digit1)(input)?;
    let (input, _) = newline(input)?;
    Ok((input, test.parse().unwrap()))
}

fn parse_true(input: &str) -> IResult<&str, i64> {
    let (input, itrue) = preceded(tag("    If true: throw to monkey "), digit1)(input)?;
    let (input, _) = newline(input)?;
    Ok((input, itrue.parse().unwrap()))
}

fn parse_false(input: &str) -> IResult<&str, i64> {
    let (input, ifalse) = preceded(tag("    If false: throw to monkey "), digit1)(input)?;
    let (input, _) = newline(input)?;
    Ok((input, ifalse.parse().unwrap()))
}

fn parse_monkey(input: &str) -> IResult<&str, Monkey> {
    let (input, number) = parse_monkey_number(input)?;
    let (input, items) = parse_starting_items(input)?;
    let (input, operation) = parse_operation(input)?;
    let (input, test) = parse_test(input)?;
    let (input, itrue) = parse_true(input)?;
    let (input, ifalse) = parse_false(input)?;
    Ok((
        input,
        Monkey {
            number,
            items,
            operation,
            test,
            itrue,
            ifalse,
            count: 0,
        },
    ))
}

fn parse_data(data: &str) -> Vec<Monkey> {
    let (_, monkeys) = many1(terminated(parse_monkey, opt(newline)))(data).unwrap();
    monkeys
}

fn round(monkeys: &mut Vec<Monkey>, part1: bool) {
    let modvalue: i64 = monkeys.iter().map(|x| x.test).product();

    for idx in 0..monkeys.len() {
        let ro_monkey = monkeys[idx].clone();
        for item in ro_monkey.items {
            monkeys[idx].count += 1;

            let worry = if part1 {
                monkeys[idx].operation.calc(item) / 3
            } else {
                monkeys[idx].operation.calc(item) % modvalue
            };

            let dest = if worry % monkeys[idx].test == 0 {
                ro_monkey.itrue as usize
            } else {
                ro_monkey.ifalse as usize
            };
            monkeys[dest].items.push(worry);
        }
        monkeys[idx].items.clear();
    }
}

fn main() {
    let data = parse_data(include_str!("data.txt"));

    let mut part1_data = data.clone();
    for _ in 0..20 {
        round(&mut part1_data, true);
    }
    part1_data.sort_by(|a, b| b.count.cmp(&a.count));
    println!("PART1: {}", part1_data[0].count * part1_data[1].count);

    let mut part2_data = data.clone();
    for _ in 0..10_000 {
        round(&mut part2_data, false);
    }
    part2_data.sort_by(|a, b| b.count.cmp(&a.count));
    println!("PART2: {}", part2_data[0].count * part2_data[1].count);
}
