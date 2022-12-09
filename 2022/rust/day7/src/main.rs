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

fn main() {
    let mut directory: HashMap<String, u32> = HashMap::new();

    let data = include_str!("data.txt");
    let (remain, filesys) = parse_data(data).unwrap();
    dbg!(remain);
    let mut path = vec![];

    for option in filesys.iter() {
        match option {
            Cmd::Cd(cd) => {
                match cd.path.as_str() {
                    ".." => {
                        path.pop();
                    },
                    p => {
                        path.push(p);
                        if directory.get(p).is_none() {
                            directory.insert(p.to_string(), 0);
                        }
                    }
                };
                // dbg!(&path);
            },
            Cmd::Ls(ls) => {
                for item in ls.items.iter() {
                    match item {
                        Item::File(file) => {
                            for dir in &path {
                                directory.entry(dir.to_string()).and_modify(|e| *e += file.size);
                            }
                        },
                        Item::Dir(dir) => {
                            if directory.get(&dir.path).is_none() {
                                directory.insert(dir.path.clone(), 0);
                            }
                        }
                    };
                }
            },
        };
    }

    let answer: u32 = directory.iter().filter(|d| *d.1 <= 100_000_u32).map(|d| *d.1).sum();
    dbg!(answer);
}
