#!/usr/bin/python3

import itertools
import time

# ==================================================
def simulate(moves):
	spells = [
		{ 'name' : "Missile", 'cost' : 53,  'damage' : 4, 'heal' : 0, 'armor' : 0, 'mana' : 0,   'duration' : 1, 'active' : 0},
		{ 'name' : "Drain",   'cost' : 73,  'damage' : 2, 'heal' : 2, 'armor' : 0, 'mana' : 0,   'duration' : 1, 'active' : 0},
		{ 'name' : "Shield",  'cost' : 113, 'damage' : 0, 'heal' : 0, 'armor' : 7, 'mana' : 0,   'duration' : 6, 'active' : 0},
		{ 'name' : "Poison",  'cost' : 173, 'damage' : 3, 'heal' : 0, 'armor' : 0, 'mana' : 0,   'duration' : 6, 'active' : 0},
		{ 'name' : "Recharge",'cost' : 229, 'damage' : 0, 'heal' : 0, 'armor' : 0, 'mana' : 101, 'duration' : 5, 'active' : 0}
	]
	hero = {
		'hitpoints'	: 50,
		'mana' 			: 500
	}

	boss = {
		'hitpoints'	: 71,
		'damage'		: 10,
	}

	mana_used = 0

	for move in moves:
		print('Boss: %s\nHero: %s' % (boss['hitpoints'], hero['hitpoints']))
		print('Using %s' % spells[move])
		print(spells)
		time.sleep(1)
		# Resolve mana recharging:
		hero['mana'] = hero['mana'] + sum([spell['mana'] for spell in spells if spell['active']])
		for i in range(5): # Lower 'active' counter on spells
			spells[i]['active'] = max(0,spells[i]['active']-1)
		if spells[move]['active']:
			return False # Trying to cast an already active spell
		# Make the current spell active for some number of turns
		spells[move]['active'] = spells[move]['duration']
		# Get a total mana cost:
		mana_used = mana_used + spells[move]['cost']
		# Can the player actually cast that?
		hero['mana'] = hero['mana'] - spells[move]['cost']
		if hero['mana'] < 0:
			return False
		# Do damage to the boss
		boss['hitpoints'] = boss['hitpoints'] - sum([spell['damage'] for spell in spells if spell['active']])
		# Do damage to the player
		hero['hitpoints'] = hero['hitpoints'] - max(1, boss['damage'] - sum([spell['armor'] for spell in spells if spell['active']]))
		if boss['hitpoints'] <= 0:
			return mana_used
		if hero['hitpoints'] <= 0:
			return False

# ==================================================

mana_spent = 1000000000000
best_moves = []

# Taking a wild guess that it takes no more than 20 moves to kill the boss.
for moves in itertools.combinations_with_replacement(range(5),20):
	ms = simulate(moves)
	print(ms)
	if ms and ms < mana_spent:
		mana_spent = ms
		best_moves = moves

print('Mana spent: %s' % mana_spent)
print('Moves: %s' % best_moves)
