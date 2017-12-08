#!/usr/bin/python3

import sys

entries = []
parents = set()

def buildTree(name):
    if name not in parents:
        leaf = list(filter(lambda entry: entry['name'] == name, entries))[0]
        leaf['children'] = []
        return leaf
    else:
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
    values = []
    for counter, item in enumerate(node):
        values.append([counter, item['total'], item['weight']])
    areBalanced = lambda v: len(set([i[1] for i in v])) == 1

    if not areBalanced(values):
        index, total, value = 0, 0, 0
        for i in range(0, len(values)):
            if values[i][1] > total:
                total = values[i][1]
                value = values[i][2]
                index = i

        print('Imbalanced! node index:', index, ', its value:', value)
        findImbalance(node[index]['children'])
    else:
        print('Balanced!')


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
    print('Root:', root)

    tree = buildTree(root)
    extremes = {calculateWeights(child) for child in tree['children']}
    findImbalance(tree['children'])

    print('Last node imbalanced by:', max(extremes) - min(extremes))

