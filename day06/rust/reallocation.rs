use std::fs;

fn cycle(memory: &mut Vec<usize>) {
    let len = memory.len();
    let max_value = *memory.iter().max().unwrap();
    let max_value_index = memory.iter().position(|&v| v == max_value).unwrap();

    memory[max_value_index] = 0;
    for i in 1..=max_value {
        memory[(max_value_index + i) % len] += 1;
    }
}

fn main() {
    let content = fs::read_to_string("../input").expect("file not found");

    let mut memory: Vec<usize> = content
        .split_whitespace()
        .map(|number| number.parse::<usize>().unwrap())
        .collect();
    let mut states: Vec<Vec<usize>> = Vec::new();

    while !states.contains(&memory) {
        states.push(memory.clone());
        cycle(&mut memory);
    }

    println!("{}", states.len());
    let previous_occurrence = states.iter().position(|m| *m == memory).unwrap();
    println!("{}", states.len() - previous_occurrence);
}
