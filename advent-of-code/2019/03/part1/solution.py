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

with open('input.txt', 'r') as infile:
    directions1 = infile.readline().strip().split(',')
    directions2 = infile.readline().strip().split(',')
locations1 = get_locations(directions1)
locations2 = get_locations(directions2)
shared_locations = locations1.intersection(locations2)
shared_locations = [foo.split('*') for foo in shared_locations]
distances = [abs(int(loc[0]))+abs(int(loc[1])) for loc in shared_locations]
print(f'Min distance: {min(distances)}')