
use nom::{self, sequence::{terminated, preceded, separated_pair},  character::{complete::{ digit1, newline, not_line_ending, one_of, alphanumeric1}}, bytes::complete::{tag}, IResult, multi::{separated_list1, many1}, combinator::opt};
#[derive(Debug, Clone)]
enum Operation {
    Multiply(i32),
    Add(i32),
}
#[derive(Debug, Clone)]
struct Monkey {
    number: i32,
    items: Vec<i32>,
    operation: Operation,
    test: i32,
    itrue: i32,
    ifalse: i32,
    count: i32,
}

fn parse_monkey_number(input: &str) -> IResult<&str, i32> {
    let (input, num) = preceded(tag("Monkey "), digit1)(input)?;
    let (input, _) = terminated(not_line_ending, newline)(input)?;
    Ok((input, num.parse().unwrap()))
}

fn parse_starting_items(input: &str) -> IResult<&str, Vec<i32>> {
    let (input, items) = preceded(tag("  Starting items: "), separated_list1(tag(", "), digit1))(input)?;
    let (input, _) = newline(input)?;
    Ok((input, items.iter().map(|x| x.parse().unwrap()).collect()))
}

fn parse_operation(input: &str) -> IResult<&str, Operation> {
    let (input, operation_raw) = preceded(tag("  Operation: new = old "), not_line_ending)(input)?;
    let (input, _) = newline(input)?;
    let (_, (operation, num_raw)) = separated_pair(one_of("*+"), tag(" "), alphanumeric1)(operation_raw)?;
    let num = num_raw.parse().unwrap_or(-1);

    let op = match operation {
        '*' => Operation::Multiply(num),
        '+' => Operation::Add(num),
        _ => unreachable!(),
    };
    Ok((input, op))
}

fn parse_test(input: &str) -> IResult<&str, i32> {
    let (input, test) = preceded(tag("  Test: divisible by "), digit1)(input)?;
    let (input, _) = newline(input)?;
    Ok((input, test.parse().unwrap()))
}

fn parse_true(input: &str) -> IResult<&str, i32> {
    let (input, itrue) = preceded(tag("    If true: throw to monkey "), digit1)(input)?;
    let (input, _) = newline(input)?;
    Ok((input, itrue.parse().unwrap()))
}

fn parse_false(input: &str) -> IResult<&str, i32> {
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
    Ok((input, Monkey { number, items, operation, test, itrue, ifalse, count: 0 }))
}

fn parse_data(data: &str) -> Vec<Monkey> {
    let (_, monkeys) = many1(terminated(parse_monkey, opt(newline)))(data).unwrap();
    monkeys
}

fn round(monkeys: &mut Vec<Monkey>) {
    for idx in 0..monkeys.len() {
        let ro_monkey = monkeys[idx].clone();
        for item in ro_monkey.items {
            monkeys[idx].count += 1;

            let worry = match monkeys[idx].operation {
                Operation::Multiply(-1) => item * item,
                Operation::Multiply(x) => item * x,
                Operation::Add(x) => item + x,
            } / 3;

            if worry % monkeys[idx].test == 0 {
                monkeys[ro_monkey.itrue as usize].items.push(worry);
            } else {
                monkeys[ro_monkey.ifalse as usize].items.push(worry);
            }
        }
        monkeys[idx].items.clear();
    }
}

fn main() {
    let mut data = parse_data(include_str!("data.txt"));

    for _ in 0..20 {
        round(&mut data);
    }
    data.sort_by(|a,b| b.count.cmp(&a.count));
    println!("PART1: {}", &data[0].count * &data[1].count);
}
