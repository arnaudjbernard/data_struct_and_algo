import random
import unittest
from sort import *


class TestSortFunctions(unittest.TestCase):

    ARRAY_SIZE = 100

    def setUp(self):
        self.sorted = range(self.ARRAY_SIZE)
        self.to_sort = self.sorted[:]
        random.shuffle(self.to_sort)

    def test_insert_sort(self):
        insert_sort(self.to_sort)
        self.assertEqual(self.to_sort, self.sorted)

    def test_bubble_sort(self):
        bubble_sort(self.to_sort)
        self.assertEqual(self.to_sort, self.sorted)

    def test_quick_sort(self):
        quick_sort(self.to_sort)
        self.assertEqual(self.to_sort, self.sorted)

    def test_merge_sort(self):
        merge_sort(self.to_sort)
        self.assertEqual(self.to_sort, self.sorted)

    def test_heap_sort(self):
        heap_sort(self.to_sort)
        self.assertEqual(self.to_sort, self.sorted)

    def test_radix_sort(self):
        radix_sort(self.to_sort)
        self.assertEqual(self.to_sort, self.sorted)


if __name__ == '__main__':
    unittest.main()
