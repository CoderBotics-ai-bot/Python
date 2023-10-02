"""
Bead sort only works for sequences of non-negative integers.
https://en.wikipedia.org/wiki/Bead_sort
"""

def bead_sort(sequence: list) -> list:
    """
    Apply bead sort algorithm to given sequence.

    This function sorts a sequence of non-negative integers in ascending order using the
    bead sort algorithm.

    Bead sort is a sorting algorithm that can be used to sort lists of non-negative integers.
    It operates by moving beads up and down a set of rods until they're all in the right sequence.

    The function checks the input sequence for appropriate datatype, ie., list of non-negative integers.
    TypeError or ValueError will be raised if the sequence contains elements which are not non-negative integers.

    Each additional pass of the list takes the input list of numbers and moves a "bead" from any "rod" (item)
    that's in the wrong position to a lower rod that's in the wrong position until all rods have the correct number of beads.

    Args:

    sequence (list): List of non-negative integers which needs to be sorted.

    Returns:

    list: Sorted list of non-negative integers.

    Raises:

    TypeError: If any of the elements in the input list are not integers.
    ValueError: If any of the elements in the input list are negative.

    Examples:
    >>> bead_sort([6, 11, 12, 4, 1, 5])
    [1, 4, 5, 6, 11, 12]

    >>> bead_sort([9, 8, 7, 6, 5, 4 ,3, 2, 1])
    [1, 2, 3, 4, 5, 6, 7, 8, 9]

    >>> bead_sort([5, 0, 4, 3])
    [0, 3, 4, 5]

    >>> bead_sort("Hello world")
    Traceback (most recent call last):
    ...
    TypeError: Elements in sequence must be integers

    >>> bead_sort([-1, 0, 1])
    Traceback (most recent call last):
    ...
    ValueError: Elements in sequence must be non-negative
    """
    _check_sequence(sequence)
    for _ in range(len(sequence)):
        for i, (rod_upper, rod_lower) in enumerate(zip(sequence, sequence[1:])):
            if rod_upper > rod_lower:
                sequence[i], sequence[i + 1] = sequence[i + 1], sequence[i]
    return sequence


if __name__ == "__main__":
    assert bead_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
    assert bead_sort([7, 9, 4, 3, 5]) == [3, 4, 5, 7, 9]


def _check_sequence(sequence: list):
    """
    Check types and values of the elements in sequence used for bead_sort.

    Raises:
        TypeError: If any of the elements in the sequence are not integers.
        ValueError: If any of the elements in the sequence are negative.
    """
    for elem in sequence:
        if not isinstance(elem, int):
            raise TypeError("Elements in sequence must be integers")
        elif elem < 0:
            raise ValueError("Elements in sequence must be non-negative")
