#!/usr/bin/python3

import itertools
import math
import time

warrior = {
	'hitpoints': 	100,
	'damage':	0,
	'armor':	0
}

boss = {
	'hitpoints': 	109,
	'damage':	8,
	'armor':	2
}

# (cost, damage)
weapons = (
	(8, 4),
	(10, 5),
	(25, 6),
	(40, 7),
	(74, 8)
)

# (cost, armor)
armors = (
	(0, 0), # You can choose zero armor pieces
	(13, 1),
	(31, 2),
	(53, 3),
	(75, 4),
	(102, 5)
)

# (cost, damage, armor)
rings = (
	(0, 0, 0), # You can choose 0, 1, or 2 rings
	(0, 0, 0),
	(25, 1, 0),
	(50, 2, 0),
	(100, 3, 0),
	(20, 0, 1),
	(40, 0, 2),
	(80, 0, 3)
)

best_cost = 10000000000000

def warrior_wins():
	warrior_strikes_needed = math.ceil(boss['hitpoints'] / max(warrior['damage'] - boss['armor'], 1))
	boss_strikes_needed = math.ceil(warrior['hitpoints'] / max(boss['damage'] - warrior['armor'], 1))
	return warrior_strikes_needed <= boss_strikes_needed

for weapon in weapons:
	for armor in armors:
		for ring1, ring2 in itertools.combinations(rings, 2):
			warrior['damage'] = weapon[1] + ring1[1] + ring2[1]
			warrior['armor'] = armor[1] + ring1[2] + ring2[2]
			cost = weapon[0] + armor[0] + ring1[0] + ring2[0]
			if warrior_wins() and cost < best_cost:
				print('Best so far', warrior, '$%s' % cost)
				best_cost = cost
print(best_cost)
