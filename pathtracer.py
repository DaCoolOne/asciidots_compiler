

from character import DIRECTION, GUIDE, SPECIAL, compact

def move_crawl(x, y, crawl_dir):
	if crawl_dir & DIRECTION.UP:
		y -= 1
	if crawl_dir & DIRECTION.DOWN:
		y += 1
	if crawl_dir & DIRECTION.LEFT:
		x -= 1
	if crawl_dir & DIRECTION.RIGHT:
		x += 1
	return (x, y)

# Traces a path until it reaches a special path.
class path:
	def __init__(self, map, start_x, start_y, dir):
		self.complete = False
		
		self.start_x = start_x
		self.start_y = start_y
		
		crawl_dir = dir
		
		self.start_id = map.id(self.start_x, self.start_y) + compact(dir)
		
		x, y = move_crawl(start_x, start_y, crawl_dir)
		
		trace = []
		crawl_step = 1
		
		while not map.get(x, y).special:
			
			# print(x, y)
			
			crawl_step += 1
			
			m_id = map.id(x, y) + compact(crawl_dir)
			
			# Crawler has gone in a loop
			if m_id in trace:
				return
			
			# Keep track of where crawler has been.
			trace.append(m_id)
			
			# Crawler hit an invalid path
			if not map.get(x, y).direction & crawl_dir:
				# print("INVALID PATH")
				return
			
			# Crawler hit a path changer
			g = map.get(x, y).guide
			if g:
				if g & GUIDE.REFLECTOR:
					crawl_dir = g & 15
				elif g < 16:
					v = DIRECTION.VERTICAL if crawl_dir < 8 else DIRECTION.HORIZONTAL
					if not g & v:
						crawl_dir = g & 15
				elif g == GUIDE.REFLECT_A:
					crawl_dir = ((crawl_dir & 3) << 2) | ((crawl_dir & 12) >> 2)
				elif g == GUIDE.REFLECT_B:
					crawl_dir = ((~crawl_dir & 3) << 2) | ((~crawl_dir & 12) >> 2)
			
			# Step the crawler
			x, y = move_crawl(x, y, crawl_dir)
		
		self.end_x = x
		self.end_y = y
		self.end_dir = crawl_dir
		self.length = crawl_step
		
		self.end_id = map.id(self.end_x, self.end_y) + compact(crawl_dir)
		
		self.complete = True
		

class path_tracer:
	def __init__(self, map):
		# List of all paths
		self.paths = {}
		self.init_paths = []
		for i in range(map.width):
			for j in range(map.height):
				c = map.get(i, j)
				if c.special == SPECIAL.START:
					id = self.create_path(map, i, j)
					if id:
						self.init_paths.append(id)
		
		for p in self.paths:
			path = self.paths[p]
			print(path.start_x, path.start_y, path.end_x, path.end_y)
		
	
	# Recursively creates
	def create_path(self, map, start_x, start_y, dir = DIRECTION.NONE):
		
		# If not dir, assume start spot and try to find the right dir.
		if not dir:
			if map.get(start_x, start_y - 1).direction & DIRECTION.UP:
				dir = DIRECTION.UP
			elif map.get(start_x + 1, start_y).direction & DIRECTION.RIGHT:
				dir = DIRECTION.RIGHT
			elif map.get(start_x, start_y + 1).direction & DIRECTION.DOWN:
				dir = DIRECTION.DOWN
			elif map.get(start_x - 1, start_y).direction & DIRECTION.LEFT:
				dir = DIRECTION.LEFT
			else:
				return
		elif not map.get(start_x, start_y).direction & dir:
			return
		
		id = map.id(start_x, start_y) | compact(dir)
		if id in self.paths.keys():
			return
		p = path(map, start_x, start_y, dir)
		print(id, p.complete)
		if p.complete:
			self.paths[id] = p
			if map.get(p.end_x, p.end_y).special != SPECIAL.END:
				self._branch_path(map, p.end_x, p.end_y)
			return id
		
	def _branch_path(self, map, start_x, start_y):
		# Look at spawnable directions and send a path out in each direction
		self.create_path(map, start_x, start_y, DIRECTION.UP)
		self.create_path(map, start_x, start_y, DIRECTION.DOWN)
		self.create_path(map, start_x, start_y, DIRECTION.LEFT)
		self.create_path(map, start_x, start_y, DIRECTION.RIGHT)

