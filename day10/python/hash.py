#!/usr/bin/python3

import sys

lst = list(range(0, 256))
currentPosition = 0
skipSize = 0
size = len(lst)

input = [3]

#for i in input:
#    sublistEnd = currentPosition + i
#    if sublistEnd <= size:
#        sublist = lst[currentPosition:sublistEnd]
        #print(sublist, sublist[::-1])
#        sublist = sublist[::-1]
#        lst = lst[0:currentPosition] + sublist + lst[sublistEnd:]
#    else:
#        pass

#    currentPosition = currentPosition + i + skipSize
#    skipSize += 1

#print(lst)

input = [31,2,85,1,80,109,35,63,98,255,0,13,105,254,128,33]
for i in input:
    print('-----------------------------')
    #print('lst:', lst)
    print('i:', i, 'lst[', currentPosition, '] ->', lst[currentPosition])

    sublistEnd = currentPosition + i
    if sublistEnd <= size:
        sublist = lst[currentPosition:sublistEnd]
        #print('sublist:', sublist)
        #print(sublist, sublist[::-1])
        sublist = sublist[::-1]
        lst = lst[0:currentPosition] + sublist + lst[sublistEnd:]

    else:
        head = currentPosition
        headLength = size - head
        tail = i - headLength
        print('head:', head, 'tail:', tail, 'headLength:', headLength)
        sublist = lst[head + 1:] + lst[:tail]
        #if i == 5 or i == 4:
        #    print(sublistEnd - size)
        tail = sublistEnd - size
        sublist = lst[head:] + lst[:tail]
        #print('sublist:', sublist, 'reversed:', sublist[::-1])
        sublist = sublist[::-1]
        lst = sublist[headLength:] + lst[tail:head] + sublist[:headLength]


    currentPosition = (currentPosition + i + skipSize) % size

    skipSize += 1
    print('lst length:', len(lst))

print(lst[0] * lst[1])
