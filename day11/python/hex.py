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
    while steps_N > 0 and steps_S > 0:
        steps_N -= 1
        steps_S -= 1

    while steps_NE > 0 and steps_SW > 0:
        steps_NE -= 1
        steps_SW -= 1

    while steps_NW > 0 and steps_SE > 0:
        steps_NW -= 1
        steps_SE -= 1

    # COMBINE STEPS
    while steps_SW > 0 and steps_SE > 0:
        steps_SW -= 1
        steps_SE -= 1
        steps_S += 1

    while steps_NW > 0 and steps_NE > 0:
        steps_NW -= 1
        steps_NE -= 1
        steps_N += 1

    while steps_NE > 0 and steps_S > 0:
        steps_NE -= 1
        steps_S -= 1
        steps_SE += 1

    while steps_SE > 0 and steps_N > 0:
        steps_SE -= 1
        steps_N -= 1
        steps_NE += 1

    while steps_NW > 0 and steps_S > 0:
        steps_NW -= 1
        steps_S -= 1
        steps_SW += 1

    while steps_SW > 0 and steps_N > 0:
        steps_SW -= 1
        steps_N -= 1
        steps_NW += 1

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

