
"""
0123456789
1.........
2.........
3
4
5
6
7
8
9
"""

class Grid:
	"""Sudoku Grid"""
	MAX=9
	def __init__(self,gen):
		self.grid = gen.create
	
	def __getitem__(self,i):
		return self.grid[i]
	def __setitem__(self,i,val):
		self.grid[i]=val
		
	
	
	