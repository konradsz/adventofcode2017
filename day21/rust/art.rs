use std::collections::HashMap;

fn get_next_size(size: usize) -> usize {
    if size % 2 == 0 {
        let width = size / 2;
        width * 3
    } else {
        let width = size / 3;
        width * 4
    }
}

fn flip(pattern: &Vec<Vec<char>>) -> Vec<Vec<char>> {
    pattern.iter().cloned().rev().collect::<Vec<Vec<char>>>()
}

fn rotate(pattern: &Vec<Vec<char>>) -> Vec<Vec<char>> {
    let size = pattern.len();
    let mut output = Vec::new();

    for i in 0..size {
        let mut output_row = Vec::new();
        for j in (0..size).rev() {
            output_row.push(pattern[j][i]);
        }
        output.push(output_row);
    }
    output
}

fn split_into_cells(pattern: &str, size: usize) -> Vec<String> {
    let mut output = Vec::new();
    if size % 2 == 0 {
        const CELL_SIZE: usize = 2;
        let width = size / 2;
        let height = width;

        for row in 0..height {
            let row_cells = &pattern[row * width * CELL_SIZE * CELL_SIZE
                ..(width * CELL_SIZE * CELL_SIZE) + row * width * CELL_SIZE * CELL_SIZE];
            for cell_in_row in 0..width {
                let cell_offset = cell_in_row * CELL_SIZE;
                let row_offset_1 = 0 * width * CELL_SIZE;
                let row_offset_2 = 1 * width * CELL_SIZE;

                let rows = vec![
                    &row_cells[row_offset_1 + cell_offset..row_offset_1 + cell_offset + CELL_SIZE],
                    &row_cells[row_offset_2 + cell_offset..row_offset_2 + cell_offset + CELL_SIZE],
                ];

                output.push(rows.join("\n"));
            }
        }
    } else {
        const CELL_SIZE: usize = 3;
        let width = size / 3;
        let height = width;

        for row in 0..height {
            let row_cells = &pattern[row * width * CELL_SIZE * CELL_SIZE
                ..(width * CELL_SIZE * CELL_SIZE) + row * width * CELL_SIZE * CELL_SIZE];
            for cell_in_row in 0..width {
                let cell_offset = cell_in_row * CELL_SIZE;
                let row_offset_1 = 0 * width * CELL_SIZE;
                let row_offset_2 = 1 * width * CELL_SIZE;
                let row_offset_3 = 2 * width * CELL_SIZE;

                let rows = vec![
                    &row_cells[row_offset_1 + cell_offset..row_offset_1 + cell_offset + CELL_SIZE],
                    &row_cells[row_offset_2 + cell_offset..row_offset_2 + cell_offset + CELL_SIZE],
                    &row_cells[row_offset_3 + cell_offset..row_offset_3 + cell_offset + CELL_SIZE],
                ];

                output.push(rows.join("\n"));
            }
        }
    }

    output
}

fn transform(input: &Vec<Vec<char>>, book: &HashMap<String, String>) -> String {
    let convert_to_string = |pattern: &Vec<Vec<char>>| {
        let mut pattern_as_string = String::new();
        for row in pattern.iter() {
            let r: String = row.iter().collect();
            pattern_as_string.push_str(&r);
        }
        pattern_as_string
    };

    let mut pattern = input.clone();
    loop {
        if let Some(to) = book.get(&convert_to_string(&pattern)) {
            return String::from(to);
        }

        if let Some(to) = book.get(&convert_to_string(&flip(&pattern))) {
            return String::from(to);
        }

        pattern = rotate(&pattern);
    }
}

fn merge_cells(cells: &Vec<String>) -> String {
    let width = ((cells.len() as f64).sqrt()) as usize;
    let cell_size = ((cells[0].len() as f64).sqrt()) as usize;

    let mut output = vec![String::new(); width * cell_size];
    for (row_index, row) in cells.chunks(width).enumerate() {
        for element in row.iter() {
            for (column_index, ch) in element.as_bytes().chunks(cell_size).enumerate() {
                for c in ch.iter() {
                    output[row_index * cell_size + column_index].push(*c as char);
                }
            }
        }
    }

    output.join("")
}

