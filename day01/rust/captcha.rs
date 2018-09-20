use std::fs;

fn captcha(input1: &Vec<u32>, input2: &Vec<u32>) -> u32 {
    let mut sum = 0;
    for (first, second) in input1.iter().zip(input2.iter()) {
        if first == second {
            sum += first;
        }
    }
    sum
}

fn main() {
    let contents = fs::read_to_string("../input")
        .expect("file not found");

    let mut input1 = Vec::new();
    for c in contents.chars() {
        if let Some(digit) = c.to_digit(10) {
            input1.push(digit);
        }
    }

    {
        let mut input2 = input1[1..].to_vec();
        if let Some(first) = input1.first().cloned() {
            input2.push(first);
        }

        println!("{}", captcha(&input1, &input2));
    }

    {
        let mut input2 = Vec::new();
        for i in &input1[input1.len() / 2..] {
            input2.push(*i);
        }
        for i in &input1[0..input1.len() / 2] {
            input2.push(*i);
        }

        println!("{}", captcha(&input1, &input2));
    }
}
