import random
import unittest

from heap import MinHeap


class HeapTests(unittest.TestCase):

    def test_min_heap_sorting(self):

        # seed for consistant testing and reproductibility
        for seed in range(10):
            random.seed(seed)

            heap = MinHeap()
            nums = list(xrange(10))
            random.shuffle(nums)
            for n in nums:
                heap.insert(n)

            for n in xrange(10):
                self.assertEqual(n, heap.pop())

            heap.heapify(nums)

            for n in xrange(10):
                self.assertEqual(n, heap.pop())


def test_all():
    unittest.main(__name__, verbosity=2)


if __name__ == "__main__":
    test_all()
