#!/usr/bin/python3

import sys

rules = []

def flipH(square):
    return square[::-1]

def flipV(square):
    return [row[::-1] for row in square]

def rotate(square):
    return list(map(''.join, zip(*square[::-1])))

def enhance(pattern, ss):
    size = len(pattern)
    rs = int(size / ss)
    print('ss', ss, 'rs', rs)
    newSquares = []
    print('pattern', pattern, list(range(2)))
    for i in range(rs):
        for j in range(rs):
            square = [s[j * ss:j * ss + ss] for s in pattern[i * ss:i * ss + ss]]
            print('square', square, 'i', i, 'j', j)

            # make it better, add all flips for each rotation
            possibilities = [square, flipV(square), flipH(square), flipV(flipH(square))]
            rotated = square
            for _ in range(3):
                rotated = rotate(rotated)
                if rotated not in possibilities:
                    possibilities.append(rotated)
                if flipV(rotated) not in possibilities:
                    possibilities.append(flipV(rotated))
                if flipH(rotated) not in possibilities:
                    possibilities.append(flipH(rotated))

            #print(len(possibilities))
            for rule in rules:
                for possibility in possibilities:
                    print(rule[0], possibility)
                    if rule[0] == possibility:
                        #new = rule[1]
                        newSquares.append(rule[1])

    print('newSquares len:', len(newSquares))
    print(newSquares)
    pattern = []
    #for i in range(rs):
    #    row = []
    #    for j in range(rs):
    #        pass

    return pattern

if len(sys.argv) != 2:
    print('Provide input file as command line argument!')
else:
    file = open(sys.argv[1]).read().splitlines()
    for entry in file:
        rule = entry.split(' => ')
        in_ = rule[0].split('/')
        out_ = rule[1].split('/')
        rules.append((in_, out_))

    #pattern = ['.#.',
    #           '..#',
    #           '###']
    pattern = ['#..#',
               '....',
               '....',
               '#..#']

    for _ in range(1):
        size = len(pattern)
        print('size', size)
        if size % 2 == 0:
            pattern = enhance(pattern, 2)
        elif size % 3 == 0:
            pattern = enhance(pattern, 3)

    #print(pattern)

     #= ['A.B', 'E.F', 'I.J', 'C.D', 'G.H', 'K.L', 'M.N', 'Q.R', 'U.V', 'O.P', 'S.T', 'W.Z']
    dupa = [['##.', '#..', '...'], ['##.', '#..', '...'], ['##.', '#..', '...'], ['##.', '#..', '...']]

    p = []

    ss = 2
    for i in range(3):
        row = ''
        for j in range(2):
            row = dupa[j]
            #row = row + dupa[i + j * ss]

        p.append(row)

    print(p)
    print('DUPA')
    #return pattern
