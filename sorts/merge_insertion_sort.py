"""
This is a pure Python implementation of the merge-insertion sort algorithm
Source: https://en.wikipedia.org/wiki/Merge-insertion_sort

For doctests run following command:
python3 -m doctest -v merge_insertion_sort.py
or
python -m doctest -v merge_insertion_sort.py

For manual testing run:
python3 merge_insertion_sort.py
"""

from __future__ import annotations


from typing import List
from typing import List, Union


from typing import List, Union, Tuple

def binary_search_insertion(sorted_list: List[int], item: int) -> List[int]:
    """
    Performs binary search to find an insert position for an item in a sorted list, then inserts the item at that position.
    This results in a new sorted list which includes the inserted item. The function assumes that the input list is already sorted.

    Args:
        sorted_list: List of integers, which is sorted in ascending order.
        item: The integer item to be inserted into the sorted list.

    Returns:
        A new sorted list which includes the inserted item.

    >>> binary_search_insertion([1, 2, 7, 9, 10], 4)
    [1, 2, 4, 7, 9, 10]
    """

    def find_insert_index(
        sorted_list: List[int], item: int, left: int, right: int
    ) -> int:
        """Helper function to find the correct index for insertion."""
        while left <= right:
            middle = (left + right) // 2
            if left == right:
                if sorted_list[middle] < item:
                    return middle + 1
                break
            elif sorted_list[middle] < item:
                left = middle + 1
            else:
                right = middle - 1
        return left

    insert_index = find_insert_index(sorted_list, item, 0, len(sorted_list) - 1)
    sorted_list.insert(insert_index, item)
    return sorted_list

def merge(left: List[List[int]], right: List[List[int]]) -> List[List[int]]:
    """
    Merge two lists in sorted order.

    Args:
        left (List[List[int]]): The first list.
        right (List[List[int]]): The second list.

    Returns:
        List[List[int]]: The merged list in sorted order.
    """
    result = []
    while left and right:
        if left[0][0] < right[0][0]:
            result.append(left.pop(0))
            continue
        result.append(right.pop(0))

    return result + (left or right)


def sortlist_2d(list_2d):
    """
    >>> sortlist_2d([[9, 10], [1, 6], [7, 8], [2, 3], [4, 5]])
    [[1, 6], [2, 3], [4, 5], [7, 8], [9, 10]]
    """
    length = len(list_2d)
    if length <= 1:
        return list_2d
    middle = length // 2
    return merge(sortlist_2d(list_2d[:middle]), sortlist_2d(list_2d[middle:]))


def merge_insertion_sort(
    collection: List[Union[int, float]]
) -> List[Union[int, float]]:
    if len(collection) <= 1:
        return collection

    two_paired_list, has_last_odd_item = group_and_sort_pairs(collection)

    result, sorted_list_2d = initial_sorted_list(two_paired_list)

    if has_last_odd_item:
        pivot = collection[-1]
        result = binary_search_insertion(result, pivot)

    is_last_odd_item_inserted_before_this_index = False
    for i in range(len(sorted_list_2d) - 1):
        if result[i] == collection[-1] and has_last_odd_item:
            is_last_odd_item_inserted_before_this_index = True
        pivot = sorted_list_2d[i][1]

        if is_last_odd_item_inserted_before_this_index:
            result = result[: i + 2] + binary_search_insertion(result[i + 2 :], pivot)
        else:
            result = result[: i + 1] + binary_search_insertion(result[i + 1 :], pivot)

    return result


if __name__ == "__main__":
    user_input = input("Enter numbers separated by a comma:\n").strip()
    unsorted = [int(item) for item in user_input.split(",")]
    print(merge_insertion_sort(unsorted))

def group_and_sort_pairs(
    collection: List[Union[int, float]]
) -> Tuple[List[List[Union[int, float]]], bool]:
    """
    Group the items into pairs, sort them and return paired list and Boolean indicating presence of odd item.
    """
    two_paired_list = []
    has_last_odd_item = False
    for i in range(0, len(collection), 2):
        if i == len(collection) - 1:
            has_last_odd_item = True
        else:
            two_paired_list.append(sorted([collection[i], collection[i + 1]]))
    return two_paired_list, has_last_odd_item


def initial_sorted_list(
    two_paired_list: List[List[Union[int, float]]]
) -> List[Union[int, float]]:
    """
    Generate initial sorted list with elements from 2d paired list to avoid unnecessary comparison.
    """
    sorted_list_2d = sortlist_2d(two_paired_list)
    result = [i[0] for i in sorted_list_2d]
    result.append(sorted_list_2d[-1][1])
    return result, sorted_list_2d
