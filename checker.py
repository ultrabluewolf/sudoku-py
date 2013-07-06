"""Grid Validation methods"""
import grid
from grid import *
	
def is_valid(grid):
	if is_valid_rows(grid):
		if is_valid_cols(grid):
			if is_valid_blocks(grid):
				return True
	return False

def is_valid_rows(grid):
	result=False
	for i in (0..Grid.MAX):
		
	return result

def is_valid_cols(grid):
	return False

def is_valid_blocks(grid):
	return False

