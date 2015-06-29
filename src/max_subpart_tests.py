from max_subpart import max_area_under_histogram, max_rectangle_in_sparse_matrix


def test_max_area_under_histogram():
	assert max_area_under_histogram([]) == 0
	assert max_area_under_histogram([4,3,1]) == 6
	assert max_area_under_histogram([1,2,1]) == 3
	assert max_area_under_histogram([1,3,3,1]) == 6
	assert max_area_under_histogram([1,3,4,3,1]) == 9
	assert max_area_under_histogram([1,3,1,3,1]) == 5
	assert max_area_under_histogram([2,0,1]) == 2
	assert max_area_under_histogram([1,0,2]) == 2
	assert max_area_under_histogram([1,2,2,0,1]) == 4
	assert max_area_under_histogram([3,2]) == 4
	assert max_area_under_histogram([-3,-2,1,-2]) == 1
	assert max_area_under_histogram([-3,-2]) == 0


def test_max_rectangle_in_sparse_matrix():
	assert max_rectangle_in_sparse_matrix([]) == 0
	assert max_rectangle_in_sparse_matrix([[1]]) == 1
	assert max_rectangle_in_sparse_matrix([
			[0,0],
			[0,0],
		]) == 0
	assert max_rectangle_in_sparse_matrix([
			[0,1],
			[0,0],
		]) == 1
	assert max_rectangle_in_sparse_matrix([
			[0,1],
			[0,1],
		]) == 2
	assert max_rectangle_in_sparse_matrix([
			[1,1],
			[0,0],
		]) == 2
	assert max_rectangle_in_sparse_matrix([
			[0,0],
			[1,1],
		]) == 2
	assert max_rectangle_in_sparse_matrix([
			[1,0],
			[1,0],
		]) == 2
	assert max_rectangle_in_sparse_matrix([
			[0,1,1,0],
			[0,1,1,1],
			[0,0,1,0],
			[1,0,0,1],
		]) == 4
	assert max_rectangle_in_sparse_matrix([
			[0,1,1,1],
			[0,1,0,1],
			[0,1,1,1],
			[1,0,0,1],
		]) == 4


def test_all():
	test_max_area_under_histogram()
	test_max_rectangle_in_sparse_matrix()


def main():
	test_all()


if __name__ == "__main__":
	main()
