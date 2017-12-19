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
    posX = diagram[0].index('|')
    posY = 0
    letters = []
    steps = 0

    while True:
        if diagram[posY][posX] == ' ':
            break

        steps += 1

        if diagram[posY][posX].isalpha():
            letters.append(diagram[posY][posX])
            if direction == Direction.Down:
                posY += 1
            elif direction == Direction.Up:
                posY -= 1
            elif direction == Direction.Right:
                posX += 1
            elif direction == Direction.Left:
                posX -= 1
        elif diagram[posY][posX] == '+':
            if direction == Direction.Right or direction == Direction.Left:
                if diagram[posY + 1][posX] != ' ':
                    posY += 1
                    direction = Direction.Down
                elif diagram[posY - 1][posX] != ' ':
                    posY -= 1
                    direction = Direction.Up
            elif direction == Direction.Up or direction == Direction.Down:
                if diagram[posY][posX + 1] != ' ':
                    posX += 1
                    direction = Direction.Right
                elif diagram[posY][posX - 1] != ' ':
                    posX -= 1
                    direction = Direction.Left
        elif diagram[posY][posX] == '|' or diagram[posY][posX] == '-':
            if direction == Direction.Down:
                posY += 1
            elif direction == Direction.Up:
                posY -= 1
            elif direction == Direction.Right:
                posX += 1
            elif direction == Direction.Left:
                posX -= 1

    print('Collected letters:', ''.join(letters))
    print('Steps taken:', steps)
