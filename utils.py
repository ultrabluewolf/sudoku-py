"""Utils"""
import grid
from grid import *

def readGridInput(fname):
	# read in input for checker tests
	grids = []
	with open(fname,'r') as file:
		row=0
		col=0
		grids_idx=0
		grids.append(Grid(None))
		for line in file:
			line = line.strip()
			#print line
			if len(line) == 0:
				continue
			for num in line:
				#print num
				grids[grids_idx][row].append(int(num))
				if col < Grid.MAX-1:
					col+=1
				else:
					if row < Grid.MAX-1:
						row+=1
						col=0
					else:
						print "LIM Reached!"
						grids.append(Grid(None))
						grids_idx+=1
						row=0
						col=0
	return grids
