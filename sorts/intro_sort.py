"""
Introspective Sort is hybrid sort (Quick Sort + Heap Sort + Insertion Sort)
if the size of the list is under 16, use insertion sort
https://en.wikipedia.org/wiki/Introsort
"""
import math


def insertion_sort(array: list, start: int = 0, end: int = 0) -> list:
    """
    A function that sorts a list of elements using the Insertion Sort algorithm.

    Args:
        array (list): The list of elements to be sorted.
        start (int, optional): The starting index from where to start sorting, default is 0.
        end (int, optional): The end index till where to sort. If not specified, entire list is sorted.

    Returns:
        list: A sorted list.

    Examples:
        >>> array = [4, 2, 6, 8, 1, 7, 8, 22, 14, 56, 27, 79, 23, 45, 14, 12]
        >>> insertion_sort(array, 0, len(array))
        [1, 2, 4, 6, 7, 8, 8, 12, 14, 14, 22, 23, 27, 45, 56, 79]
    """
    end = end or len(array)
    for i in range(start, end):
        array[shift_elements(array, start, i)] = array[i]
    return array


def heapify(array: list, index: int, heap_size: int) -> None:
    """Converts a given array into a max heap at a given index within a heap of certain size.

    This function enforces the max-heap property on the array, i.e., for any given node i,
    array[i] is not smaller than its children. This property is recursively enforced on the
    left and right subtrees of the node.

    Args:
        array (list): Input list to be converted into a heap.
        index (int): The index where the heapify operation needs to be performed.
        heap_size (int): The number of elements in the heap. Heapify operation is confined to this size.

    Returns:
        None: The function modifies the array in-place, does not return a value.
    """
    largest = index
    left_index, right_index = 2 * index + 1, 2 * index + 2  # Left and Right Node

    if is_larger(array, left_index, largest):
        largest = left_index

    if is_larger(array, right_index, largest):
        largest = right_index

    if largest != index:
        swap_elements(array, largest, index)
        heapify(array, largest, heap_size)

def shift_elements(array: list, start: int, index: int) -> int:
    """Shifts elements to right in array starting from start and till index

    Args:
        array (list): array where elements needs to be shifted
        start (int): start index of array where shifting needs to start
        index (int): index of array till where elements needs to be shifted

    Returns:
        int: position where current index element should be located
    """
    temp_index_value = array[index]
    while index != start and temp_index_value < array[index - 1]:
        array[index] = array[index - 1]
        index -= 1
    return index

def is_larger(array: list, i: int, j: int) -> bool:
    """Checks if array[i] is larger than array[j].

    Returns:
        bool: True if array[i] > array[j], else False.
    """
    try:
        return array[i] > array[j]
    except IndexError:
        return False


def swap_elements(array: list, i: int, j: int) -> None:
    """Swap the elements of array at positions i and j."""
    array[i], array[j] = array[j], array[i]


def heap_sort(array: list) -> list:
    """
    >>> array = [4, 2, 6, 8, 1, 7, 8, 22, 14, 56, 27, 79, 23, 45, 14, 12]

    >>> heap_sort(array)
    [1, 2, 4, 6, 7, 8, 8, 12, 14, 14, 22, 23, 27, 45, 56, 79]
    """
    n = len(array)

    for i in range(n // 2, -1, -1):
        heapify(array, i, n)

    for i in range(n - 1, 0, -1):
        array[i], array[0] = array[0], array[i]
        heapify(array, 0, i)

    return array


def median_of_3(
    array: list, first_index: int, middle_index: int, last_index: int
) -> int:
    """
    >>> array = [4, 2, 6, 8, 1, 7, 8, 22, 14, 56, 27, 79, 23, 45, 14, 12]

    >>> median_of_3(array, 0, 0 + ((len(array) - 0) // 2) + 1, len(array) - 1)
    12
    """
    if (array[first_index] > array[middle_index]) != (
        array[first_index] > array[last_index]
    ):
        return array[first_index]
    elif (array[middle_index] > array[first_index]) != (
        array[middle_index] > array[last_index]
    ):
        return array[middle_index]
    else:
        return array[last_index]


def partition(array: list, low: int, high: int, pivot: int) -> int:
    """
    >>> array = [4, 2, 6, 8, 1, 7, 8, 22, 14, 56, 27, 79, 23, 45, 14, 12]

    >>> partition(array, 0, len(array), 12)
    8
    """
    i = low
    j = high
    while True:
        while array[i] < pivot:
            i += 1
        j -= 1
        while pivot < array[j]:
            j -= 1
        if i >= j:
            return i
        array[i], array[j] = array[j], array[i]
        i += 1


def sort(array: list) -> list:
    """
    :param collection: some mutable ordered collection with heterogeneous
    comparable items inside
    :return: the same collection ordered by ascending

    Examples:
    >>> sort([4, 2, 6, 8, 1, 7, 8, 22, 14, 56, 27, 79, 23, 45, 14, 12])
    [1, 2, 4, 6, 7, 8, 8, 12, 14, 14, 22, 23, 27, 45, 56, 79]

    >>> sort([-1, -5, -3, -13, -44])
    [-44, -13, -5, -3, -1]

    >>> sort([])
    []

    >>> sort([5])
    [5]

    >>> sort([-3, 0, -7, 6, 23, -34])
    [-34, -7, -3, 0, 6, 23]

    >>> sort([1.7, 1.0, 3.3, 2.1, 0.3 ])
    [0.3, 1.0, 1.7, 2.1, 3.3]

    >>> sort(['d', 'a', 'b', 'e', 'c'])
    ['a', 'b', 'c', 'd', 'e']
    """
    if len(array) == 0:
        return array
    max_depth = 2 * math.ceil(math.log2(len(array)))
    size_threshold = 16
    return intro_sort(array, 0, len(array), size_threshold, max_depth)


def intro_sort(
    array: list, start: int, end: int, size_threshold: int, max_depth: int
) -> list:
    """
    >>> array = [4, 2, 6, 8, 1, 7, 8, 22, 14, 56, 27, 79, 23, 45, 14, 12]

    >>> max_depth = 2 * math.ceil(math.log2(len(array)))

    >>> intro_sort(array, 0, len(array), 16, max_depth)
    [1, 2, 4, 6, 7, 8, 8, 12, 14, 14, 22, 23, 27, 45, 56, 79]
    """
    while end - start > size_threshold:
        if max_depth == 0:
            return heap_sort(array)
        max_depth -= 1
        pivot = median_of_3(array, start, start + ((end - start) // 2) + 1, end - 1)
        p = partition(array, start, end, pivot)
        intro_sort(array, p, end, size_threshold, max_depth)
        end = p
    return insertion_sort(array, start, end)


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    user_input = input("Enter numbers separated by a comma : ").strip()
    unsorted = [float(item) for item in user_input.split(",")]
    print(sort(unsorted))
