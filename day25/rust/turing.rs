enum State {
    A,
    B,
    C,
    D,
    E,
    F,
}

fn step(
    tape: &mut Vec<u32>,
    state: &mut State,
    position: &mut usize,
    value: (u32, u32),
    movement: (i32, i32),
    new_state: (State, State),
) {
    let mut pos = *position as i32;
    if tape[*position] == 0 {
        tape[*position] = value.0;
        pos += movement.0;
        *state = new_state.0;
    } else if tape[*position] == 1 {
        tape[*position] = value.1;
        pos += movement.1;
        *state = new_state.1;
    }

    if pos == tape.len() as i32 {
        tape.push(0);
    } else if pos < 0 {
        tape.insert(0, 0);
        pos += 1;
    }

    *position = pos as usize;
}

fn main() {
    let mut tape = vec![0];
    let mut state = State::A;
    let mut position: usize = 0;

    for _ in 0..12134527 {
        match state {
            State::A => step(
                &mut tape,
                &mut state,
                &mut position,
                (1, 0),
                (1, -1),
                (State::B, State::C),
            ),
            State::B => step(
                &mut tape,
                &mut state,
                &mut position,
                (1, 1),
                (-1, 1),
                (State::A, State::C),
            ),
            State::C => step(
                &mut tape,
                &mut state,
                &mut position,
                (1, 0),
                (1, -1),
                (State::A, State::D),
            ),
            State::D => step(
                &mut tape,
                &mut state,
                &mut position,
                (1, 1),
                (-1, -1),
                (State::E, State::C),
            ),
            State::E => step(
                &mut tape,
                &mut state,
                &mut position,
                (1, 1),
                (1, 1),
                (State::F, State::A),
            ),
            State::F => step(
                &mut tape,
                &mut state,
                &mut position,
                (1, 1),
                (1, 1),
                (State::A, State::E),
            ),
        }
    }

    println!("{}", tape.iter().filter(|&value| *value == 1).count());
}
