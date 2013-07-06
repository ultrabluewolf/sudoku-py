#!/usr/bin/env python

import engine, checker, grid, grid_gen
from grid import *

print 'hello'
g=Grid(None)

# temp, read in input for checker tests
with open('input','r') as file:
	row=0
	col=0
	for line in file:
		line = line.strip()
		#print line
		if len(line) == 0:
			continue
		for num in line:
			#print num
			g[row].append(int(num))
			if col < Grid.MAX-1:
				col+=1
			else:
				if row < Grid.MAX-1:
					row+=1
					col=0
				else:
					print "LIM Reached!"
print str(g)
