struct Generator {
    value: usize,
    factor: usize,
}

impl Generator {
    fn new(value: usize, factor: usize) -> Generator {
        Generator { value, factor }
    }
}

impl Iterator for Generator {
    type Item = usize;

    fn next(&mut self) -> Option<usize> {
        self.value = (self.value * self.factor) % 2147483647;

        Some(self.value)
    }
}

fn main() {
    let generator_a = Generator::new(591, 16807);
    let generator_b = Generator::new(393, 48271);

    let count = generator_a
        .zip(generator_b)
        .take(40_000_000)
        .filter(|&(a, b)| a & 0xFFFF == b & 0xFFFF)
        .count();
    println!("{}", count);

    let generator_a = Generator::new(591, 16807);
    let generator_b = Generator::new(393, 48271);

    let count = generator_a
        .filter(|a| a % 4 == 0)
        .zip(generator_b.filter(|b| b % 8 == 0))
        .take(5_000_000)
        .filter(|&(a, b)| a & 0xFFFF == b & 0xFFFF)
        .count();
    println!("{}", count);
}
