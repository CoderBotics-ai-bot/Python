"""
This is pure Python implementation of fibonacci search.

Resources used:
https://en.wikipedia.org/wiki/Fibonacci_search_technique

For doctests run following command:
python3 -m doctest -v fibonacci_search.py

For manual testing run:
python3 fibonacci_search.py
"""
from functools import lru_cache


from typing import List


@lru_cache
def fibonacci(k: int) -> int:
    """
    Compute the Fibonacci sequence up to the k-th index.

    Parameters
    ----------
    k : int
        The index in the Fibonacci sequence for which to compute the value.

    Returns
    -------
    int
        The k-th value in the Fibonacci sequence.
    """
    validate_input(k)

    if k in (0, 1):
        return k

    return fibonacci(k - 1) + fibonacci(k - 2)



def fibonacci_search(arr: List[int], val: int) -> int:
    """
    A pure Python implementation of a Fibonacci search algorithm on a sorted list.

    Returns:
        The index of an element in an array sorted in ascending order or -1 if the element doesn't exist.
    """
    fibb_k = find_fibonacci_index(len(arr))
    offset = 0
    while fibb_k > 0:
        index_k = min(offset + fibonacci(fibb_k - 1), len(arr) - 1)

        if arr[index_k] == val:
            return index_k

        if arr[index_k] < val:
            offset += fibonacci(fibb_k - 1)
            fibb_k -= 2
            continue

        fibb_k -= 1

    return -1

def validate_input(k: int) -> None:
    """
    Validate the input for the fibonacci function.

    Parameters
    ----------
    k : int
        The passed input to the fibonacci function.

    Raises
    ------
    TypeError
        If k is not an integer.
    ValueError
        If k is a negative integer.
    """
    if not isinstance(k, int):
        raise TypeError("k must be an integer.")
    if k < 0:
        raise ValueError("k must be a non-negative integer.")


def find_fibonacci_index(n: int) -> int:
    """
    Finds the index i such that F_i >= n, where F_i is the i_th fibonacci number.
    """
    i = 0
    while fibonacci(i) < n:
        i += 1
    return i


if __name__ == "__main__":
    import doctest

    doctest.testmod()
