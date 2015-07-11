import random
import unittest


def _partition(arr, start, end):
    """
    Partitions a slice of arr around a pivot placing all element
    smaller than the pivot before it and all greater after it.

    @param: arr list
    @param: start int
    @param: end int
    @param: n int
    @return: the position of the pivot at the end of the partitioning
    """
    # pick a pivot at random to limit likelyhood of worst case scenario
    pivot_index = random.randrange(start, end + 1)

    # move the pivot to the end for later processing
    pivot = arr[pivot_index]
    arr[end], arr[pivot_index] = arr[pivot_index], arr[end]

    # move all elements smaller than the pivot before pivot index
    pivot_index = start
    for i in xrange(start, end):
        if arr[i] < pivot:
            arr[i], arr[pivot_index] = arr[pivot_index], arr[i]
            pivot_index += 1

    # move the pivot to the correct location
    arr[end], arr[pivot_index] = arr[pivot_index], arr[end]

    return pivot_index


def _quick_select(arr, start, end, n):
    """
    Select the nth smallest element assuming it is between start and end.

    Similar to a binary search but the array needs to be reorganize to
    have the nth element in its ordered position using part of the pivot
    sort algorithm.

    @param: arr list
    @param: start int
    @param: end int
    @param: n int
    @return: nth smallest element of arr
    """
    while start != end:
        # partition around a random pivot
        # the pivot will be placed in its sorted position
        pivot_index = _partition(arr, start, end)

        if n == pivot_index:
            return arr[pivot_index]
        elif n < pivot_index:
            end = pivot_index - 1
        else:
            start = pivot_index + 1

    return arr[start]


def quick_select(arr, n):
    """
    Select the nth smallest element of a list by modifying the list in place.
    Uses a zero based index.

    Example: quick_select([8,6,7,9], 1) -> 7

    @param: arr list
    @param: n int
    @return: nth smallest element of arr
    """
    assert n >= 0
    assert n < len(arr)
    assert isinstance(arr, list)

    return _quick_select(arr, 0, len(arr) - 1, n)


class QuickSelectTests(unittest.TestCase):

    def setUp(self):
        # seed random module to get reproductible tests
        random.seed(0)

    def test_predifined_values(self):
        self.assertEqual(quick_select([8,6,7,9], 0), 6)
        self.assertEqual(quick_select([8,6,7,9], 1), 7)
        self.assertEqual(quick_select([8,6,7,9], 2), 8)
        self.assertEqual(quick_select([8,6,7,9], 3), 9)

        with self.assertRaises(Exception):
            self.assertEqual(quick_select([], 0))

        self.assertEqual(quick_select([1], 0), 1)
        self.assertEqual(quick_select([1,1,1,1,1], 4), 1)
        self.assertEqual(quick_select([-1,-1,-1,-1,-1], 4), -1)
        self.assertEqual(quick_select([1,-1,2,-2,3,-3,0], 3), 0)

    def test_range(self):
        for i in xrange(100):
            random_a = range(100) * 10
            random.shuffle(random_a)
            median = quick_select(random_a, i*10)
            self.assertEqual(median, i)


def main():
    unittest.main()


if __name__ == '__main__':
    main()