"""Grid Validation methods"""
import grid
from grid import *
	
def is_valid(grid):
	if is_valid_rows(grid):
		if is_valid_cols(grid):
			if is_valid_blocks(grid):
				return True
	return False

def is_valid_row(grid,row):
	result=True
	found=set()
	for col in range(grid.MAX):
		if not grid[row][col] in found:
			found.add(grid[row][col])
		else:
			result = False
			break
	return result

def is_valid_col(grid,col):
	result=True
	found=set()
	for row in range(grid.MAX):
		if not grid[row][col] in found:
			found.add(grid[row][col])
		else:
			result = False
			break
	return result
"""
012|345|678
1..|...|...
2..|...|...
-----------
3..|...|...
4..|...|...
5..|...|...
-----------
6..|...|...
7..|...|...
8..|...|...
"""
def is_valid_block(grid,block):
	result=True
	found=set()
	
	return result
	
def is_valid_rows(grid):
	result=True
	for row in range(grid.MAX):
		result = is_valid_row(grid,row)
		if not result:
			break
	return result

def is_valid_cols(grid):
	result=True
	for col in range(grid.MAX):
		result = is_valid_col(grid,col)
		if not result:
			break
	return result

#TODO: is a block check required??
def is_valid_blocks(grid):
	return True

