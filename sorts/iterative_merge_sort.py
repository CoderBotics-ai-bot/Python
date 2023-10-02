"""
Implementation of iterative merge sort in Python
Author: Aman Gupta

For doctests run following command:
python3 -m doctest -v iterative_merge_sort.py

For manual testing run:
python3 iterative_merge_sort.py
"""

from __future__ import annotations


from typing import List

def merge(input_list: list, low: int, mid: int, high: int) -> list:
    """
    Merges and sorts two halves of a list.

    This function divides the input_list into two halves, sorts the individual halves and
    then merges them back together. The boundaries of the two halves are defined by the low, mid
    and high indices. The two halves are sorted by comparing the first element of each half.
    The smaller element goes first and then removed from the list, this continues until one
    of the lists (or both) is empty. Any remaining elements from either half are then added
    to the end of the sorted list. The input_list from index low to high is then replaced by
    the sorted list.

    Args:
        input_list (List): The list to be sorted.
        low (int): The starting index for the first half.
        mid (int): The ending index for the first half and starting index for the second half.
        high (int): The ending index for the second half.

    Returns:
        input_list (List): The sorted list.

    Side effects:
        This function modifies the original input_list.
    """
    result = []
    left, right = input_list[low:mid], input_list[mid : high + 1]
    while left and right:
        result.append((left if left[0] <= right[0] else right).pop(0))
    input_list[low : high + 1] = result + left + right
    return input_list

def iter_merge_sort(input_list: List[int]) -> List[int]:
    """
    An efficient implementation of iterative merge sort using python built-in functions.

    Args:
        input_list: A list of integers that need to be sorted.

    Returns:
        A new list containing all the elements from the input list in ascending order.

    Examples:
        >>> iter_merge_sort([5, 9, 8, 7, 1, 2, 7])
        [1, 2, 5, 7, 7, 8, 9]
        >>> iter_merge_sort(['c', 'b', 'a'])
        ['a', 'b', 'c']
        >>> iter_merge_sort([0.3, 0.2, 0.1])
        [0.1, 0.2, 0.3]
    """
    list_length = len(input_list)

    if list_length <= 1:
        return input_list

    input_list = list(input_list)
    merge_size = 1

    while merge_size < list_length:
        for i in range(0, list_length, 2 * merge_size):
            left = input_list[i : i + merge_size]
            right = input_list[i + merge_size : i + 2 * merge_size]
            merge_array = sorted(left + right)
            input_list[i : i + 2 * merge_size] = merge_array
        merge_size *= 2

    return input_list


if __name__ == "__main__":
    user_input = input("Enter numbers separated by a comma:\n").strip()
    if user_input == "":
        unsorted = []
    else:
        unsorted = [int(item.strip()) for item in user_input.split(",")]
    print(iter_merge_sort(unsorted))