fn main() {
    let mut pattern = String::from(".#...####");
    let mut size = 3;

    let mut book = HashMap::new();
    book.insert("....".to_string(), "#.##.....".to_string());
    book.insert("#...".to_string(), "#.##.#.#.".to_string());
    book.insert("##..".to_string(), "#...####.".to_string());
    book.insert(".##.".to_string(), "..#..#..#".to_string());
    book.insert("###.".to_string(), "##..#.#..".to_string());
    book.insert("####".to_string(), "....#..#.".to_string());
    book.insert(".........".to_string(), "..#.##.##.####.#".to_string());
    book.insert("#........".to_string(), "#.##....##..###.".to_string());
    book.insert(".#.......".to_string(), "##.####.#.###.#.".to_string());
    book.insert("##.......".to_string(), "##.##.##.#..##.#".to_string());
    book.insert("#.#......".to_string(), "...#..#..#.#.###".to_string());
    book.insert("###......".to_string(), "....#..##.####..".to_string());
    book.insert(".#.#.....".to_string(), ".#...#.#..#..###".to_string());
    book.insert("##.#.....".to_string(), "..###.###...#.#.".to_string());
    book.insert("..##.....".to_string(), ".##.#.##.#..##..".to_string());
    book.insert("#.##.....".to_string(), "#....##....####.".to_string());
    book.insert(".###.....".to_string(), "#.##..##.#.###..".to_string());
    book.insert("####.....".to_string(), "#..#...#..#....#".to_string());
    book.insert("....#....".to_string(), ".###.#....#.####".to_string());
    book.insert("#...#....".to_string(), "#####....#####..".to_string());
    book.insert(".#..#....".to_string(), "#####..######..#".to_string());
    book.insert("##..#....".to_string(), ".#....##..###..#".to_string());
    book.insert("#.#.#....".to_string(), ".#.##.###.#..#.#".to_string());
    book.insert("###.#....".to_string(), "#.###...###.#..#".to_string());
    book.insert(".#.##....".to_string(), "###.#........###".to_string());
    book.insert("##.##....".to_string(), "#.#####....####.".to_string());
    book.insert("..###....".to_string(), ".#.####...#.#...".to_string());
    book.insert("#.###....".to_string(), "#.#.##..##....##".to_string());
    book.insert(".####....".to_string(), "......#..##..#.#".to_string());
    book.insert("#####....".to_string(), "#....#..#.#.#..#".to_string());
    book.insert("...#.#...".to_string(), "##..#.##.##..##.".to_string());
    book.insert("#..#.#...".to_string(), "#.#.##.#.###.###".to_string());
    book.insert(".#.#.#...".to_string(), "....########.#.#".to_string());
    book.insert("##.#.#...".to_string(), "#.##.#####..#...".to_string());
    book.insert("#.##.#...".to_string(), "###...###.#.####".to_string());
    book.insert("####.#...".to_string(), ".##.....###.....".to_string());
    book.insert("...###...".to_string(), "###..##.##...###".to_string());
    book.insert("#..###...".to_string(), ".#..#...###....#".to_string());
    book.insert(".#.###...".to_string(), "#.#.#.#.#######.".to_string());
    book.insert("##.###...".to_string(), "...###..###.#.#.".to_string());
    book.insert("#.####...".to_string(), ".#.##.#...#..##.".to_string());
    book.insert("######...".to_string(), "....#.##...###..".to_string());
    book.insert("..#...#..".to_string(), "...##.###..#..##".to_string());
    book.insert("#.#...#..".to_string(), "..#.##.#.#.#..##".to_string());
    book.insert(".##...#..".to_string(), "..####..#.#.#.##".to_string());
    book.insert("###...#..".to_string(), "#.#####....#.##.".to_string());
    book.insert(".###..#..".to_string(), "##..#.####.###..".to_string());
    book.insert("####..#..".to_string(), "#.####...##..#.#".to_string());
    book.insert("..#.#.#..".to_string(), "#..###...####.#.".to_string());
    book.insert("#.#.#.#..".to_string(), ".####.###.#.####".to_string());
    book.insert(".##.#.#..".to_string(), "#.#.#...#.##...#".to_string());
    book.insert("###.#.#..".to_string(), ".##..#.##.#..#.#".to_string());
    book.insert(".####.#..".to_string(), ".###.#.#...##.#.".to_string());
    book.insert("#####.#..".to_string(), ".####.###.###.#.".to_string());
    book.insert("#....##..".to_string(), "#...##...##.###.".to_string());
    book.insert(".#...##..".to_string(), "#...#.###...###.".to_string());
    book.insert("##...##..".to_string(), "####....##.#.###".to_string());
    book.insert("#.#..##..".to_string(), "..####.##.###..#".to_string());
    book.insert(".##..##..".to_string(), "..#.##.##.#...##".to_string());
    book.insert("###..##..".to_string(), "..##...##..##..#".to_string());
    book.insert("#..#.##..".to_string(), "#.......#...#.##".to_string());
    book.insert(".#.#.##..".to_string(), "##..####.#.###..".to_string());
    book.insert("##.#.##..".to_string(), ".#......#....##.".to_string());
    book.insert("..##.##..".to_string(), ".#...#.#.#.#..#.".to_string());
    book.insert("#.##.##..".to_string(), "..#.#.###.#...##".to_string());
    book.insert(".###.##..".to_string(), "#.##..##...#####".to_string());
    book.insert("####.##..".to_string(), ".##..#.####.#..#".to_string());
    book.insert("#...###..".to_string(), "..##.###.#..##.#".to_string());
    book.insert(".#..###..".to_string(), "#.##.##..##..###".to_string());
    book.insert("##..###..".to_string(), ".##..#........##".to_string());
    book.insert("#.#.###..".to_string(), "....#.#.##.####.".to_string());
    book.insert(".##.###..".to_string(), "#..#....##.#..#.".to_string());
    book.insert("###.###..".to_string(), "######.##..###..".to_string());
    book.insert("#..####..".to_string(), "#.#.###..####...".to_string());
    book.insert(".#.####..".to_string(), "##.##..##.##..#.".to_string());
    book.insert("##.####..".to_string(), "..#....#..##...#".to_string());
    book.insert("..#####..".to_string(), ".#.#......##..##".to_string());
    book.insert("#.#####..".to_string(), "#..#..#..#....#.".to_string());
    book.insert(".######..".to_string(), ".#.#....#..#...#".to_string());
    book.insert("#######..".to_string(), "#.####...#......".to_string());
    book.insert(".#.#.#.#.".to_string(), "....####.###.#.#".to_string());
    book.insert("##.#.#.#.".to_string(), "#.##...#########".to_string());
    book.insert("#.##.#.#.".to_string(), "..#.##......#...".to_string());
    book.insert("####.#.#.".to_string(), "#####.#####....#".to_string());
    book.insert(".#.###.#.".to_string(), "...#..#....#..#.".to_string());
    book.insert("##.###.#.".to_string(), ".##.#....#.#.###".to_string());
    book.insert("#.####.#.".to_string(), ".........#.##.##".to_string());
    book.insert("######.#.".to_string(), "..#.###.##.#....".to_string());
    book.insert("#.#..###.".to_string(), ".###.#....#.####".to_string());
    book.insert("###..###.".to_string(), "#.##..#.#..#....".to_string());
    book.insert(".###.###.".to_string(), "#...##..####.##.".to_string());
    book.insert("####.###.".to_string(), "###...#...#.##..".to_string());
    book.insert("#.#.####.".to_string(), "#...##..##.##.##".to_string());
    book.insert("###.####.".to_string(), "..#.#..##.######".to_string());
    book.insert(".#######.".to_string(), ".#.#.###...#.#..".to_string());
    book.insert("########.".to_string(), "####.....#.#...#".to_string());
    book.insert("#.#...#.#".to_string(), "##.##..#.##....#".to_string());
    book.insert("###...#.#".to_string(), "#.#..#.....#...#".to_string());
    book.insert("####..#.#".to_string(), ".#.#.#..##..##..".to_string());
    book.insert("#.#.#.#.#".to_string(), "###.#...####.#.#".to_string());
    book.insert("###.#.#.#".to_string(), "##..#.#...####.#".to_string());
    book.insert("#####.#.#".to_string(), "####....###..##.".to_string());
    book.insert("#.##.##.#".to_string(), "...#.##.##...###".to_string());
    book.insert("####.##.#".to_string(), "..#..##.##.#.#..".to_string());
    book.insert("#.#####.#".to_string(), "...#......#....#".to_string());
    book.insert("#######.#".to_string(), "#.#.#.#.##......".to_string());
    book.insert("####.####".to_string(), "#...##.#.#....#.".to_string());
    book.insert("#########".to_string(), "##....#.##....#.".to_string());

    let count_on = |pattern: &str| -> usize { pattern.chars().filter(|c| *c == '#').count() };
    for _ in 0..18 {
        let cells = split_into_cells(&pattern, size);

        pattern.clear();
        let mut cells_strings = Vec::new();
        for cell in cells.iter() {
            let mut cell_chars = Vec::new();
            let rows: Vec<&str> = cell.split_whitespace().collect();
            for row in rows.iter() {
                let row_chars: Vec<char> = row.chars().collect();
                cell_chars.push(row_chars);
            }
            let output = transform(&cell_chars, &book);
            pattern.push_str(&output);
            cells_strings.push(output);
        }

        size = get_next_size(size);
        pattern = merge_cells(&cells_strings);
        println!("{}", count_on(&pattern));
    }
}
