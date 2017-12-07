#!/usr/bin/python3

import sys

entries = []
parents = set()
tree = []

def buildTree(name):
    global entries
    global parents

    if name not in parents:
        leaf = list(filter(lambda entry: entry['name'] == name, entries))[0]
        leaf['children'] = []
        return leaf
    else:
        #print(name)
        node = list(filter(lambda entry: entry['name'] == name, entries))[0]
        node['children'] = [buildTree(child) for child in list(filter(lambda entry: entry['name'] == name, entries))[0]['children']]
        return node

def calculateWeights(node):
    sum = 0
    if node['children']:
        for child in node['children']:
            sum += calculateWeights(child)
    sum += int(node['weight'])
    node['total'] = int(sum)
    return int(sum)

def findImbalance(node):
    #values = [item['total'] for item in node]
    values = []
    for counter, item in enumerate(node):
        values.append([counter, item['total']])
    allTheSame = lambda v: len(set([i[1] for i in v])) == 1
    #print(values)
    print(values)
    if not allTheSame(values):
        index, value = 0, 0
        for i in range(0, len(values)):
            if values[i][1] > value:
                value = values[i][1]
                index = i

        print(index, value)
        findImbalance(node[i]['children'])
    else:
        print('the same!')


if len(sys.argv) != 2:
    print('Provide input file as command line argument!')
else:
    for line in open(sys.argv[1]).readlines():
        entries.append({
            'name': line.split()[0],
            'weight': line.split()[1].strip('()'),
            'children': [item.strip() for item in line[line.find('->') + 3:].split(',')] if '->' in line else []
        })

    parents = {entry['name'] for entry in entries if entry['children']}
    children = {child for entry in entries for child in entry['children']}
    root = next(iter(parents - children)) # retrieve first (and only) element from set
    #print(root)

    tree = buildTree(root)

    extremes = [calculateWeights(child) for child in tree['children']]


    findImbalance(tree['children'])

    for child in tree['children']:
        if child['name'] == 'nhrla':
            for child2 in child['children']:
                if child2['name'] == 'idfyy':
                    for child3 in child2['children']:
                        if child3['name'] == 'aobgmc':
                            for child4 in child3['children']:
                                #print(child4['name'], child4['weight'], calculateWeights(child3))
                                print(child2['total'])
                                pass

    #print(max(extremes) - min(extremes))
    #print(extremes)
