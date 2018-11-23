use std::fs;

struct Particle {
    position: (i32, i32, i32),
    velocity: (i32, i32, i32),
    acceleration: (i32, i32, i32),
    destroyed: bool,
}

impl Particle {
    fn update(&mut self) {
        self.velocity.0 += self.acceleration.0;
        self.velocity.1 += self.acceleration.1;
        self.velocity.2 += self.acceleration.2;
        self.position.0 += self.velocity.0;
        self.position.1 += self.velocity.1;
        self.position.2 += self.velocity.2;
    }

    fn calculate_acceleration_magnitude(&self) -> f64 {
        ((self.acceleration.0.pow(2) + self.acceleration.1.pow(2) + self.acceleration.2.pow(2))
            as f64)
            .sqrt()
    }

    fn mark_destroyed_if_collide(&mut self, x: i32, y: i32, z: i32) {
        if self.position.0 == x && self.position.1 == y && self.position.2 == z {
            self.destroyed = true;
        }
    }
}

fn main() {
    let content = fs::read_to_string("../input").expect("file not found");
    let mut particles = Vec::new();

    let mut magnitudes = Vec::new();
    for line in content.lines() {
        let p_begin = line.find('<').unwrap();
        let p_end = line.find('>').unwrap();
        let position = &line[p_begin + 1..p_end];
        let mut position = position.split(',');

        let v_begin = &line[p_end + 1..].find('<').unwrap() + p_end + 1;
        let v_end = &line[p_end + 1..].find('>').unwrap() + p_end + 1;
        let velocity = &line[v_begin + 1..v_end];
        let mut velocity = velocity.split(',');

        let a_begin = &line[v_end + 1..].find('<').unwrap() + v_end + 1;
        let a_end = &line[v_end + 1..].find('>').unwrap() + v_end + 1;
        let acceleration = &line[a_begin + 1..a_end];
        let mut acceleration = acceleration.split(',');

        particles.push(Particle {
            position: (
                position.next().unwrap().parse().unwrap(),
                position.next().unwrap().parse().unwrap(),
                position.next().unwrap().parse().unwrap(),
            ),
            velocity: (
                velocity.next().unwrap().parse().unwrap(),
                velocity.next().unwrap().parse().unwrap(),
                velocity.next().unwrap().parse().unwrap(),
            ),
            acceleration: (
                acceleration.next().unwrap().parse().unwrap(),
                acceleration.next().unwrap().parse().unwrap(),
                acceleration.next().unwrap().parse().unwrap(),
            ),
            destroyed: false,
        });
        magnitudes.push(particles.last().unwrap().calculate_acceleration_magnitude());
    }

    let min_element = magnitudes
        .iter()
        .min_by(|x, y| {
            if x < y {
                return std::cmp::Ordering::Less;
            }
            return std::cmp::Ordering::Greater;
        }).unwrap();
    let min_index = magnitudes
        .iter()
        .position(|element| *element == *min_element)
        .unwrap();
    println!("{}", min_index);

    let mut number_of_particles = particles.len();
    for _ in 0..1_000 {
        for i in 0..number_of_particles {
            for j in 0..number_of_particles {
                if i != j {
                    let (x, y, z) = (
                        particles[j].position.0,
                        particles[j].position.1,
                        particles[j].position.2,
                    );
                    particles[i].mark_destroyed_if_collide(x, y, z);
                }
            }
        }

        particles = particles
            .into_iter()
            .filter(|ref i| !i.destroyed)
            .collect::<Vec<_>>();
        particles.iter_mut().for_each(|particle| particle.update());
        number_of_particles = particles.len();
        println!("{}", number_of_particles);
    }
}
