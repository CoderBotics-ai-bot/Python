from typing import List


def binary_search(array: List[int], value: int) -> int:
    """
    Function to initial call to recursive binary search helper.
    """
    return binary_search_helper(array, 0, len(array) - 1, value)


def mat_bin_search(value: int, matrix: list) -> list:
    """
    This function loops over a 2d matrix and calls binarySearch on
    the selected 1d array and returns [-1, -1] is it do not exist
    value : value meant to be searched
    matrix = a sorted 2d matrix
    >>> matrix = [[1, 4, 7, 11, 15],
    ...           [2, 5, 8, 12, 19],
    ...           [3, 6, 9, 16, 22],
    ...           [10, 13, 14, 17, 24],
    ...           [18, 21, 23, 26, 30]]
    >>> target = 1
    >>> mat_bin_search(target, matrix)
    [0, 0]
    >>> target = 34
    >>> mat_bin_search(target, matrix)
    [-1, -1]
    """
    index = 0
    if matrix[index][0] == value:
        return [index, 0]
    while index < len(matrix) and matrix[index][0] < value:
        r = binary_search(matrix[index], 0, len(matrix[index]) - 1, value)
        if r != -1:
            return [index, r]
        index += 1
    return [-1, -1]



def binary_search_helper(
    array: List[int], lower_bound: int, upper_bound: int, value: int
) -> int:
    """
    Recursive helper function to perform the binary search.
    """
    if lower_bound > upper_bound:
        return -1

    mid = (lower_bound + upper_bound) // 2
    if array[mid] < value:
        return binary_search_helper(array, mid + 1, upper_bound, value)
    elif array[mid] > value:
        return binary_search_helper(array, lower_bound, mid - 1, value)
    else:
        return mid


if __name__ == "__main__":
    import doctest

    doctest.testmod()
