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
	return result

def is_valid_rows(grid):
	result=True
	for row in range(grid.MAX):
		found = set()
		for col in range(grid.MAX):
			if not grid[row][col] in found:
				found.add(grid[row][col])
			else:
				result = False
				return result
	return result

def is_valid_cols(grid):
	result=True
	for col in range(grid.MAX):
		found = set()
		for row in range(grid.MAX):
			if not grid[row][col] in found:
				found.add(grid[row][col])
			else:
				result = False
				return result
	return result

#TODO: is a block check required??
def is_valid_blocks(grid):
	return True

