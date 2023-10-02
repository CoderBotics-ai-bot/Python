"""
This function implements the shell sort algorithm
which is slightly faster than its pure implementation.

This shell sort is implemented using a gap, which
shrinks by a certain factor each iteration. In this
implementation, the gap is initially set to the
length of the collection. The gap is then reduced by
a certain factor (1.3) each iteration.

For each iteration, the algorithm compares elements
that are a certain number of positions apart
(determined by the gap). If the element at the higher
position is greater than the element at the lower
position, the two elements are swapped. The process
is repeated until the gap is equal to 1.

The reason this is more efficient is that it reduces
the number of comparisons that need to be made. By
using a smaller gap, the list is sorted more quickly.
"""


from typing import List

def shell_sort(collection: List[int]) -> List[int]:
    """
    Implement the shell sort algorithm in Python and sort a given list in ascending order.

    Shell sort is a generalized version of insertion sort. In shell sort, elements at a specific interval are sorted.
    The interval between the elements is gradually decreased based on the sequence used.
    The performance of the shell sort depends on the type of sequence used for a given input array.

    Parameters:
    collection (List[int]): A mutable ordered collection with heterogeneous comparable items inside

    Returns:
    List[int]: The original collection ordered in ascending order

    Doctests:
    >>> shell_sort([3, 2, 1])
    [1, 2, 3]
    >>> shell_sort([])
    []
    >>> shell_sort([1])
    [1]
    """
    shrink = 1.3  # Set the gap value to be decreased by a factor of 1.3 after each iteration.
    gap = len(collection)  # Choose an initial gap value.

    while gap > 1:  # Continue sorting until the gap is 1.
        gap = int(gap / shrink)  # Decrease the gap value.
        _insertion_sort_at_gap(collection, gap)

    return collection


if __name__ == "__main__":
    import doctest

    doctest.testmod()


def _insertion_sort_at_gap(collection: List[int], gap: int) -> None:
    """
    Helper function to perform insertion sort at a given gap.

    The function modifies the input collection in-place.

    Parameters:
    collection (List[int]): The collection to sort.
    gap (int): The gap to use when sorting.
    """
    for i in range(gap, len(collection)):
        temp = collection[i]
        j = i
        while j >= gap and collection[j - gap] > temp:
            collection[j] = collection[j - gap]
            j -= gap
        collection[j] = temp
