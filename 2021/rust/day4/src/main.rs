use std::fs::File;
use std::io::Read;
use std::iter::FromIterator;

#[derive(Debug, Clone, PartialEq, Eq)]
struct BingoCard {
    grid: Vec<Vec<i32>>,
    winner: bool,
}

impl BingoCard {
    fn mark(&mut self, pick:i32) {
        let mut n_grid = self.grid.clone();
        for (y, line) in self.grid.iter().enumerate() {
            for (x, number) in line.iter().enumerate() {
                if number == &pick {
                    n_grid[y][x] = -1;
                }
            }
        }
        self.grid = n_grid;
        self.check();
    }

    fn get_column(&self, pos: usize) -> Vec<i32> {
        let mut column = Vec::new();
        for line in self.grid.iter() {
            column.push(line[pos as usize]);
        }
        column
    }

    fn check(&mut self) -> bool {
        for line in self.grid.iter() {
            if line.iter().all(|&x| x == -1) {
                self.winner = true;
                return true
            }
        }
        let length = self.grid[0].len();
        for i in 0..length {
            let column = self.get_column(i);
            if column.iter().all(|&x| x == -1) {
                self.winner = true;
                return true
            }
        }
        false
    }
}

impl FromIterator<Vec<i32>> for BingoCard {
    fn from_iter<I>(iter: I) -> Self
        where I: IntoIterator<Item = Vec<i32>>
        {
            let mut grid = Vec::new();
            for row in iter {
                grid.push(row);
            }
            BingoCard { grid, winner:false }
    }
}

fn get_data(filename: &str) -> String {
    let mut file = File::open(filename).expect("file not found");
    let mut contents = String::new();
    file.read_to_string(&mut contents).expect("something went wrong reading the file");
    contents
}

fn process_cards(data: Vec<&str>) -> Vec<BingoCard> {

    let mut cards:Vec<BingoCard> = Vec::new();
    for lines in data.iter().skip(1) {
        let mut grid: Vec<Vec<i32>> = Vec::new();
        for line in lines.split("\n") {
            let mut row: Vec<i32> = Vec::new();
            for s in line.split_whitespace() {
                row.push(s.parse::<i32>().unwrap());
            }
            if !row.is_empty() {
                grid.push(row);
            }
        }
        cards.push(BingoCard{grid , winner:false});
    }
    cards
}

fn play_game(picks: Vec<i32>, mut cards: Vec<BingoCard>) -> (i32, BingoCard) {
    for pick in picks {
        for card in cards.iter_mut() {
            card.mark(pick);
            if card.winner {
                return (pick, card.clone());
            }
        }
    }
    return (-1, BingoCard{grid:vec![], winner:false});
}

fn get_score(pick: i32, card: BingoCard) -> i32 {
    let mut score = 0;
    for line in card.grid.iter() {
        for number in line.iter() {
            if *number != -1 {
                score += number;
            }
        }
    }
    score * pick
}

fn main() {
    let data = get_data("data.txt");
    let bingos: Vec<_> = data.split("\n\n").collect();

    let picks:Vec<i32> = bingos[0]
                        .split(",")
                        .map(|s| s.parse::<i32>().unwrap())
                        .collect();
    let cards = process_cards(bingos);
    let (pick, winner) = play_game(picks, cards);
    dbg!(&pick, &winner);
    println!("PART1: {:?}", get_score(pick, winner));
}
