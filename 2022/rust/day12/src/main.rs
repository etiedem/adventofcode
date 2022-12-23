use std::cmp::Ordering;
use std::collections::{BinaryHeap, HashMap};
use std::hash::Hash;

#[derive(Debug)]
struct Map {
    grid: Vec<Vec<Node>>,
    length: usize,
    width: usize,
}

impl Map {
    fn get_neighbors(&self, node: &Node) -> Vec<Node> {
        let mut neighbors = Vec::new();
        let moves = vec![(0, 1), (1, 0), (0, -1), (-1, 0)];
        for (x, y) in moves {
            let new_x = node.x + x;
            let new_y = node.y + y;
            if self.check_bounds(new_x, new_y)
                && self.grid[(new_y) as usize][(new_x) as usize].value <= node.value + 1
            {
                neighbors.push(self.grid[(new_y) as usize][(new_x) as usize])
            }
        }
        neighbors
    }

    fn check_bounds(&self, x: isize, y: isize) -> bool {
        x >= 0 && x < self.width as isize && y >= 0 && y < self.length as isize
    }

    fn show_path(&self, path: Vec<Node>) {
        for row in self.grid.iter() {
            for item in row {
                if path.contains(item) {
                    print!("X");
                } else {
                    print!(".");
                }
            }
            println!();
        }
    }

    fn iter(&self) -> impl Iterator<Item = &Node> {
        self.grid.iter().flat_map(|row| row.iter())
    }
}

#[derive(Debug)]
struct State {
    dist: isize,
    node: Node,
}
impl PartialOrd for State {
    fn partial_cmp(&self, other: &Self) -> Option<Ordering> {
        Some(other.dist.cmp(&self.dist))
    }
}

impl Ord for State {
    fn cmp(&self, other: &Self) -> Ordering {
        other.dist.cmp(&self.dist)
    }
}

impl PartialEq for State {
    fn eq(&self, other: &Self) -> bool {
        (self.dist == other.dist) && (self.node == other.node)
    }
}
impl Eq for State {}

#[derive(Debug, Hash, Eq, PartialEq, Default, Clone, Copy)]
struct Node {
    x: isize,
    y: isize,
    item: char,
    value: isize,
}

impl Node {
    fn manhattan_distance(&self, other: &Self) -> isize {
        (self.x - other.x).abs() + (self.y - other.y).abs()
    }
}

fn parse_data(data: &str) -> Vec<Vec<char>> {
    data.split_whitespace()
        .map(|line| line.chars().collect())
        .collect()
}

fn create_map(data: Vec<Vec<char>>) -> (Node, Node, Map) {
    let mut grid = Vec::new();
    let mut start = Node::default();
    let mut goal = Node::default();
    for (y, row) in data.iter().enumerate() {
        let mut new_row = Vec::new();
        for (x, item) in row.iter().enumerate() {
            let value = match item {
                'S' => 1,
                'E' => 26,
                c => (*c as usize) - 96,
            };
            if *item == 'S' {
                start = Node {
                    x: x as isize,
                    y: y as isize,
                    item: *item,
                    value: value as isize,
                };
                new_row.push(Node {
                    x: x as isize,
                    y: y as isize,
                    item: *item,
                    value: value as isize,
                });
            } else if *item == 'E' {
                goal = Node {
                    x: x as isize,
                    y: y as isize,
                    item: *item,
                    value: value as isize,
                };
                new_row.push(Node {
                    x: x as isize,
                    y: y as isize,
                    item: *item,
                    value: value as isize,
                });
            } else {
                new_row.push(Node {
                    x: x as isize,
                    y: y as isize,
                    item: *item,
                    value: value as isize,
                });
            }
        }
        grid.push(new_row);
    }
    let length = grid.len();
    let width = grid[0].len();
    (
        start,
        goal,
        Map {
            grid,
            length,
            width,
        },
    )
}

fn dijkstra(graph: &Map, start: Node) -> HashMap<Node, Option<Node>> {
    let mut q = BinaryHeap::new();
    let mut prev: HashMap<Node, Option<Node>> = HashMap::new();
    let mut dist: HashMap<Node, isize> = HashMap::new();

    dist.insert(start, 0);
    q.push(State {
        dist: 0,
        node: start,
    });

    while !q.is_empty() {
        let current = q.pop().unwrap();

        for nei in graph.get_neighbors(&current.node) {
            let alt = State {
                dist: current.dist.saturating_add(nei.manhattan_distance(&start)),
                node: nei,
            };
            if alt.dist < *dist.entry(nei).or_insert(isize::MAX) {
                dist.entry(nei).and_modify(|e| *e = alt.dist);
                prev.entry(nei)
                    .and_modify(|e| *e = Some(current.node))
                    .or_insert(Some(current.node));
                q.push(alt);
            }
        }
    }
    prev
}

fn get_path(data: HashMap<Node, Option<Node>>, goal: Node) -> Vec<Node> {
    let mut path: Vec<Node> = Vec::new();
    let mut current: Option<Node> = Some(goal);
    let mut shortest = data.clone();
    while let Some(next) = current {
        path.push(next);
        current = *shortest.entry(next).or_default();
    }
    path.reverse();
    path
}

fn find_char(map: &Map, find: char) -> Vec<Node> {
    map.iter().filter(|i| i.item == find).map(|i| *i).collect()
}

fn find_path(map: &Map, find: char, goal: Node) -> Vec<Node> {
    let mut min: Vec<Node> = Vec::new();
    for start in find_char(&map, find) {
        let current = get_path(dijkstra(map, start), goal);
        if current.len() > 1 && (min.is_empty() || (current.len() < min.len())) {
            min = current;
        }
    }
    min
}

fn main() {
    let data = parse_data(include_str!("data.txt"));
    let (start, goal, map) = create_map(data);
    let shortest = dijkstra(&map, start);
    let path = get_path(shortest, goal);
    println!("PART 1: {}", &path.len() - 1);
    println!("PART 2: {:?}", find_path(&map, 'a', goal).len() - 1);
}
