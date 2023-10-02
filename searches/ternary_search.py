"""
This is a type of divide and conquer algorithm which divides the search space into
3 parts and finds the target value based on the property of the array or list
(usually monotonic property).

Time Complexity  : O(log3 N)
Space Complexity : O(1)
"""
from __future__ import annotations
from typing import List, Tuple

# This is the precision for this function which can be altered.
# It is recommended for users to keep this number greater than or equal to 10.
precision = 10


# This is the linear search that will occur after the search space has become smaller.


def lin_search(left: int, right: int, array: list[int], target: int) -> int:
    """Perform linear search in list. Returns -1 if element is not found.

    Parameters
    ----------
    left : int
        left index bound.
    right : int
        right index bound.
    array : List[int]
        List of elements to be searched on
    target : int
        Element that is searched

    Returns
    -------
    int
        index of element that is looked for.

    Examples
    --------
    >>> lin_search(0, 4, [4, 5, 6, 7], 7)
    3
    >>> lin_search(0, 3, [4, 5, 6, 7], 7)
    -1
    >>> lin_search(0, 2, [-18, 2], -18)
    0
    >>> lin_search(0, 1, [5], 5)
    0
    >>> lin_search(0, 3, ['a', 'c', 'd'], 'c')
    1
    >>> lin_search(0, 3, [.1, .4 , -.1], .1)
    0
    >>> lin_search(0, 3, [.1, .4 , -.1], -.1)
    2
    """
    for i in range(left, right):
        if array[i] == target:
            return i
    return -1


def ite_ternary_search(array: list[int], target: int) -> int:
    """
    Perform iterative ternary search on an ordered list and return the index of the target element.
    If target is not found, return -1.

    The function will perform a ternary search, which is an improvement over binary search for long lists,
    and switch to linear search when the remaining slice of the list is smaller than 10.
    It checks at two points (one_third and two_third) in the array.

    Parameters:
    array (List[int]): ordered list of integers to be searched
    target (int): integer to be searched for in the list

    Returns:
    int: the index in the array where the target element is located; returns -1 if target is not found
    """
    left = 0
    right = len(array) - 1
    while left <= right:
        if right - left < precision:
            return lin_search(left, right, array, target)

        one_third = (2 * left + right) // 3
        two_third = (left + 2 * right) // 3

        target_index = find_target_at_boundaries(one_third, two_third, array, target)

        if target_index != -1:
            return target_index

        left, right = update_search_boundaries(
            one_third, two_third, array, target, left, right
        )
    return -1


def rec_ternary_search(left: int, right: int, array: list[int], target: int) -> int:
    """Recursive method of the ternary search algorithm.

    >>> test_list = [0, 1, 2, 8, 13, 17, 19, 32, 42]
    >>> rec_ternary_search(0, len(test_list), test_list, 3)
    -1
    >>> rec_ternary_search(4, len(test_list), test_list, 42)
    8
    >>> rec_ternary_search(0, 2, [4, 5, 6, 7], 4)
    0
    >>> rec_ternary_search(0, 3, [4, 5, 6, 7], -10)
    -1
    >>> rec_ternary_search(0, 1, [-18, 2], -18)
    0
    >>> rec_ternary_search(0, 1, [5], 5)
    0
    >>> rec_ternary_search(0, 2, ['a', 'c', 'd'], 'c')
    1
    >>> rec_ternary_search(0, 2, ['a', 'c', 'd'], 'f')
    -1
    >>> rec_ternary_search(0, 0, [], 1)
    -1
    >>> rec_ternary_search(0, 3, [.1, .4 , -.1], .1)
    0
    """
    if left < right:
        if right - left < precision:
            return lin_search(left, right, array, target)
        one_third = (left + right) // 3 + 1
        two_third = 2 * (left + right) // 3 + 1

        if array[one_third] == target:
            return one_third
        elif array[two_third] == target:
            return two_third

        elif target < array[one_third]:
            return rec_ternary_search(left, one_third - 1, array, target)
        elif array[two_third] < target:
            return rec_ternary_search(two_third + 1, right, array, target)
        else:
            return rec_ternary_search(one_third + 1, two_third - 1, array, target)
    else:
        return -1

def find_target_at_boundaries(
    one_third: int, two_third: int, array: list[int], target: int
) -> int:
    """
    This function is a helper function for the ite_ternary_search function.
    It checks if the target element is found at the one_third and two_third of array.

    Parameters:
    one_third (int): integer representing one third index of the array
    two_third (int): integer representing two third index of the array
    array (List[int]): ordered list of integers to be searched
    target (int): integer to be searched for in the list

    Returns:
    int: the index in the array where the target element is located; returns -1 if target is not found
    """
    if array[one_third] == target:
        return one_third
    if array[two_third] == target:
        return two_third
    return -1


def update_search_boundaries(
    one_third: int, two_third: int, array: list[int], target: int, left: int, right: int
) -> tuple[int, int]:
    """
    This function is a helper function for the ite_ternary_search function.
    It updates the search boundaries based on the comparison with target element.

    Parameters:
    one_third (int): integer representing one third index of the array
    two_third (int): integer representing two third index of the array
    array (List[int]): ordered list of integers to be searched
    target (int): integer to be searched for in the list
    left (int): left boundary for search
    right (int): right boundary for search

    Returns:
    Tuple[int,int]: updated left and right boundaries for ternary search
    """
    if target < array[one_third]:
        return left, one_third - 1
    elif target > array[two_third]:
        return two_third + 1, right
    else:
        return one_third + 1, two_third - 1


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    user_input = input("Enter numbers separated by comma:\n").strip()
    collection = [int(item.strip()) for item in user_input.split(",")]
    assert collection == sorted(collection), f"List must be ordered.\n{collection}."
    target = int(input("Enter the number to be found in the list:\n").strip())
    result1 = ite_ternary_search(collection, target)
    result2 = rec_ternary_search(0, len(collection) - 1, collection, target)
    if result2 != -1:
        print(f"Iterative search: {target} found at positions: {result1}")
        print(f"Recursive search: {target} found at positions: {result2}")
    else:
        print("Not found")
