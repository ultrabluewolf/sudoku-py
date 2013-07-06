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
	
	def create(self):
		g=Grid(None)
		return g
	