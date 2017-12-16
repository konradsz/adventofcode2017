#!/usr/bin/python3

import sys

#programs = ['a', 'b', 'c', 'd', 'e']

def spin(input, size):
    return input[-size:] + input[:-size]

def exchange(input, pos1, pos2):
    input[pos1], input[pos2] = input[pos2], input[pos1]
    return input

def partner(input, program1, program2):
    pos1 = input.index(program1)
    pos2 = input.index(program2)
    input[pos1], input[pos2] = input[pos2], input[pos1]
    return input

#programs = ['a', 'b', 'c', 'd', 'e']
#programs = spin(programs, 1)
#programs = exchange(programs, 3, 4)
#programs = partner(programs, 'e', 'b')
#print(programs)

programs = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p']
#programs = ['a', 'b', 'c', 'd', 'e']

if len(sys.argv) != 2:
    print('Provide input file as command line argument!')
else:
    steps = open(sys.argv[1]).read().strip().split(',')
    ops = []

    for step in steps:
        if step[0] == 's': # spin
            size = int(step[1:])
            #print('spin', size)
            ops.append(lambda prg, size = size: spin(prg, size))
        elif step[0] == 'x': # exchange
            values = step[1:]
            val1, val2 = int(values[:values.index('/')]), int(values[values.index('/') + 1:])
            #print('exchange', val1, val2)
            ops.append(lambda prg, val1 = val1, val2 = val2: exchange(prg, val1, val2))
        elif step[0] == 'p': # partner
            values = step[1:]
            val1, val2 = values[:values.index('/')], values[values.index('/') + 1:]
            #print('parnter', val1, val2)
            ops.append(lambda prg, val1 = val1, val2 = val2: partner(prg, val1, val2))

    #for _ in range(1):
    #    for step in steps:
    #        if step[0] == 's': # spin
    #            size = int(step[1:])
    #            programs = spin(programs, size)
    #        if step[0] == 'x': # exchange
    #            values = step[1:]
    #            val1, val2 = int(values[:values.index('/')]), int(values[values.index('/') + 1:])
    #            exchange(programs, val1, val2)
    #        if step[0] == 'p': # partner
    #            values = step[1:]
    #            val1, val2 = values[:values.index('/')], values[values.index('/') + 1:]
    #            partner(programs, val1, val2)

    for _ in range(10000):
        for op in ops:
            programs = op(programs)
print(''.join(programs))
    #opz = []
    #for i in range(5):
    #    opz.append(lambda i = i: print(i))

    #for op in opz:
    #    op()
