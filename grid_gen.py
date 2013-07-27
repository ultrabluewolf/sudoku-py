import grid,checker,random
from random import *
from grid import *

class GridGen:
	"""Sudoku Grid Generator
		creates sudoku board based on difficulty level on scale of 1 to 5
		5 being the hardest"""
	EASY=1
	HARD=5
	def __init__(self,diff_lvl):
		self.lvl=diff_lvl
		self.rand = Random()
	
	def create(self):
		g=Grid(None)
		self.gen_randomized_soln(g)
		self.poke_holes(g)
		return g
	
	"""takes randomized solution and clears numbers depending on difficulty selected"""
	def poke_holes(self,grid):
		pass
	
	def gen_randomized_soln(self,grid):
		self.rand.seed()
		grid.pad()
		#is_not_valid=True
		#while is_not_valid:
		for row in range(Grid.MAX):
			#usedNums=set()
			#for col in range(Grid.MAX):
			col=0
			while col < Grid.MAX:
				is_not_valid = True
				while is_not_valid:
					num = self.rand.randint(1,Grid.MAX)
					grid[row][col] = num
					print str(row) + "," + str(col) + "; " + str(num)
					print str(grid)
					#is_not_valid = not checker.is_valid_not_full(grid)
					is_not_valid = (not checker.is_valid_row(grid,row,False)) or (not checker.is_valid_col(grid,col,False))
				col+=1
				#if not num in usedNums:
					#print str(row) + "," + str(col)
					#usedNums.add(num)
					#grid[row][col]=num
					#col+=1
			#is_not_valid = not checker.is_valid(grid)
	