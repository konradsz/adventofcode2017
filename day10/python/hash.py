#!/usr/bin/python3

class Hash:
    def __init__(self, lst):
        self.lst = lst
        self.currentPosition = 0
        self.skipSize = 0
        self.size = len(lst)

    def reorderList(self, inputLengths):
        for length in inputLengths:
            sublistEnd = self.currentPosition + length
            if sublistEnd <= self.size:
                sublist = (self.lst[self.currentPosition:sublistEnd])[::-1]
                self.lst = self.lst[0:self.currentPosition] + sublist + self.lst[sublistEnd:]
            else:
                head = self.currentPosition
                headLength = self.size - head
                tail = sublistEnd - self.size
                sublist = (self.lst[head:] + self.lst[:tail])[::-1]
                self.lst = sublist[headLength:] + self.lst[tail:head] + sublist[:headLength]

            self.currentPosition = (self.currentPosition + length + self.skipSize) % self.size
            self.skipSize += 1

    def calculateHash(self):
        hash = str()
        for i in range(0, 16):
            x = self.lst[i * 16]
            for j in range(i * 16 + 1, i * 16 + 16):
                x ^= self.lst[j]
            hash += '{:02x}'.format(int(x))

        print('Hash:', hash)

def getInputLengths(input):
    lengths = [ord(char) for char in input]
    fixedLengths = [17, 31, 73, 47, 23]
    return lengths + fixedLengths

hash1 = Hash(list(range(0, 256)))
input = [31,2,85,1,80,109,35,63,98,255,0,13,105,254,128,33]
hash1.reorderList(input)
print('Multiplication of two first elements:', hash1.lst[0] * hash1.lst[1])

hash2 = Hash(list(range(0, 256)))
input = getInputLengths('31,2,85,1,80,109,35,63,98,255,0,13,105,254,128,33')
for _ in range(0, 64):
    hash2.reorderList(input)
hash2.calculateHash()
