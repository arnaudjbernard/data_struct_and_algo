def max_area_under_histogram(histogram):
	"""
	Find the area of the biggest rectangle that can fit under and histogram

	The idea is to find for each bar, given its height, how far it can expand.
	A stack keeps track of lower bounds to the left and we iterate on the right.

	The stack is always growing. When a bar is too small to be put in the stack,
	we found the right limit for all the bars in the stack that are bigger than
	the current one. The left limit is always the previous bar in the stack.

	@param histogram: list heights
	@return: max area under the histogram
	"""
	if not histogram:
		return 0

	# helper class to contain stack elements
	class StackElement(object):
		def __init__(self, index, height):
			self.index = index
			self.height = height
		def __repr__(self):
			return "index: %s, height: %s" % (self.index, self.height)

	# holds the best result found so far
	max_area = 0

	# always growing stack
	stack = []

	for index, height in enumerate(histogram, start=0):
		# unstack everything above the current bar
		while stack and stack[-1].height >= height:
			popped = stack.pop()
			prev_index = stack[-1].index + 1 if stack else 0
			popped_area = popped.height * (index - prev_index)
			max_area = max(max_area, popped_area)

		# stack the current bar
		stack.append(StackElement(index, height))

	# handle the remaining stack element that can expand all the way to the right
	index += 1
	while stack:
		popped = stack.pop()
		prev_index = stack[-1].index + 1 if stack else 0
		popped_area = popped.height * (index - prev_index)
		max_area = max(max_area, popped_area)

	return max_area


def max_rectangle_in_sparse_matrix(matrix):
	"""
	In a matrix with True and False values, find the biggest rectangle of True values.

	Go through the matrix line by line keeping track of how far high each column can go
	without hitting a zero.
	For each line compute the maximum area that extends from this line up using the
	max_area_under_histogram algorithm.

	@return the area of the rectangle
	"""
	# keeps track of the previous line heights
	prev_line_histogram = None

	# holds the best result found so far
	max_area = 0

	for i, row in enumerate(matrix):
		line_histogram = []
		for j, value in enumerate(row):

			if bool(value):
				prev_line_height = prev_line_histogram[j] if prev_line_histogram else 0
				histogram_height = prev_line_height + 1
			else:
				histogram_height = 0

			line_histogram.append(histogram_height)

		max_area = max(max_area, max_area_under_histogram(line_histogram))
		prev_line_histogram = line_histogram

	return max_area


def max_subarray(array):
	pass


def max_submatrix(matrix):
	pass


def main():
	from max_subpart_tests import test_all
	test_all()


if __name__ == "__main__":
	main()
