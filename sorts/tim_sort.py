from typing import List

def binary_search(lst: List[int], item: int, start: int, end: int) -> int:
    """
    Perform a Binary Search on the list to find where the item fits in
    Args:
        lst: The list to search
        item: The item to search for
        start: Start index of the segment to search in
        end: End index of the segment to search in

    Returns:
         The index found or -1 if not found
    """
    if start > end:
        return start

    mid = get_mid_point(start, end)

    if is_item_found(lst, mid, item):
        return mid
    elif is_item_less_than_mid(lst, mid, item):
        return binary_search(lst, item, start, mid - 1)
    else:
        return binary_search(lst, item, mid + 1, end)


def insertion_sort(lst):
    length = len(lst)

    for index in range(1, length):
        value = lst[index]
        pos = binary_search(lst, value, 0, index - 1)
        lst = lst[:pos] + [value] + lst[pos:index] + lst[index + 1 :]

    return lst


def get_mid_point(start: int, end: int) -> int:
    """Calculate mid point"""
    return (start + end) // 2

def merge(left: List[int], right: List[int]) -> List[int]:
    """
    This function takes two sorted lists and merges them into a single sorted list.

    Parameters
    ----------
    left : List[int]
        A sorted list of integers.
    right : List[int]
        An another sorted list of integers.

    Returns
    -------
    List[int]
        A single sorted list which is a combination of left and right lists.

    The function uses Python inbuilt list methods to sort and merge the lists.
    """
    # Initialize an empty result list
    result: List[int] = []

    # Loop through both lists until one is empty
    while left and right:
        # Compare the first element of both lists and append the smallest one to the result
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))

    # Append any remaining elements (if any) to the result
    result.extend(left if left else right)

    return result


def is_item_found(lst: List[int], mid: int, item: int) -> bool:
    """Check if item is equal to Mid point"""
    return lst[mid] == item


def is_item_less_than_mid(lst: List[int], mid: int, item: int) -> bool:
    """Check if item is less than Mid point"""
    return lst[mid] > item


def tim_sort(lst):
    """
    >>> tim_sort("Python")
    ['P', 'h', 'n', 'o', 't', 'y']
    >>> tim_sort((1.1, 1, 0, -1, -1.1))
    [-1.1, -1, 0, 1, 1.1]
    >>> tim_sort(list(reversed(list(range(7)))))
    [0, 1, 2, 3, 4, 5, 6]
    >>> tim_sort([3, 2, 1]) == insertion_sort([3, 2, 1])
    True
    >>> tim_sort([3, 2, 1]) == sorted([3, 2, 1])
    True
    """
    length = len(lst)
    runs, sorted_runs = [], []
    new_run = [lst[0]]
    sorted_array = []
    i = 1
    while i < length:
        if lst[i] < lst[i - 1]:
            runs.append(new_run)
            new_run = [lst[i]]
        else:
            new_run.append(lst[i])
        i += 1
    runs.append(new_run)

    for run in runs:
        sorted_runs.append(insertion_sort(run))
    for run in sorted_runs:
        sorted_array = merge(sorted_array, run)

    return sorted_array


def main():
    lst = [5, 9, 10, 3, -4, 5, 178, 92, 46, -18, 0, 7]
    sorted_lst = tim_sort(lst)
    print(sorted_lst)


if __name__ == "__main__":
    main()
