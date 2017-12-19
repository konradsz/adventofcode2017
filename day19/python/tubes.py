#!/usr/bin/python3

import sys
from enum import Enum

class Direction(Enum):
    Up = 0,
    Down = 1,
    Right = 2,
    Left = 3


if len(sys.argv) != 2:
    print('Provide input file as command line argument!')
else:
    diagram = open(sys.argv[1]).read().splitlines()
    direction = Direction.Down
    posX, posY = diagram[0].index('|'), 0
    letters = []
    steps = 0

    while diagram[posY][posX] != ' ':
        steps += 1

        if diagram[posY][posX] == '+': # crossing
            if direction == Direction.Right or direction == Direction.Left:
                if diagram[posY + 1][posX] != ' ':
                    direction = Direction.Down
                    posY += 1
                elif diagram[posY - 1][posX] != ' ':
                    direction = Direction.Up
                    posY -= 1
            elif direction == Direction.Up or direction == Direction.Down:
                if diagram[posY][posX + 1] != ' ':
                    direction = Direction.Right
                    posX += 1
                elif diagram[posY][posX - 1] != ' ':
                    direction = Direction.Left
                    posX -= 1
        else:
            if diagram[posY][posX].isalpha(): # collect letters
                letters.append(diagram[posY][posX])

            if   direction == Direction.Down:  posY += 1
            elif direction == Direction.Up:    posY -= 1
            elif direction == Direction.Right: posX += 1
            elif direction == Direction.Left:  posX -= 1

    print('Collected letters:', ''.join(letters))
    print('Steps taken:', steps)

