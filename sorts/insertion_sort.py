"""
A pure Python implementation of the insertion sort algorithm

This algorithm sorts a collection by comparing adjacent elements.
When it finds that order is not respected, it moves the element compared
backward until the order is correct.  It then goes back directly to the
element's initial position resuming forward comparison.

For doctests run following command:
python3 -m doctest -v insertion_sort.py

For manual testing run:
python3 insertion_sort.py
"""


from typing import List, Union



def insertion_sort(collection: List[Union[int, str]]) -> List[Union[int, str]]:
    """
    A pure Python implementation of the insertion sort algorithm

    This function takes in a list of integers or strings and
    returns a list sorted in ascending order using the insertion sort
    algorithm. Insertion sort is a simple sorting algorithm that
    builds the final sorted array one item at a time. It is more efficient
    than bubble sort and selection sort for smaller datasets.

    Arguments:
    collection : List[Union[int, str]] -- input list of integers or strings.

    Returns:
    List[Union[int, str]] -- sorted list in ascending order.

    Example:

    >>> insertion_sort([0, 5, 3, 2, 2])
    [0, 2, 2, 3, 5]

    """
    for insert_index in range(1, len(collection)):
        insert_value = collection[insert_index]
        collection = shift_elements_right(collection, insert_index, insert_value)
    return collection


if __name__ == "__main__":
    from doctest import testmod

    testmod()

    user_input = input("Enter numbers separated by a comma:\n").strip()
    unsorted = [int(item) for item in user_input.split(",")]
    print(f"{insertion_sort(unsorted) = }")


def shift_elements_right(
    collection: List[Union[int, str]], insert_index: int, insert_value: Union[int, str]
) -> List[Union[int, str]]:
    """
    A helper function that shifts elements to the right in a collection.

    This function takes in a collection, an insert index, and an insert value.
    It performs the shifting operation of the insertion sort algorithm.

    Arguments:
    collection : List[Union[int, str]] -- input list of integers or strings.
    insert_index : int -- insert index.
    insert_value : Union[int, str] -- insert value.

    Returns:
    List[Union[int, str]] -- list with elements shifted to the right.

    """
    while insert_index > 0 and insert_value < collection[insert_index - 1]:
        collection[insert_index] = collection[insert_index - 1]
        insert_index -= 1
    collection[insert_index] = insert_value

    return collection
