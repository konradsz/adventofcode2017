use std::collections::HashMap;
use std::fs;

fn get(operand: &str, registers: &HashMap<char, isize>) -> isize {
    if let Ok(number) = operand.parse::<isize>() {
        number
    } else {
        registers[&operand.chars().next().unwrap()]
    }
}

fn main() {
    let content = fs::read_to_string("../input").expect("file not found");
    let instructions: Vec<&str> = content.lines().collect();

    let mut registers = HashMap::new();
    registers.insert('a', 0);
    registers.insert('b', 0);
    registers.insert('c', 0);
    registers.insert('d', 0);
    registers.insert('e', 0);
    registers.insert('f', 0);
    registers.insert('g', 0);
    registers.insert('h', 0);

    let mut pc = 0;
    let mut counter = 0;

    while pc < instructions.len() {
        let mut instruction = instructions[pc].split_whitespace();
        pc += 1;

        let instruction_type = instruction.next().unwrap();
        let first_operand = instruction.next().unwrap();
        let second_operand = instruction.next().unwrap();

        if instruction_type == "set" {
            let value = get(second_operand, &registers);
            let first_operand = first_operand.chars().next().unwrap();
            *registers.get_mut(&first_operand).unwrap() = value;
        } else if instruction_type == "sub" {
            let value = get(second_operand, &registers);
            let first_operand = first_operand.chars().next().unwrap();
            *registers.get_mut(&first_operand).unwrap() -= value;
        } else if instruction_type == "mul" {
            let value = get(second_operand, &registers);
            let first_operand = first_operand.chars().next().unwrap();
            *registers.get_mut(&first_operand).unwrap() *= value;
            counter += 1;
        } else if instruction_type == "jnz" {
            let first_value = get(first_operand, &registers);
            let second_value = get(second_operand, &registers);
            if first_value != 0 {
                let mut pc_i = pc as isize;
                pc_i += second_value - 1;
                pc = pc_i as usize;
            }
        }
    }

    println!("{}", counter);
}
