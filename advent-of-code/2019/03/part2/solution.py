#!/usr/bin/env python3

def get_locations(directions):
    position = [0,0]
    locations = set()
    for d in directions:
        direction = d[0]
        distance = int(d[1:])
        for i in range(distance):
            if direction == 'L':
                position[0] -= 1
            if direction == 'R':
                position[0] += 1
            if direction == 'U':
                position[1] += 1
            if direction == 'D':
                position[1] -= 1
            locations.add('*'.join([str(x) for x in position]))
    return locations

def get_distance(directions, location):
    position = [0,0]
    steps = 0
    for d in directions:
        direction = d[0]
        distance = int(d[1:])
        for i in range(distance):
            steps += 1
            if direction == 'L':
                position[0] -= 1
            if direction == 'R':
                position[0] += 1
            if direction == 'U':
                position[1] += 1
            if direction == 'D':
                position[1] -= 1
            if position == location:
                return steps

with open('input.txt', 'r') as infile:
    directions1 = infile.readline().strip().split(',')
    directions2 = infile.readline().strip().split(',')
locations1 = get_locations(directions1)
locations2 = get_locations(directions2)
shared_locations = locations1.intersection(locations2)
shared_locations = [[int(f[0]),int(f[1])] for f in [foo.split('*') for foo in shared_locations]]
min_distance = -1
for shared_location in shared_locations:
    total_distance = get_distance(directions1, shared_location) + get_distance(directions2, shared_location)
    if min_distance == -1 or total_distance < min_distance:
        min_distance = total_distance
print(f'Min distance: {min_distance}')