import random
import time
import unittest

from stack import Stack

def sort_stack(stack, buffer_stack):
	"""
	Sort a stack using another stack as buffer.
	Brute force implementation similar to insert sort.
	"""
	for i in range(stack.size):
		mini = stack.pop()
		for _ in range(i, stack.size):
			elem = stack.pop()
			if elem < mini:
				buffer_stack.push(mini)
				mini = elem
			else:
				buffer_stack.push(elem)
		stack.push(mini)
		while buffer_stack:
			stack.push(buffer_stack.pop())


def insert_sort_stack(stack, buffer_stack):
	"""
	Sort a stack using another stack as buffer.
	Optimized implementation to only unstack the biggest part of the sorted
	buffer to insert a new element.
	"""
	while stack:
		elem = stack.pop()
		c = 0
		while buffer_stack and elem > buffer_stack.peek():
			stack.push(buffer_stack.pop())
			c += 1
		buffer_stack.push(elem)
		for i in range(c):
			buffer_stack.push(stack.pop())

	while buffer_stack:
		stack.push(buffer_stack.pop())


class SortStackTests(unittest.TestCase):

	size = 100

	def setUp(self):
		self.ref = sorted(range(self.size) * 10)
		self.to_sort = self.ref[:]
		random.shuffle(self.to_sort)

		self.start_time = time.time()

	def tearDown(self):
		t = time.time() - self.start_time
		print "%s: %.4f" % (self.id(), t)

	def test_sort_stack(self):
		s = Stack(self.to_sort)
		sort_stack(s, Stack())
		for i in reversed(self.ref):
			self.assertEqual(s.pop(), i)

	def test_insert_sort_stack(self):
		s = Stack(self.to_sort)
		insert_sort_stack(s, Stack())
		for i in reversed(self.ref):
			self.assertEqual(s.pop(), i)


if __name__ == "__main__":
	unittest.main(verbosity=0)
