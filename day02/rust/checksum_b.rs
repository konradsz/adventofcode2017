use std::io::{self, BufReader};
use std::io::prelude::*;
use std::fs::File;

fn main() -> io::Result<()> {
    let f = File::open("../input")?;
    let f = BufReader::new(f);

    let mut checksum = 0;

    for line in f.lines() {
        let line: String = line.unwrap();
        let numbers: Vec<&str> = line.split_whitespace().collect();

        for (i, number) in numbers.iter().enumerate() {
            let number = String::from(*number).parse::<u32>().unwrap();
            for (j, number2) in numbers.iter().enumerate() {
                let number2 = String::from(*number2).parse::<u32>().unwrap();
                if (number % number2 == 0) && (i != j) {
                    checksum += number / number2;
                }
            }
        }
    }

    println!("{}", checksum);
    Ok(())
}
