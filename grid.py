
class Grid:
	"""Sudoku Grid"""
	MAX=9
	def __init__(self,gen):
		self.grid = []#gen.create
		for i in range(Grid.MAX):
			self.grid.append([])
		print self.grid
	def __getitem__(self,i):
		return self.grid[i]
	def __setitem__(self,i,val):
		self.grid[i]=val
	
	def __str__(self):
		str = ''
		for row in range(Grid.MAX):
			#print 'row'+row.__str__()
			for col in range(Grid.MAX):
				#print 'col'+col.__str__()
				#print(self.grid[row][col]).__str__()
				str += (self.grid[row][col]).__str__()
				if col > 0 and col < Grid.MAX-1 and (col+1)%3==0:
					str += "|"
			if row > 0 and row < Grid.MAX-1 and (row+1)%3==0:
				str += "\n-----------"
			str += '\n'
		return str
		
	
	
	