import unittest


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
		return "stack-%s" % self.array


def solve_towers_of_anoi(stack1, stack2, stack3, depth=None):
	"""
	Moves elems from stack1 to stack3 keeping them always ordered from bottom to top.
	This function modifies the stacks in place.

	complexity: O(2**n) where n is the size of stack1

	@param stack1: Stack the source
	@param stack2: Stack the buffer
	@param stack3: Stack the destination
	"""
	if depth is None:
		depth = stack1.size - 1

	# move all but the biggest to the middle
	if depth > 0:
		solve_towers_of_anoi(stack1, stack3, stack2, depth - 1)

	# move the last one to the final stack
	elem = stack1.pop()
	stack3.push(elem)

	# put back the rest of the elements on the last stack
	if depth > 0:
		solve_towers_of_anoi(stack2, stack1, stack3, depth - 1)


class TestTowersOfAnoi(unittest.TestCase):

	def test_solver(self):
		size = 10
		stack1 = Stack()
		stack2 = Stack()
		stack3 = Stack()
		for i in reversed(xrange(size)):
			stack1.push(i)

		solve_towers_of_anoi(stack1, stack2, stack3)

		for i in xrange(size):
			self.assertEqual(i, stack3.pop())


def main():
	unittest.main()


if __name__ == "__main__":
	main()