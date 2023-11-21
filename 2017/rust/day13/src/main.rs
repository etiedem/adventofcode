use regex::Regex;

#[derive(Debug)]
struct Layer {
    depth: i32,
    pos: i32,
    direction: String,
}

impl Default for Layer {
    fn default() -> Self {
        Layer {
            depth: 0,
            pos: 0,
            direction: "down".into(),
        }
    }
}

impl Layer {
    fn step(&mut self) {
        match self.direction.as_str() {
            "down" => {
                self.pos += 1;
                if self.pos == self.depth - 1 {
                    self.direction = "up".into()
                }
            }
            "up" => {
                self.pos -= 1;
                if self.pos == 0 {
                    self.direction = "down".into()
                }
            }
            _ => unreachable!(),
        }
    }
}

#[derive(Debug)]
struct Search {
    delay: u32,
    skip: Vec<(usize, u32)>,
}

impl Search {
    fn check_num(&self) -> bool {
        for (idx, num) in self.skip.iter() {
            if (self.delay + *idx as u32) % num == 0 {
                return true;
            }
        }
        return false;
    }

    fn new(game: &Game) -> Search {
        let mut nums = vec![];
        for (idx, value) in game.layers.iter().enumerate() {
            match value {
                Some(layer) => nums.push((idx, 2 * (layer.depth as u32 - 1))),
                None => {}
            }
        }
        nums.sort();

        Search {
            delay: 0,
            skip: nums,
        }
    }
}

impl Iterator for Search {
    type Item = u32;

    fn next(&mut self) -> Option<Self::Item> {
        self.delay += 1;
        if self.check_num() {
            while self.check_num() {
                self.delay += 1;
            }
        }
        Some(self.delay)
    }
}

#[derive(Debug)]
struct Game {
    layers: Vec<Option<Layer>>,
    player: i32,
    severity: i32,
    caught: bool,
}

impl Default for Game {
    fn default() -> Self {
        Game {
            layers: vec![None],
            player: -1,
            severity: 0,
            caught: false,
        }
    }
}

impl Game {
    fn run(&mut self, part2: bool) {
        while self.player as usize != self.layers.len() {
            if part2 && self.caught {
                break;
            }
            self.step();
        }
    }

    fn reset(&mut self) {
        self.player = -1;
        self.severity = 0;
        self.caught = false;

        for value in &mut self.layers {
            match value {
                Some(ref mut layer) => {
                    layer.pos = 0;
                    layer.direction = "down".into()
                }
                None => {}
            }
        }
    }

    fn delay(&mut self, num: u32) {
        for _ in 0..num {
            for value in &mut self.layers {
                match value {
                    Some(ref mut layer) => layer.step(),
                    None => {}
                }
            }
        }
    }

    fn step(&mut self) -> Option<&Game> {
        self.player += 1;
        if self.player as usize >= self.layers.len() {
            return Some(self);
        }
        if let Some(layer) = &self.layers[self.player as usize] {
            if layer.pos == 0 {
                self.caught = true;
                self.severity += self.player * layer.depth
            }
        }

        for value in &mut self.layers {
            match value {
                Some(ref mut layer) => layer.step(),
                None => {}
            }
        }
        None
    }
}

fn parse_data(data: &str) -> Game {
    let re = Regex::new(r": ").unwrap();
    let mut count = 0;
    let mut layers = vec![];
    for parsed in data
        .lines()
        .map(|line| re.split(line).collect::<Vec<&str>>())
    {
        while parsed[0].parse::<i32>().unwrap() > count {
            layers.push(None);
            count += 1;
        }
        layers.push(Some(Layer {
            depth: parsed[1].parse().unwrap(),
            ..Default::default()
        }));
        count += 1;
    }
    Game {
        layers,
        ..Default::default()
    }
}

fn find_delay(mut game: Game) -> u32 {
    let mut farthest = 0;
    for count in Search::new(&game) {
        game.reset();
        game.delay(count);
        game.run(true);
        if game.player > farthest {
            farthest = game.player;
        }
        if !game.caught {
            return count;
        }
    }
    u32::MAX
}

fn main() {
    let data = include_str!("../day13.txt");
    let mut game = parse_data(data);

    game.run(false);
    println!("Part 1: {}", game.severity);

    let p2 = find_delay(game);
    println!("Part 2: {}", p2);
}
