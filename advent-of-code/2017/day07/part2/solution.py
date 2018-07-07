#1/usr/bin/env python3
import pprint

graph = {}

with open('input.txt', 'r') as f:
    for line in f.readlines():
        words = line.split()
        name = words[0]
        weight = int(words[1].strip('(').strip(')'))
        children = words[3:]
        graph[name] = dict()
        graph[name]['weight'] = weight
        graph[name]['children'] = [c.strip(',') for c in children]

bottom = ''

for key in graph:
    is_bottom = True
    for node in graph:
        if key in graph[node]['children']:
            is_bottom = False
    if is_bottom:
        bottom = key

def get_weight(node):
    weight = graph[node]['weight']
    for child in graph[node]['children']:
        weight += get_weight(child)
    return weight

def find_error(node):
    children_weights = [get_weight(child) for child in graph[node]['children']]
    if len(set(children_weights)) == 1: # All are the same
        for child in graph[node]['children']:
            find_error(child)
    else:
        for child in graph[node]['children']:
            if get_weight(child) != max(set(children_weights), key=children_weights.count):
                return (child, graph[child]['weight'], get_weight(child), max(set(children_weights), key=children_weights.count))

current_error = bottom
while find_error(current_error):
    previous_error = current_error
    current_error = find_error(current_error)[0]

errorenous_line = find_error(previous_error)
print(errorenous_line[1] - errorenous_line[2] + errorenous_line[3])
