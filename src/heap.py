class MinHeap(object):
    """
    Min Binary Heap implementation.
    'A parent is always smaller than its children.'

    O(1) get min
    O(log(n)) insertion
    O(log(n)) remove min
    O(n) construction
    """
    def __init__(self):
        """
        Create an empty min heap.
        """
        super(MinHeap, self).__init__()
        # 1 based array
        self.array = [None]

    def insert(self, value):
        """
        Insert value in the heap.
        """
        self.array.append(value)
        self._up_heap(len(self.array)-1)

    def _up_heap(self, i):
        """
        Swap with parent if child is smaller and recurse on parent position.
        """
        parent = i/2
        if i > 1 and self.array[parent] > self.array[i]:
            self.array[i], self.array[parent] = self.array[parent], self.array[i]
            self._up_heap(parent)

    def pop(self):
        """
        Remove the min element from the heap and return it.
        """
        res = self.array[1]

        end = self.array.pop()
        if len(self.array) > 1:
            self.array[1] = end
            self._down_heap(1)
        return res

    def peek(self):
        """
        Return the min element.
        """
        return self.array[1]

    def _down_heap(self, i):
        """
        Take the two child, swap with the smallest and recurse on that position.
        """
        left = 2 * i
        right = 2 * i + 1
        smallest = i
        if left < len(self.array) and self.array[left] < self.array[smallest]:
            smallest = left
        if right < len(self.array) and self.array[right] < self.array[smallest]:
            smallest = right
        if smallest != i:
            self.array[i], self.array[smallest] = self.array[smallest], self.array[i]
            self._down_heap(smallest)

    def heapify(self, other):
        """
        From a given array, build a min heap.
        DownHeap all the non-leaf nodes.
        """
        self.array[1:] = other[:]
        for i in xrange(len(self.array)/2, 0, -1):
            self._down_heap(i)


def main():
    from heap_test import test_all
    test_all()


if __name__ == "__main__":
    main()