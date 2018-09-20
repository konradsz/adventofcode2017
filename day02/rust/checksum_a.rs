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

        let mut smallest = std::u32::MAX;
        let mut largest = 0;

        for number in numbers {
            let number = String::from(number).parse::<u32>().unwrap();
            if number < smallest {
                smallest = number;
            }
            if number > largest {
                largest = number;
            }
        }

        checksum += largest - smallest;
    }

    println!("{}", checksum);
    Ok(())
}
