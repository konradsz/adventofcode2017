use std::fs;
use std::collections::HashMap;

enum Operation {
    Inc,
    Dec
}

fn execute(registers: &mut HashMap<&str, i32>, operation: Operation, register: &str, value: i32, highest_value: &mut i32) {
    match operation {
        Operation::Inc => {
            *registers.get_mut(register).unwrap() += value;
        },
        Operation::Dec => {
            *registers.get_mut(register).unwrap() -= value;
        }
    }

    if *registers.get(register).unwrap() > *highest_value {
        *highest_value = *registers.get(register).unwrap();
    }
}

fn main() {
    let content = fs::read_to_string("../input").expect("file not found");

    let mut registers = HashMap::new();
    let mut highest_value = 0;

    for line in content.lines() {
        let mut parts_iter = line.split_whitespace();
        let register = parts_iter.next().unwrap();
        let operation = match parts_iter.next().unwrap() {
            "inc" => Operation::Inc,
            "dec" => Operation::Dec,
            _ => panic!("unknown operation")
        };
        let value = parts_iter.next().unwrap().parse::<i32>().unwrap();
        parts_iter.next(); // skip if
        let condition_register = parts_iter.next().unwrap();
        let condition = parts_iter.next().unwrap();
        let condition_value = parts_iter.next().unwrap().parse::<i32>().unwrap();

        if !registers.contains_key(register) {
            registers.insert(register, 0);
        }
        if !registers.contains_key(condition_register) {
            registers.insert(condition_register, 0);
        }

        match condition {
            ">" => {
                if registers.get(condition_register).unwrap() > &condition_value {
                    execute(&mut registers, operation, register, value, &mut highest_value);
                }
            },
            "<" => {
                if registers.get(condition_register).unwrap() < &condition_value {
                    execute(&mut registers, operation, register, value, &mut highest_value);
                }
            },
            ">=" => {
                if registers.get(condition_register).unwrap() >= &condition_value {
                    execute(&mut registers, operation, register, value, &mut highest_value);
                }
            },
            "<=" => {
                if registers.get(condition_register).unwrap() <= &condition_value {
                    execute(&mut registers, operation, register, value, &mut highest_value);
                }
            },
            "==" => {
                if registers.get(condition_register).unwrap() == &condition_value {
                    execute(&mut registers, operation, register, value, &mut highest_value);
                }
            },
            "!=" => {
                if registers.get(condition_register).unwrap() != &condition_value {
                    execute(&mut registers, operation, register, value, &mut highest_value);
                }
            },
            _ => panic!("unknown condition")
        };
    }

    let max_value = registers.values().max().unwrap();
    println!("{}", max_value);
    println!("{}", highest_value);
}
