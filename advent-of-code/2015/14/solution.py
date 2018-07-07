#!/usr/bin/python
import re, math

deer = []
total_seconds = 2503

class raindeer(object):
	def __init__(self, name, speed, fly_seconds, rest_seconds):
		self.name = name
		self.speed = int(speed)
		self.fly_seconds = int(fly_seconds)
		self.rest_seconds = int(rest_seconds)
		self.points = 0
		self.total_distance = 0
		self.flying = True
		self.cycle_time = 0
	def move(self):
		self.cycle_time = self.cycle_time + 1
		if self.flying:
			self.total_distance = self.total_distance + self.speed
		if self.cycle_time == self.fly_seconds and self.flying:
			self.flying = False
			self.cycle_time = 0
		if self.cycle_time == self.rest_seconds and not self.flying:
			self.flying = True
			self.cycle_time = 0

with open('input.txt','r') as f:
	for line in f:
		name, speed, fly_seconds, rest_seconds = re.match(r'([A-Za-z]+) can fly ([0-9]+) km/s for ([0-9]+) seconds, but then must rest for ([0-9]+) seconds.',line).groups()
		deer.append(raindeer(name, speed, fly_seconds, rest_seconds))

for i in range(total_seconds):
	furthest = 0
	for d in deer:
		d.move()
		if d.total_distance > furthest:
			furthest = d.total_distance
	for d in deer:
		if d.total_distance == furthest:
			d.points = d.points + 1

most_points = 0
furthest = 0
for d in deer:
	if d.points > most_points:
		most_points = d.points
		most_points_name = d.name
	if d.total_distance > furthest:
		furthest = d.total_distance
		furthest_name = d.name

print '   Furthest: %s (%s)' % (furthest_name, furthest)
print 'Most Points: %s (%s)' % (most_points_name, most_points)
