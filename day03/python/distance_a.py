#!/usr/bin/python3

import math

class Spiral:
    def __init__(self):
        self.spiral = [[1]]
        self.highestValue = 1
        self.size = 1

    def extendTopRight(self):
        self.size += 1
        for row in self.spiral[::-1]:
            self.highestValue += 1
            row.append(self.highestValue)
        self.spiral.insert(0, list(reversed(range(self.highestValue + 1, self.highestValue + 1 + self.size))))
        self.highestValue += self.size

    def extendBottomLeft(self):
        self.size += 1
        for row in self.spiral:
            self.highestValue += 1
            row.insert(0, self.highestValue)
        self.spiral.append(list(range(self.highestValue + 1, self.highestValue + 1 + self.size)))
        self.highestValue += (self.size)

    def generateSpiral(self, target):
        targetSize = math.ceil(math.sqrt(target))
        self.extendTopRight()

        while self.size < targetSize:
            if self.spiral[0][0] == self.highestValue:
                self.extendBottomLeft()
            else:
                self.extendTopRight()

    def calculateDistance(self, target):
        self.generateSpiral(target)

        for i in range(0, len(self.spiral)):
            for j in range(0, len(self.spiral[i])):
                if self.spiral[i][j] == 1:
                    i_1, j_1 = i, j
                elif self.spiral[i][j] == target:
                    i_target, j_target = i, j
        distance = abs(i_1 - i_target) + abs(j_1 - j_target)
        return distance

    def printSpiral(self):
        for row in self.spiral:
            for column in row:
                print(column, end='\t')
            print()

spiral = Spiral()
print(spiral.calculateDistance(312051))

