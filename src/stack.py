class Stack(object):
	"""
	Implement a stack from an array with more explicit methods.
	"""
	def __init__(self, array=None):
		assert array is None or isinstance(array, list)
		self.array = array if array is not None else []

	def pop(self):
		return self.array.pop()

	def push(self, elem):
		self.array.append(elem)

	def peek(self):
		return self.array[-1] if self.array else None

	@property
	def size(self):
		return len(self.array)

	def __repr__(self):
		return "Stack(array=%r)" % self.array

	def __str__(self):
		return "stack%s" % self.array

	def __nonzero__(self):
		return bool(self.array)