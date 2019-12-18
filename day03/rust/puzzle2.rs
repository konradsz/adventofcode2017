use std::collections::HashMap;

const INPUT: u32 = 312051;

enum Direction {
    Right,
    Up,
    Left,
    Down,
}

#[derive(Debug, Clone, PartialEq, Eq, Hash)]
struct Position {
    x: i32,
    y: i32,
}

impl Position {
    fn new(x: i32, y: i32) -> Self {
        Position { x, y }
    }
}

fn main() {
    let mut grid = HashMap::new();

    let mut current_position = Position { x: 0, y: 0 };
    let mut direction = Direction::Right;
    let mut width = 1;
    let mut height = 1;

    grid.insert(current_position.clone(), 1);

    let sum_neighbours = |grid: &HashMap<Position, u32>, position: &Position| -> u32 {
        let neighbours = vec![
            grid.get(&Position::new(position.x - 1, position.y - 1)),
            grid.get(&Position::new(position.x, position.y - 1)),
            grid.get(&Position::new(position.x + 1, position.y - 1)),
            grid.get(&Position::new(position.x + 1, position.y)),
            grid.get(&Position::new(position.x + 1, position.y + 1)),
            grid.get(&Position::new(position.x, position.y + 1)),
            grid.get(&Position::new(position.x - 1, position.y + 1)),
            grid.get(&Position::new(position.x - 1, position.y)),
        ];

        neighbours
            .iter()
            .filter(|elem| elem.is_some())
            .map(|elem| elem.unwrap())
            .sum()
    };

    let mut sum;
    let mut number_of_iterations;
    let mut offset;

    'outer: loop {
        match direction {
            Direction::Right => {
                number_of_iterations = width;
                offset = (1, 0);
                width += 1;
                direction = Direction::Up;
            }
            Direction::Up => {
                number_of_iterations = height;
                offset = (0, -1);
                height += 1;
                direction = Direction::Left;
            }
            Direction::Left => {
                number_of_iterations = width;
                offset = (-1, 0);
                width += 1;
                direction = Direction::Down;
            }
            Direction::Down => {
                number_of_iterations = height;
                offset = (0, 1);
                height += 1;
                direction = Direction::Right;
            }
        };

        for _ in 0..number_of_iterations {
            current_position.x += offset.0;
            current_position.y += offset.1;
            sum = sum_neighbours(&grid, &current_position);
            if sum > INPUT {
                break 'outer;
            }
            grid.insert(current_position.clone(), sum);
        }
    }

    println!("{}", sum);
}
