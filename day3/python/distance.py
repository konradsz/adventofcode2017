#!/usr/bin/python3

spiral = [[1]]
highestValue = 1
size = 2

def calculateSize(target):
    size2 = 3;
    while pow(size2, 2) < target:
        size2 += 1

    return size2

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

        self.spiral = [list(reversed(range(self.highestValue + 1, self.highestValue + 1 + self.size)))] + self.spiral
        self.highestValue += self.size

    def extendBottomLeft(self):
        self.size += 1
        for row in self.spiral:
            self.highestValue += 1
            row.insert(0, self.highestValue)

        self.spiral.append(list(range(self.highestValue + 1, self.highestValue + 1 + self.size)))
        self.highestValue += (self.size)


    def printSpiral(self):
        for row in self.spiral:
            for column in row:
                print(column, end='\t')
            print()

    def generateSpiral(self, target):
        a = calculateSize(target)
        self.extendTopRight()

        #print(list(range(3, a + 1)))
        #for i in range(2, a):
        #    if spiral[0][0] == highestValue:
        #        extendBottomLeft()
        #    else:
        #        extendTopRight()
        while self.size < a:
            if self.spiral[0][0] == self.highestValue:
                self.extendBottomLeft()
            else:
                self.extendTopRight()
        print(self.calculateDistance(target))

    def calculateDistance(self, target):
        i_1 = 0
        j_1 = 0
        i_target = 0
        j_target = 0
        for i in range(0, len(self.spiral)):
            for j in range(0, len(self.spiral[i])):
                if self.spiral[i][j] == 1:
                    i_1 = i
                    j_1 = j
                elif self.spiral[i][j] == target:
                    i_target = i
                    j_target = j
        distance = abs(i_1 - i_target) + abs(j_1 - j_target)
        return distance


def calculateSize(target):
    size = 3;
    while pow(size, 2) < target:
        size += 1

    return size

def extendTopRight():
    global spiral #LEGB ???
    global highestValue
    global size

    for row in spiral[::-1]:
        highestValue += 1
        row.append(highestValue)

    spiral = [list(reversed(range(highestValue + 1, highestValue + 1 + size)))] + spiral
    highestValue += size

def extendBottomLeft():
    global spiral #LEGB ???
    global highestValue
    global size

    for row in spiral:
        highestValue += 1
        row.insert(0, highestValue)

    spiral.append(list(range(highestValue + 1, highestValue + 1 + size)))
    highestValue += size

#def generateSpiral():
#    pass

def printSpiral():
    for row in spiral:
        for column in row:
            print(column, end='\t')
        print()

#generateSpiral()

#extendTopRight()
#size += 1
#extendBottomLeft()
#size += 1
#extendTopRight()
#size += 1
#extendBottomLeft()
#size += 1
#extendTopRight()
#printSpiral()
#print(spiral)

spiral2 = Spiral()
spiral2.generateSpiral(312051)
#spiral2.printSpiral()
