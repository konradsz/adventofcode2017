#!/usr/bin/python3

import sys

if len(sys.argv) != 2:
    print('Provide input file as command line argument!')
else:
    maze = [int(number) for number in open(sys.argv[1]).read().splitlines()]
    mazeLength = len(maze)
    currentPos = 0
    steps = 0
    while currentPos < mazeLength:
        move = maze[currentPos]
        maze[currentPos] += 1
        currentPos += move
        steps += 1

    print(steps)
