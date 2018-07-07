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

print(bottom)
