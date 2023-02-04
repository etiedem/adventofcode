#[derive(Debug)]
enum Dir {
    Up,
    Right,
    Down,
    Left,
}

impl From<char> for Dir {
    fn from(value: char) -> Self {
        match value {
            'U' => Dir::Up,
            'R' => Dir::Right,
            'D' => Dir::Down,
            'L' => Dir::Left,
            _ => unreachable!(),
        }
    }
}

impl Dir {
    fn step(&self) -> (i32, i32) {
        match self {
            Dir::Up => (0, -1),
            Dir::Right => (1, 0),
            Dir::Down => (0, 1),
            Dir::Left => (-1, 0),
        }
    }
}

#[derive(Debug)]
struct Pos(i32, i32);

impl Pos {
    fn step(&self, dir: &Dir) -> Pos {
        let (x, y) = dir.step();
        Pos(self.0 + x, self.1 + y)
    }
}

struct Grid<'a> {
    matrix: Vec<Vec<&'a str>>,
    pos: Pos,
}

impl<'a> Grid<'a> {
    fn step(&mut self, dir: &Dir) {
        let Pos(cx, cy) = self.pos.step(dir);
        if cx >= 0
            && cy >= 0
            && cx < self.matrix.len() as i32
            && cy < self.matrix.len() as i32
            && self.matrix[cy as usize][cx as usize] != "#"
        {
            self.pos = Pos(cx, cy);
        }
    }
}

fn parse_directions(input: &str) -> Vec<Vec<Dir>> {
    input
        .lines()
        .map(|x| x.chars().map(|x| x.into()).collect())
        .collect()
}

fn solve(mut grid: Grid, directions: &Vec<Vec<Dir>>) -> String {
    let mut num = String::new();
    for line in directions {
        for dir in line {
            grid.step(dir);
        }
        num.push_str(grid.matrix[grid.pos.1 as usize][grid.pos.0 as usize]);
    }
    num
}

fn main() {
    let data = parse_directions(include_str!("input.txt"));

    let part1_matrix = vec![
        vec!["1", "2", "3"],
        vec!["4", "5", "6"],
        vec!["7", "8", "9"],
    ];
    let part1_pos = Pos(1, 1);
    let part1_grid = Grid {
        matrix: part1_matrix,
        pos: part1_pos,
    };
    let part1 = solve(part1_grid, &data);
    println!("Part 1: {}", part1);

    let part2_matrix = vec![
        vec!["#", "#", "1", "#", "#"],
        vec!["#", "2", "3", "4", "#"],
        vec!["5", "6", "7", "8", "9"],
        vec!["#", "A", "B", "C", "#"],
        vec!["#", "#", "D", "#", "#"],
    ];
    let part2_pos = Pos(0, 2);
    let part2_grid = Grid {
        matrix: part2_matrix,
        pos: part2_pos,
    };
    let part2 = solve(part2_grid, &data);
    println!("Part 2: {}", part2);
}
