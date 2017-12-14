#!/usr/bin/python3

import sys
sys.path.append('../../day10/python')
from hash import Hash

input = 'oundnydw'

def markNeighbour(grid, x, y, group):
    if x >= 1 and grid[y][x - 1] == -1: # left neighbour
        grid[y][x - 1] = group
        markNeighbour(grid, x - 1, y, group)
    if x < len(grid[y]) - 1 and grid[y][x + 1] == -1: # right neighbour
        grid[y][x + 1] = group
        markNeighbour(grid, x + 1, y, group)
    if y >= 1 and grid[y - 1][x] == -1: # top neighbour
        grid[y - 1][x] = group
        markNeighbour(grid, x, y - 1, group)
    if y < len(grid) - 1 and grid[y + 1][x] == -1: # bottom neighbour
        grid[y + 1][x] = group
        markNeighbour(grid, x, y + 1, group)

def findGroups(grid):
    nextGroupNumber = 0

    for y in range(0, len(grid)):
        for x in range(0, len(grid[y])):
            if grid[y][x] == -1:
                nextGroupNumber += 1
                #print(x, y)
                grid[y][x] = nextGroupNumber
                markNeighbour(grid, x, y, nextGroupNumber)

    return nextGroupNumber

squaresUsed = 0
binGrid = []
for i in range(0, 128):
    hexRow = Hash().calculateHash(input + '-' + str(i))
    binRow = str()
    for hex in hexRow:
        binRow += '{0:04b}'.format(int(hex, 16))
    squaresUsed += binRow.count('1')
    binGrid.append(binRow)

print('Used squares:', squaresUsed)
print('Number of groups:',
      findGroups([[-1 if x == '1' else 0 for x in y] for y in binGrid]))

