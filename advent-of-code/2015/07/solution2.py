#!/usr/bin/python

import re

desired_node = '_a'

class Node:
	def __init__(self, name):
		self.name = name
		self.edges = []
		self.dependents = []
		self.instruction = ''
	def addEdge(self, node):
		self.edges.append(node)
	def addDependents(self, dependents):
		self.dependents = dependents
	def addInstruction(self, instruction):
		self.instruction = instruction
		self.instruction = self.instruction.replace('LSHIFT', '<<')
		self.instruction = self.instruction.replace('RSHIFT', '>>')
		self.instruction = self.instruction.replace('OR', '|')
		self.instruction = self.instruction.replace('AND', '&')
		self.instruction = self.instruction.replace('NOT', '65535 - ')

def dep_resolve(node, resolved, unresolved):
	unresolved.append(node)
	for edge in node.edges:
		if edge not in resolved:
			if edge in unresolved:
				raise Exception('Circular reference detected: %s -> %s' % (node.name, edge.name))
			dep_resolve(edge, resolved, unresolved)
	resolved.append(node)
	unresolved.remove(node)

def print_var(v):
	var_to_print = '%(' + v + ')s'
	print var_to_print % globals()

with open('input.txt', 'r') as f:
	nodes = dict()
	for line in f:
		line = re.sub('([a-z]+)',r'_\1',line)
		linein, lineout = line.strip().split(' -> ')
		nodes[lineout] = Node(lineout)
		nodes[lineout].addDependents(re.findall('_[a-z]+',linein))
		nodes[lineout].addInstruction(linein)
	for node in nodes:
		for dependent in nodes[node].dependents:
			nodes[node].addEdge(nodes[dependent])
	resolved = []
	dep_resolve(nodes[desired_node],resolved,[])
	for node in resolved:
		code = '%s = %s\n' % (node.name, node.instruction)
		exec code
	nodes['_b'].addInstruction(str(_a)) 
	for node in resolved:
		code = '%s = %s\n' % (node.name, node.instruction)
		exec code
	print_var(desired_node)
