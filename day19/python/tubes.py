#!/usr/bin/python3

import sys
from operator import add

directions = {'up': (0, -1), 'down': (0, 1), 'right': (1, 0), 'left': (-1, 0)}

if len(sys.argv) != 2:
    print('Provide input file as command line argument!')
else:
    diagram = open(sys.argv[1]).read().splitlines()
    direction = directions['down']
    pos = diagram[0].index('|'), 0
    letters = []
    steps = 0

    while not diagram[pos[1]][pos[0]].isspace():
        if diagram[pos[1]][pos[0]].isalpha(): # collect letters
            letters.append(diagram[pos[1]][pos[0]])

        if diagram[pos[1]][pos[0]] == '+': # crossing, change direction
            if direction == directions['right'] or direction == directions['left']:
                if not diagram[pos[1] + 1][pos[0]].isspace():
                    direction = directions['down']
                elif not diagram[pos[1] - 1][pos[0]].isspace():
                    direction = directions['up']
            elif direction == directions['up'] or direction == directions['down']:
                if not diagram[pos[1]][pos[0] + 1].isspace():
                    direction = directions['right']
                elif not diagram[pos[1]][pos[0] - 1].isspace():
                    direction = directions['left']

        pos = tuple(map(add, pos, direction))
        steps += 1

    print('Collected letters:', ''.join(letters))
    print('Steps taken:', steps)

