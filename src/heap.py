class MinHeap(object):
    """
    Min Binary Heap implementation.
    'A parent is always smaller than its children.'
    O(1) get min
    O(log(n)) insertion
    O(log(n)) remove min
    """
    def __init__(self):
        super(MinHeap, self).__init__()
        # 1 based array
        self.array = [0]

    def insert(self, value):
        self.array.append(value)
        self.up_heap(len(self.array)-1)

    def up_heap(self, i):
        parent = i/2
        if i >= 1 and self.array[parent] > self.array[i]:
            self.array[i], self.array[parent] = self.array[parent], self.array[i]
            self.up_heap(parent)

    def pop(self):
        res = self.array[1]

        end = self.array.pop()
        if len(self.array) > 1:
            self.array[1] = end
            self.down_heap(1)
        return res

    def peek(self):
        return self.array[1]

    def down_heap(self, i):
        left = 2 * i
        right = 2 * i + 1
        smallest = i
        if left < len(self.array) and self.array[left] < self.array[smallest]:
            smallest = left
        if right < len(self.array) and self.array[right] < self.array[smallest]:
            smallest = right
        if smallest != i:
            self.array[i], self.array[smallest] = self.array[smallest], self.array[i]
            self.down_heap(smallest)

    def heapify(self, other):
        self.array[1:] = other[:]
        for i in range(len(self.array)/2, 0, -1):
            self.down_heap(i)


def main():
    import random
    heap = MinHeap()
    nums = list(xrange(10))
    random.shuffle(nums)
    for n in nums:
        heap.insert(n)

    for n in xrange(10):
        assert n == heap.pop()

    heap.heapify(nums)

    for n in xrange(10):
        assert n == heap.pop()


if __name__ == "__main__":
    main()