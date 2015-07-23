import random
import unittest

from heap import MinHeap


class HeapTests(unittest.TestCase):

    def test_min_heap_sorting(self):

        # seed for consistant testing and reproductibility
        for seed in xrange(10):
            random.seed(seed)

            heap = MinHeap()
            shuffled_nums = [int(random.random() * 20 - 10) for _ in xrange(1000)]
            nums = sorted(shuffled_nums)
            for n in shuffled_nums:
                heap.insert(n)

            for n in nums:
                self.assertEqual(n, heap.pop())

            heap.heapify(shuffled_nums)

            for n in nums:
                self.assertEqual(n, heap.pop())


def test_all():
    unittest.main(__name__, verbosity=2)


if __name__ == "__main__":
    test_all()
