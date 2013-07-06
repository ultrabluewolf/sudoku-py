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

def is_valid_block(grid,block):
	BOUND=3
	result=True
	found=set()
	#find upper left corner of block
	row_ul=0
	if block >= 6:
		row_ul=6
	elif block >= 3:
		row_ul=3
	col_ul=(block-row_ul)*3
	#print str(block) + ':' + str(row) +','+ str(col)
	for row in range(row_ul,row_ul+BOUND):
		for col in range(col_ul,col_ul+BOUND):
			#print '('+str(row)+','+str(col)+')'
			if not grid[row][col] in found:
				found.add(grid[row][col])
			else:
				result=False
				return result
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

