#!/usr/bin/python3

import sys

def spin(input, size):
    input = input[-size:] + input[:-size]
    return input

def exchange(input, pos1, pos2):
    input[pos1], input[pos2] = input[pos2], input[pos1]
    return input

def partner(input, program1, program2):
    pos1 = input.index(program1)
    pos2 = input.index(program2)
    input[pos1], input[pos2] = input[pos2], input[pos1]
    return input

programs = list('abcdefghijklmnop')
starting = list(programs)

if len(sys.argv) != 2:
    print('Provide input file as command line argument!')
else:
    steps = open(sys.argv[1]).read().strip().split(',')
    ops = []

    for step in steps:
        if step[0] == 's': # spin
            size = int(step[1:])
            ops.append(lambda prg, size = size: spin(prg, size))
        elif step[0] == 'x': # exchange
            values = step[1:]
            val1, val2 = int(values[:values.index('/')]), int(values[values.index('/') + 1:])
            ops.append(lambda prg, val1 = val1, val2 = val2: exchange(prg, val1, val2))
        elif step[0] == 'p': # partner
            values = step[1:]
            val1, val2 = values[:values.index('/')], values[values.index('/') + 1:]
            ops.append(lambda prg, val1 = val1, val2 = val2: partner(prg, val1, val2))

    seen = [''.join(programs)]
    for i in range(1000000000):
        for op in ops:
            programs = op(programs)

        if i == 0:
            print('After first dance:', ''.join(programs))

        if programs == starting: # found cycle
            programs = seen[1000000000 % (i + 1)]
            break
        else:
            seen.append(''.join(programs))

print('After 1 bilion dances:', programs)
