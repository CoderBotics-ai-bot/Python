"""
This is a pure Python implementation of the binary insertion sort algorithm

For doctests run following command:
python -m doctest -v binary_insertion_sort.py
or
python3 -m doctest -v binary_insertion_sort.py

For manual testing run:
python binary_insertion_sort.py
"""

def binary_insertion_sort(collection: list) -> list:
    """
    Pure implementation of the binary insertion sort algorithm in Python.

    Args:
        collection (list): A mutable ordered collection with heterogeneous
        comparable items inside.

    Returns:
        list: The same collection ordered by ascending.
    """

    for i in range(1, len(collection)):
        val = collection[i]
        proper_index = binary_search(collection, val, i)
        shift_elements(collection, val, i, proper_index)

    return collection


if __name__ == "__main__":
    user_input = input("Enter numbers separated by a comma:\n").strip()
    unsorted = [int(item) for item in user_input.split(",")]
    print(binary_insertion_sort(unsorted))


def binary_search(collection: list, value: int, upper_bound: int) -> int:
    """
    Performs a binary search in the collection to find the proper location to
    insert the selected item.

    Args:
        collection (list): A mutable ordered collection with heterogeneous
            comparable items inside.
        value (int): Value to be inserted.
        upper_bound (int): Upper bound of the search range.

    Returns:
        int: The proper location to insert the selected item.
    """
    low = 0

    while low < upper_bound:
        mid = (low + upper_bound) // 2
        if value < collection[mid]:
            upper_bound = mid
        else:
            low = mid + 1

    return low


def shift_elements(collection: list, value: int, start: int, end: int) -> None:
    """
    Shifts elements in the collection to make place for newly inserted element.

    Args:
        collection (list): A mutable ordered collection with heterogeneous
            comparable items inside.
        value (int): Value to be inserted.
        start (int): The starting position of shifting.
        end (int): The ending position of shifting.
    """

    for j in range(start, end, -1):
        collection[j] = collection[j - 1]

    collection[end] = value
