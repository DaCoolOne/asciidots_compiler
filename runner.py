

from pathtracer import path_tracer
from mapper import map

class QueuePoint:
	def __init__(self, t, id):
		self.time = t
		self.id = id
		self.next = None

class ControlQueue:
	def __init__(self):
		self.start = None
	def insert(self, qp):
		p = self.start
		while not p.next is None or p.next.time > qp.time:
			p = p.next
		
		n = p.next
		p.next = qp
		qp.next = n
	def pop(self):
		n = self.start
		if n is None:
			return None
		
		self.start = n.next
		
		return n
		

# Assumes that the file exists. Creates the file and runs it.
class Compiler:
	def __init__(self, file_name):
		
		m = map("script.dots")
		self.path_tracer = path_tracer(m)
		
	# Initializes the enviroment
	def initialize(self):
		
		self.control_queue = ControlQueue()
		
		for id in path_trace.init_paths:
			self.control_queue.append()
		
	def step(self):
		pass
	def run(self, x, y):
		while not self.step():
			pass













