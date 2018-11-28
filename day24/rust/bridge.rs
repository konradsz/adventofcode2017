use std::fs;

fn build_bridge(
    bridges: &mut Vec<(usize, usize)>,
    components: &Vec<(usize, usize)>,
    port: usize,
    strenght: usize,
    length: usize,
) {
    bridges.push((strenght, length));
    let connectors: Vec<usize> = components
        .iter()
        .filter(|component| component.0 == port || component.1 == port)
        .map(|component| {
            if component.0 == port {
                component.1
            } else {
                component.0
            }
        }).collect();

    for connector in connectors {
        let index = components
            .iter()
            .position(|component| {
                (component.0 == connector && component.1 == port)
                    || (component.0 == port && component.1 == connector)
            }).unwrap();
        let mut reduced_components = components.to_vec();
        reduced_components.remove(index);

        let calculate_strength = |component: (usize, usize)| component.0 + component.1 + strenght;
        build_bridge(
            bridges,
            &reduced_components,
            connector,
            calculate_strength(components[index]),
            length + 1,
        );
    }
}

fn main() {
    let content = fs::read_to_string("../input").expect("file not found");
    let mut components = Vec::new();
    let mut bridges = Vec::new();

    for line in content.lines() {
        let mut ports = line.split('/');
        components.push((
            ports.next().unwrap().parse::<usize>().unwrap(),
            ports.next().unwrap().parse::<usize>().unwrap(),
        ));
    }

    build_bridge(&mut bridges, &components, 0, 0, 0);

    let max_strenght = bridges
        .iter()
        .max_by(|&bridge_1, &bridge_2| (*bridge_1).0.cmp(&bridge_2.0))
        .unwrap()
        .0;
    println!("{}", max_strenght);

    let strenght_of_the_longest = bridges
        .iter()
        .max_by(|&bridge_1, &bridge_2| (*bridge_1).1.cmp(&bridge_2.1))
        .unwrap()
        .0;
    println!("{}", strenght_of_the_longest);
}
