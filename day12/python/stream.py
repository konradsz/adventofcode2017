#!/usr/bin/python3

import sys

if len(sys.argv) != 2:
    print('Provide input file as command line argument!')
else:
    file = open(sys.argv[1]).read().splitlines()
    pipes = {}
    for i in range(0, len(file)):
        pipes[i] = [int(item.strip(',')) for item in file[i].split()[2:]]

    allPrograms = set(range(0, len(file)))

    def findConnections(index):
        findConnections.group.add(index)
        for connection in pipes[index]:
            if connection not in findConnections.group:
                findConnections(connection)

        return findConnections.group

    connectedPrograms = []
    no = 0
    while len(connectedPrograms) != len(allPrograms):
        no += 1
        diff = allPrograms - set(connectedPrograms)
        program = diff.pop()
        findConnections.group = set()
        group = findConnections(program)
        print('(', no, ') program', program, 'size of group:', len(group))
        connectedPrograms += group

