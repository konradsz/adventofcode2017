use std::fs;
use std::collections::HashMap;

fn main() {
    let content = fs::read_to_string("../input").expect("file not found");

    let mut registers: HashMap<String, i32> = HashMap::new();
    let mut highest_value = i32::min_value();

    for line in content.lines() {
        let mut parts_iter = line.split_whitespace();
        let register = parts_iter.next().unwrap();
        let operation = parts_iter.next().unwrap();
        let value = match operation {
            "inc" => parts_iter.next().unwrap().parse::<i32>().unwrap(),
            "dec" => -1 * parts_iter.next().unwrap().parse::<i32>().unwrap(),
            _ => panic!("unknown operation")
        };
        parts_iter.next(); // skip if
        let condition_register = parts_iter.next().unwrap().to_string();
        let condition = parts_iter.next().unwrap();
        let condition_value = parts_iter.next().unwrap().parse::<i32>().unwrap();

        let should_execute = match condition {
            ">" => *registers.entry(condition_register).or_insert(0) > condition_value,
            "<" => *registers.entry(condition_register).or_insert(0) < condition_value,
            ">=" => *registers.entry(condition_register).or_insert(0) >= condition_value,
            "<=" => *registers.entry(condition_register).or_insert(0) <= condition_value,
            "==" => *registers.entry(condition_register).or_insert(0) == condition_value,
            "!=" => *registers.entry(condition_register).or_insert(0) != condition_value,
            _ => panic!("unknown condition")
        };

        if should_execute {
            *registers.entry(register.to_string()).or_insert(0) += value;
            highest_value = highest_value.max(registers[register]);
        }
    }

    let max_value = registers.values().max().unwrap();
    println!("{}", max_value);
    println!("{}", highest_value);
}
