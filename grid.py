
class Grid:
	"""Sudoku Grid"""
	MAX=9
	EMPTY=0
	def __init__(self,gen):
		if gen is None:
			self.grid = []
			for i in range(Grid.MAX):
				self.grid.append([])
		else:
			self.grid = gen.create()
		
	def pad(self):
		for row in range(Grid.MAX):
			if len(self.grid[row]) != 0:
				return
			else:
				for col in range(Grid.MAX):
					self.grid[row].append(0)
	
	def __getitem__(self,i):
		return self.grid[i]
	def __setitem__(self,i,val):
		self.grid[i]=val
	
	def __str__(self):
		str = ''
		for row in range(Grid.MAX):
			for col in range(Grid.MAX):
				str += (self.grid[row][col]).__str__()
				if col > 0 and col < Grid.MAX-1 and (col+1)%3==0:
					str += "|"
			if row > 0 and row < Grid.MAX-1 and (row+1)%3==0:
				str += "\n-----------"
			str += '\n'
		return str
		
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
	