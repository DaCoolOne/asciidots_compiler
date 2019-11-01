

from character import get_character

SPACE_CHARACTER = get_character(" ")

class warp:
	def __init__(self, ax, ay, bx, by):
		self.link_ax = ax
		self.link_ay = ay
		self.link_bx = bx
		self.link_by = by

class grid:
	def __init__(self, width, height):
		self.width = width
		self.height = height
	def id(self, x, y):
		return (x * self.height + y) * 4 # Times 4 allows us to fit directions in as well.

class map(grid):
	def __init__(self, filepath):
		self.width = 0
		self.height = 0
		self.cells = []
		self.warps = []
		
		back_tick = False
		with open(filepath) as f:
			for line in f:
				list = []
				for c in line:
					if not c in '\n\r':
						if c == "`":
							if back_tick:
								back_tick = False
								break
							else:
								list.append(get_character(c))
							back_tick = True
						else:
							if back_tick:
								list.append(get_character("`"))
							list.append(get_character(c))
							back_tick = False
					
				self.cells.append(list)
				self.width = max(self.width, len(list))
				self.height += 1
		
		for i in range(self.height):
			for j in range(self.width):
				if len(self.cells[i]) >= j:
					self.cells[i].append(get_character(" "))
		
	def get(self, x, y):
		if x < 0 or y < 0 or x >= self.width or y >= self.height:
			return SPACE_CHARACTER
		else:
			return self.cells[y][x]
	def link_warps(self):
		self.warps = []
	def simplify(self):
		return grid(self.width, self.height)







