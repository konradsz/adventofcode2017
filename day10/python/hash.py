#!/usr/bin/python3

import sys

class Hash:
    def __init__(self, lst):
        self.lst = lst
        self.currentPosition = 0
        self.skipSize = 0
        self.size = len(lst)

    def reorderList(self, inputLengths):
        for length in inputLengths:
            print('-----------------------------')
            #print('lst:', lst)
            print('i:', length, 'lst[', self.currentPosition, '] ->', lst[self.currentPosition])

            sublistEnd = self.currentPosition + length
            if sublistEnd <= self.size:
                sublist = self.lst[self.currentPosition:sublistEnd]
                #print('sublist:', sublist)
                #print(sublist, sublist[::-1])
                sublist = sublist[::-1]
                self.lst = self.lst[0:self.currentPosition] + sublist + self.lst[sublistEnd:]

            else:
                head = self.currentPosition
                headLength = self.size - head
                tail = length - headLength
                print('head:', head, 'tail:', tail, 'headLength:', headLength)
                sublist = self.lst[head + 1:] + self.lst[:tail]
                tail = sublistEnd - self.size
                sublist = self.lst[head:] + self.lst[:tail]
                #print('sublist:', sublist, 'reversed:', sublist[::-1])
                sublist = sublist[::-1]
                self.lst = sublist[headLength:] + self.lst[tail:head] + sublist[:headLength]


            self.currentPosition = (self.currentPosition + length + self.skipSize) % self.size

            self.skipSize += 1
            print('lst length:', len(self.lst))
        print(self.lst[0] * self.lst[1])

lst = list(range(0, 256))
hash = Hash(lst)
input = [31,2,85,1,80,109,35,63,98,255,0,13,105,254,128,33]
hash.reorderList(input)
