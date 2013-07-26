import grid,checker
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
		return g
	
	"""takes randomized solution and clears numbers depending on difficulty selected"""
	def poke_holes(self):
		pass
	
	def gen_randomized_soln(self):
		self.rand.seed()
		for row in grid.MAX:
			usedNums=set()
			for col in grid.MAX:
				num = self.rand.randint(1,grid.MAX)
				if not num in usedNums:
					usedNums.add(num)
					
				
	