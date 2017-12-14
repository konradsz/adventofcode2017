#!/usr/bin/python3

import sys
sys.path.append('../../day10/python')
from hash import Hash

input = 'oundnydw'
grid = []

squaresUsed = 0
for i in range(0, 128):
    hexRow = Hash().calculateHash(input + '-' + str(i))
    binRow = str()
    for hex in hexRow:
        binRow += '{0:04b}'.format(int(hex, 16))
    squaresUsed += binRow.count('1')
    grid.append(binRow)

print(squaresUsed)

