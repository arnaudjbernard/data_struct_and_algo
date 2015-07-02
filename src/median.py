import random


def _partition(a, start, end, pivot_index):

    pivot = a[pivot_index]
    a[end], a[pivot_index] = a[pivot_index], a[end]

    pivot_index = start
    for i in xrange(start, end):
        if a[i] < pivot:
            a[i], a[pivot_index] = a[pivot_index], a[i]
            pivot_index += 1

    a[end], a[pivot_index] = a[pivot_index], a[end]

    return pivot_index


def _quick_select(a, start, end, n):
    while start != end:
        pivot_index = random.randrange(start, end + 1)
        pivot_index = _partition(a, start, end, pivot_index)
        if n == pivot_index:
            return a[pivot_index]
        elif n < pivot_index:
            end = pivot_index - 1
        else:
            start = pivot_index + 1
    return a[start]


def quick_select(a, n):
    """
    param a list
    param n int
    return n smallest element of a
    """
    assert n >= 0
    assert n < len(a)
    assert isinstance(a, list)
    return _quick_select(a, 0, len(a) - 1, n)


def main():
    for i in range(100):
        random_a = range(100) * 10
        random.shuffle(random_a)
        median = quick_select(random_a, i*10)
        print median
        assert median == i


if __name__ == '__main__':
    main()