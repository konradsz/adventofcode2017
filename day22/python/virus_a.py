#!/usr/bin/python3

import sys
import math
from operator import add

dirs = {'up': (0, -1), 'down': (0, 1), 'right': (1, 0), 'left': (-1, 0)}

leftTurns = {dirs['up']:    dirs['left'],
             dirs['right']: dirs['up'],
             dirs['down']:  dirs['right'],
             dirs['left']:  dirs['down']}

rightTurns = {dirs['up']:    dirs['right'],
              dirs['right']: dirs['down'],
              dirs['down']:  dirs['left'],
              dirs['left']:  dirs['up']}

def extend(grid):
    size = len(grid)
    newGrid = ['.' * (size + 2)]
    for row in grid:
        newRow = '.' + row + '.'
        newGrid.append(newRow)
    newGrid.append('.' * (size + 2))
    return newGrid

if len(sys.argv) != 2:
    print('Provide input file as command line argument!')
else:
    grid = open(sys.argv[1]).read().splitlines()
    middle = math.ceil(len(grid) / 2)
    direction = dirs['up']
    position = (middle - 1, middle - 1)

    counter = 0
    for _ in range(10000):
        if grid[position[1]][position[0]] == '#':
            direction = rightTurns[direction]
            row = list(grid[position[1]])
            row[position[0]] = '.'
            grid[position[1]] = ''.join(row)
        elif grid[position[1]][position[0]] == '.':
            direction = leftTurns[direction]
            row = list(grid[position[1]])
            row[position[0]] = '#'
            grid[position[1]] = ''.join(row)
            counter += 1

        position = tuple(map(add, position, direction))
        if (position[0] == len(grid) or position[1] == len(grid) or
            position[0] < 0 or position[1] < 0):
            grid = extend(grid)
            position = tuple(map(add, position, (1, 1)))

    print('Bursts that caused a node to become infected:', counter)

