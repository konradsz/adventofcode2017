struct Generator {
    value: usize,
    factor: usize
}

impl Generator {
    fn new(value: usize, factor: usize) -> Generator {
        Generator {
            value,
            factor
        }
    }
}

impl Iterator for Generator {
    type Item = usize;

    fn next(&mut self) -> Option<usize> {
        self.value = (self.value * self.factor) % 2147483647;

        Some(self.value)
    }
}

struct Generator2 {
    value: usize,
    factor: usize,
    divisor: usize
}

impl Generator2 {
    fn new(value: usize, factor: usize, divisor: usize) -> Generator2 {
        Generator2 {
            value,
            factor,
            divisor
        }
    }
}

impl Iterator for Generator2 {
    type Item = usize;

    fn next(&mut self) -> Option<usize> {
        self.value = (self.value * self.factor) % 2147483647;
        if self.value % self.divisor == 0 {
            Some(self.value)
        } else {
            None
        }
    }
}

fn main() {
    let mut generator1 = Generator::new(591, 16807);
    let mut generator2 = Generator::new(393, 48271);

    let mut count = 0;
    for _ in 0..40_000_000 {
        if (generator1.next().unwrap() & 0xFFFF) == (generator2.next().unwrap() & 0xFFFF) {
            count += 1;
        }
    }
    println!("{}", count);

    count = 0;
    let mut generator1 = Generator2::new(591, 16807, 4);
    let mut generator2 = Generator2::new(393, 48271, 8);
    for _ in 0..5_000_000 {
        let mut value1;
        let mut value2;
        loop {
            value1 = generator1.next();
            if value1 != None {
                break;
            }
        }

        loop {
            value2 = generator2.next();
            if value2 != None {
                break;
            }
        }

        if (value1.unwrap() & 0xFFFF) == (value2.unwrap() & 0xFFFF) {
            count += 1;
        }
    }
    println!("{}", count);
}
