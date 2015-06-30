import unittest

from max_subpart import max_area_under_histogram, max_rectangle_in_sparse_matrix, \
	max_subarray, max_submatrix


class TestSubpartMethods(unittest.TestCase):

	def test_max_area_under_histogram(self):
		self.assertEqual(max_area_under_histogram([]), 0)
		self.assertEqual(max_area_under_histogram([4,3,1]), 6)
		self.assertEqual(max_area_under_histogram([1,2,1]), 3)
		self.assertEqual(max_area_under_histogram([1,3,3,1]), 6)
		self.assertEqual(max_area_under_histogram([1,3,4,3,1]), 9)
		self.assertEqual(max_area_under_histogram([1,3,1,3,1]), 5)
		self.assertEqual(max_area_under_histogram([2,0,1]), 2)
		self.assertEqual(max_area_under_histogram([1,0,2]), 2)
		self.assertEqual(max_area_under_histogram([1,2,2,0,1]), 4)
		self.assertEqual(max_area_under_histogram([3,2]), 4)
		self.assertEqual(max_area_under_histogram([-3,-2,1,-2]), 1)
		self.assertEqual(max_area_under_histogram([-3,-2]), 0)


	def test_max_rectangle_in_sparse_matrix(self):
		self.assertEqual(max_rectangle_in_sparse_matrix([]), 0)
		self.assertEqual(max_rectangle_in_sparse_matrix([[1]]), 1)
		self.assertEqual(max_rectangle_in_sparse_matrix([
				[0,0],
				[0,0],
			]), 0)
		self.assertEqual(max_rectangle_in_sparse_matrix([
				[0,1],
				[0,0],
			]), 1)
		self.assertEqual(max_rectangle_in_sparse_matrix([
				[0,1],
				[0,1],
			]), 2)
		self.assertEqual(max_rectangle_in_sparse_matrix([
				[1,1],
				[0,0],
			]), 2)
		self.assertEqual(max_rectangle_in_sparse_matrix([
				[0,0],
				[1,1],
			]), 2)
		self.assertEqual(max_rectangle_in_sparse_matrix([
				[1,0],
				[1,0],
			]), 2)
		self.assertEqual(max_rectangle_in_sparse_matrix([
				[0,1,1,0],
				[0,1,1,1],
				[0,0,1,0],
				[1,0,0,1],
			]), 4)
		self.assertEqual(max_rectangle_in_sparse_matrix([
				[0,1,1,1],
				[0,1,0,1],
				[0,1,1,1],
				[1,0,0,1],
			]), 4)


	def test_max_subarray(self):
		self.assertEqual(max_subarray([]), 0)
		self.assertEqual(max_subarray([0]), 0)
		self.assertEqual(max_subarray([-1]), 0)
		self.assertEqual(max_subarray([1]), 1)
		self.assertEqual(max_subarray([1,2,3]), 6)
		self.assertEqual(max_subarray([0,-2,1]), 1)
		self.assertEqual(max_subarray([1,-2,0]), 1)
		self.assertEqual(max_subarray([1,-2,3,1,-5,-2,3,2,-7,-3,4,0]), 5)

	def test_max_submatrix(self):
		self.assertEqual(max_submatrix([[]]), 0)
		self.assertEqual(max_submatrix([[-1]]), 0)
		self.assertEqual(max_submatrix([[0]]), 0)
		self.assertEqual(max_submatrix([
				[1,-1],
				[1,-1],
			]), 2)
		self.assertEqual(max_submatrix([
				[1,-1],
				[-1,-1],
			]), 1)
		self.assertEqual(max_submatrix([
				[ 1,-2, 3, 5],
				[ 2, 3, 4,-1],
				[-1,-3, 4, 2],
				[-3, 3,-2,10],
			]), 26)
		self.assertEqual(max_submatrix([
				[-1,-2, 3,-4],
				[ 2,-3,-4, 1],
				[-2, 5,-2, 4],
				[ 1, 1, 1, 1],
				[-1, 3, 2,-1],
			]), 14)


def test_all():
	unittest.main(__name__, verbosity=2)

if __name__ == "__main__":
	test_all()
