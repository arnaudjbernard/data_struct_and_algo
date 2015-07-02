
def insert_sort(arr):
    """
    iterate on the array putting each element in its correct position
    """
    l = len(arr)
    for i in xrange(1, l):
        j = i
        #move i element up to the correct position
        while j > 0 and arr[j-1] > arr[j]:
            arr[j-1], arr[j] = arr[j], arr[j-1]
            j -= 1


def bubble_sort(arr):
    """
    swap unordered neighbor items until the array is sorted
    """
    l = len(arr)
    is_sorted = False

    while not is_sorted:
        is_sorted = True
        for i in xrange(1, l):
            if arr[i-1] > arr[i]:
                arr[i-1], arr[i] = arr[i], arr[i-1]
                is_sorted = False


def _quick_sort_rec(arr, start, end):
    if start > end:
        return

    # pick the pivot to be the last element
    pivot = arr[end]
    pivot_index = start
    # swap every element to its correct side of the pivot
    for i in xrange(start, end):
        if arr[i] <= pivot:
            arr[pivot_index], arr[i] = arr[i], arr[pivot_index]
            pivot_index += 1

    # put the pivot at its place
    arr[pivot_index], arr[end] = arr[end], arr[pivot_index]

    # sort sub-array before the pivot
    _quick_sort_rec(arr, start, pivot_index - 1)

    # sort sub-array after the pivot
    _quick_sort_rec(arr, pivot_index + 1, end)


def quick_sort(arr):
    """
    pick a random pivot
    put every smaller element before the pivot and every bigger after the pivot
    sort the two sub-arrays before and after the pivot
    """
    _quick_sort_rec(arr, 0, len(arr) - 1)


def _merge_sort_rec(arr, start, end, buff):
    if end - start <= 1:
        return

    middle = (start + end) / 2

    #sort left
    _merge_sort_rec(arr, start, middle, buff)

    #sort right
    _merge_sort_rec(arr, middle, end, buff)

    #merge left and right
    left_index = start
    right_index = middle
    for merge_index in xrange(start, end):
        if left_index < middle and ((right_index >= end) or arr[left_index] <= arr[right_index]):
            buff[merge_index] = arr[left_index]
            left_index += 1
        else:
            buff[merge_index] = arr[right_index]
            right_index += 1

    arr[start:end] = buff[start:end]


def merge_sort(arr):
    """
    sort each half of the array and merge the result to have an array completely sorted
    """
    _merge_sort_rec(arr, 0, len(arr), [0] * len(arr))


def heap_sort(arr):
    import heapq
    heap = arr[:]
    heapq.heapify(heap)
    for i in xrange(len(arr)):
        arr[i] = heapq.heappop(heap)


def count_sort(arr, arr_len, exp, base):
    """
    A function to do counting sort of arr[] according to the digit represented by exp.
    """
    output = [0] * arr_len
    count = [0] * base

    # Store count of occurrences in count[]
    for i in xrange(arr_len):
        digit = (arr[i]/exp) % base
        count[digit] += 1

    # Change count[i] so that count[i] now contains actual position of this digit in output[]
    for digit in xrange(1, base):
        count[digit] += count[digit-1]

    # Build the output array
    for i in xrange(arr_len - 1, -1, -1):
        digit = (arr[i]/exp) % base
        output[count[digit] - 1] = arr[i]
        count[digit] -= 1

    # Copy the output array to arr[], so that arr[] now contains sorted numbers according to current digit
    arr[:] = output[:]


def _radix_sort(arr, base):
    arr_max = max(arr)
    arr_len = len(arr)

    # Do counting sort for every digit. Note that instead of passing digit number, exp is passed.
    # exp is base^i where i is current digit number
    exp = 1
    while arr_max/exp > 0:
        count_sort(arr, arr_len, exp, base)
        exp *= base


def radix_sort(arr):
    # http://www.geeksforgeeks.org/radix-sort/#highlighter_259275
    _radix_sort(arr, 10)



def merge_sort2_rec(arr, start, end, buff):

    if start >= end - 1:
        return

    mid = (start + end) / 2

    # rec left
    merge_sort2_rec(arr, start, mid, buff)
    # rec right
    merge_sort2_rec(arr, mid, end, buff)

    # merge into buff
    l_i = start
    r_i = mid
    for i in xrange(start, end):
        if r_i == end or (l_i < mid and arr[l_i] <= arr[r_i]):
            buff[i] = arr[l_i]
            l_i += 1
        else:
            buff[i] = arr[r_i]
            r_i += 1

    # copy buff back in arr
    arr[start:end] = buff[start:end]

def merge_sort2(arr):
    merge_sort2_rec(arr, 0, len(arr), [0] * len(arr))

def main():
    import random
    import time
    import pprint
    import sys

    sort_functions = [insert_sort, bubble_sort, quick_sort, merge_sort, heap_sort, radix_sort]

    dic_times = {}
    for i in xrange(0, 4):
        size = 10 ** i
        sys.setrecursionlimit(size * 10)

        sort_functions_times = {}
        for function in sort_functions:
            sort_times = []

            sorted_array = range(size)
            reverse_array = range(size + 1, -1, -1)
            shuffled_array = sorted_array[:]
            random.shuffle(shuffled_array)
            arrays = [sorted_array, reverse_array, shuffled_array]

            for array in arrays:
                start_time = time.time()
                function(array)
                sort_time = time.time() - start_time
                sort_times.append(sort_time)

            sort_functions_times[function.__name__] = sort_times

        dic_times[size] = sort_functions_times

    pprint.pprint(dic_times)


if __name__ == "__main__":
    import random
    sorted_array = range(30)
    shuffled_array = sorted_array[:]
    random.shuffle(shuffled_array)
    merge_sort2(shuffled_array)
    print shuffled_array
    main()