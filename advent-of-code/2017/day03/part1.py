#!/usr/bin/env python3

distance = lambda location: abs(location[0]) + abs(location[1])

def solve(number):
    layer = 0
    while (2*layer+1)**2 < number:
        layer += 1
    location = [layer, -layer]

    delta = (2*layer+1)**2 - number
    side_length = layer * 2 + 1

    if delta <= side_length-1:
        location[0] -= delta
    elif delta <= 2*(side_length-1):
        location[0] = -location[0]
        location[1] += delta - side_length + 1
    elif delta <= 3*(side_length-1):
        location[1] = -location[1]
        location[0] = -location[0] + (delta - 2*(side_length-1))
    elif delta <= 4*(side_length-1):
        location[1] = -location[1] - (delta - 3*(side_length-1))

    print("%s is located at %s, which is %s away from center" % (number, location, distance(location)))

for i in range(1,50):
    solve(i)
solve(1024)
solve(368078)
