#!/usr/bin/python3

import sys

def removeGarbage(stream):
    hasGarbage = lambda s: s.find('<') > 0

    #stream = removeDoubleMarks(stream)
    stream = stream.replace('!!', '')
    #begin = findOpening(stream)
    #end = findClosing(stream)
    #cleared = stream[0:begin] + stream[end + 1:]
    while hasGarbage(stream):
        begin = stream.find('<')
        end = stream.find('>')
        while stream[end - 1] == '!' and stream[end - 2] != '!':
            #stream = stream[0:begin] + stream[end + 1:]
            end = stream.find('>', end + 1)

        stream = stream[0:begin] + stream[end + 1:]
        print(begin, end, len(stream))

    stream = stream.replace(',', '')
    return stream

def calculateScore(stream):
    score = 0
    current = 1
    for i in range(0, len(stream)):
        if stream[i] == '{':
            score += current
            current += 1
        elif stream[i] == '}':
            current -= 1
    return score

#stream = '{<a>,<a>,<a>,<a>}'
#stream = '{{{{{{},<!!a!>o!>!>,<!!!>"!>u!>,<e!!!>,<o"!!!!!!!>,<!>,<!!!>}>}}}}'

if len(sys.argv) != 2:
    print('Provide input file as command line argument!')
else:
    stream = open(sys.argv[1]).read()
    #stream = '{{<!!>},{<!!>},{<!!>},{<!!>}}'
    stream = removeGarbage(stream)
    print(calculateScore(stream))

#stream = removeDoubleMarks(stream)
#stream = removeGarbage(stream)
#print(stream)
