#!/usr/bin/python3

import sys

def countSteps(steps):
    steps_N = steps.count('n')
    steps_NE = steps.count('ne')
    steps_SE = steps.count('se')
    steps_S = steps.count('s')
    steps_SW = steps.count('sw')
    steps_NW = steps.count('nw')

    # REMOVE OPPOSITE STEPS
    s = min(steps_N, steps_S)
    steps_N -= s
    steps_S -= s

    s = min(steps_NE, steps_SW)
    steps_NE -= s
    steps_SW -= s

    s = min(steps_NW, steps_SE)
    steps_NW -= s
    steps_SE -= s

    # COMBINE STEPS
    s = min(steps_SW, steps_SE)
    steps_SW -= s
    steps_SE -= s
    steps_S += s

    s = min(steps_NW, steps_NE)
    steps_NW -= s
    steps_NE -= s
    steps_N += s

    s = min(steps_NE, steps_S)
    steps_NE -= s
    steps_S -= s
    steps_SE += s

    s = min(steps_SE, steps_N)
    steps_SE -= s
    steps_N -= s
    steps_NE += s

    s = min(steps_NW, steps_S)
    steps_NW -= s
    steps_S -= s
    steps_SW += s

    s = min(steps_SW, steps_N)
    steps_SW -= s
    steps_N -= s
    steps_NW += s

    return steps_N + steps_NE + steps_SE + steps_S + steps_SW + steps_NW

if len(sys.argv) != 2:
    print('Provide input file as command line argument!')
else:
    steps = (open(sys.argv[1]).read())[:-1].split(',')

    print(countSteps(steps))

    distances = []
    for i in range(0, len(steps)):
        distances.append(countSteps(steps[:i]))

    print(max(distances))

