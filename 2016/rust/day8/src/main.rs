use std::fmt::Display;

#[derive(Debug)]
struct Screen {
    data: [[bool; 50]; 6],
}

impl Display for Screen {
    fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        for row in &self.data {
            for col in row {
                write!(f, "{}", if *col { '#' } else { ' ' })?;
            }
            write!(f, "\n")?;
        }
        write!(f, "")
    }
}

impl Screen {
    fn new() -> Self {
        Screen {
            data: [[false; 50]; 6],
        }
    }
    fn rect(&mut self, x: usize, y: usize) {
        for i in 0..y {
            for j in 0..x {
                self.data[i][j] = true;
            }
        }
    }
    fn rotate_row(&mut self, row: usize, by: usize) {
        let mut new_row = [false; 50];
        for i in 0..50 {
            new_row[(i + by) % 50] = self.data[row][i];
        }
        self.data[row] = new_row;
    }
    fn rotate_col(&mut self, col: usize, by: usize) {
        let mut new_col = [false; 6];
        for i in 0..6 {
            new_col[(i + by) % 6] = self.data[i][col];
        }
        for i in 0..6 {
            self.data[i][col] = new_col[i];
        }
    }
    fn run_instr(&mut self, instr: &Instr) {
        match instr {
            Instr::Rect(x, y) => self.rect(*x, *y),
            Instr::RotateRow(row, by) => self.rotate_row(*row, *by),
            Instr::RotateCol(col, by) => self.rotate_col(*col, *by),
        }
    }
    fn count(&self) -> usize {
        self.data
            .iter()
            .map(|row| row.iter().filter(|col| **col).count())
            .sum()
    }
}

#[derive(Debug)]
enum Instr {
    Rect(usize, usize),
    RotateRow(usize, usize),
    RotateCol(usize, usize),
}
impl Display for Instr {
    fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        writeln!(f, "{}", self)
    }
}

impl Instr {
    fn parse(input: &str) -> Self {
        match input.split(' ').collect::<Vec<&str>>().as_slice() {
            ["rect", rest] => {
                let mut rest = rest.split('x');
                let x = rest.next().unwrap().parse().unwrap();
                let y = rest.next().unwrap().parse().unwrap();
                Instr::Rect(x, y)
            }
            ["rotate", "row", rest @ ..] => {
                let mut row = rest.get(0).unwrap().split('=');
                row.next();
                let col = row.next().unwrap().parse().unwrap();
                let by = rest.get(rest.len() - 1).unwrap().parse().unwrap();
                Instr::RotateRow(col, by)
            }
            ["rotate", "column", rest @ ..] => {
                let mut col = rest.get(0).unwrap().split('=');
                col.next();
                let col = col.next().unwrap().parse().unwrap();
                let by = rest.get(rest.len() - 1).unwrap().parse().unwrap();
                Instr::RotateCol(col, by)
            }
            _ => panic!("Invalid instruction"),
        }
    }
}

fn main() {
    let data = include_str!("input.txt").trim();
    let instructions: Vec<_> = data.lines().map(Instr::parse).collect();
    let mut screen = Screen::new();
    // instructions.into_iter().fold(screen, |mut screen, instr| {
    //     screen.run_instr(&instr);
    //     screen
    // });
    for instr in instructions {
        screen.run_instr(&instr);
    }
    println!("Part 1: {}", screen.count());
    println!("Part 2:\n{}", screen);
}
