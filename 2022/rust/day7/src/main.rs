use std::collections::HashMap;
use nom::{IResult, character::{complete::{line_ending, digit1, space1, not_line_ending}}, bytes::complete::tag, multi::many1, branch::alt};

#[derive(Debug)]
enum Cmd {
    Cd(Cd),
    Ls(Ls),
}

#[derive(Debug)]
struct Cd {
    path: String,
}

#[derive(Debug)]
struct Ls {
    items: Vec<Item>,
}

#[derive(Debug)]
enum Item {
    File(File),
    Dir(Dir),
}

#[derive(Debug)]
struct File {
    size: u32,
    name: String,
}

#[derive(Debug)]
struct Dir {
    path: String,
}

fn cd(input: &str) -> IResult<&str, Cmd> {
    let (input, _) = tag("$ cd ")(input)?;
    let (input, path) = not_line_ending(input)?;
    let (input, _) = line_ending(input)?;
    Ok((input, Cmd::Cd(Cd{path: path.to_string()})))
}

fn dir(input: &str) -> IResult<&str, Item> {
    let (input, _) = tag("dir ")(input)?;
    let (input, path) = not_line_ending(input)?;
    let (input, _) = line_ending(input)?;
    Ok((input, Item::Dir(Dir{path: path.to_string()})))
}

fn file(input: &str) -> IResult<&str, Item> {
    let (input, size) = digit1(input)?;
    let (input, _) = space1(input)?;
    let (input, name) = not_line_ending(input)?;
    let (input, _) = line_ending(input)?;
    Ok((input, Item::File(File{size: size.parse().unwrap(), name: name.to_string()})))
}

fn ls(input: &str) -> IResult<&str, Cmd> {
    let file_or_dir = alt((file, dir));
    let (input, _) = tag("$ ls")(input)?;
    let (input, _) = line_ending(input)?;
    let (input, items) = many1(file_or_dir)(input)?;
    Ok((input, Cmd::Ls(Ls{items})))
}

fn parse_data(input: &str) -> IResult<&str, Vec<Cmd>> {
    let parser = alt((cd, ls));
    let (input, items) = many1(parser)(input)?;
    Ok((input, items))
}

fn get_directory_data(data: Vec<Cmd>) -> HashMap<String, u32> {
    let mut directory: HashMap<String, u32> = HashMap::new();
    let mut path = vec![];

    for option in data.iter() {
        match option {
            Cmd::Cd(cd) => {
                match cd.path.as_str() {
                    ".." => {
                        path.pop();
                    },
                    p => {
                        if p == "/" {
                            path.push("");
                        } else {
                            path.push(p);
                        }
                    }
                };
            },
            Cmd::Ls(ls) => {
                for item in ls.items.iter() {
                    match item {
                        Item::File(file) => {
                            for i in 1..=path.len() {
                                directory.entry(path[0..i].join("/"))
                                    .and_modify(|e| *e += file.size)
                                    .or_insert(file.size);
                            }

                        },
                        Item::Dir(dir) => {
                            ();
                        }
                    };
                }
            },
        };
    }
    directory
}

fn main() {

    let data = include_str!("data.txt");
    let (_, filesys) = parse_data(data).unwrap();
    let directory = get_directory_data(filesys);
    const PART1_SIZE: u32 = 100_000;
    const TOTAL_DISK_SPACE: u32 = 70_000_000;
    const INSTALL_SIZE: u32 = 30_000_000;

    let part1: u32 = directory.iter().filter(|d| *d.1 <= PART1_SIZE).map(|d| *d.1).sum();
    println!("PART1: {}", part1);

    let PART2_SIZE: u32 = INSTALL_SIZE - (TOTAL_DISK_SPACE - directory.get("").unwrap());
    let part2: u32 = directory.iter().filter(|d| *d.1 >= PART2_SIZE).map(|d| *d.1).min_by(|a,b| a.cmp(&b)).unwrap();
    println!("PART2: {}", part2);
}
