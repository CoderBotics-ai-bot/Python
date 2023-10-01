from typing import List

def binary_search(
    array: List[int], lower_bound: int, upper_bound: int, value: int
) -> int:
    """
    Performs Binary search on a 1D array.

    This function searches for a specific value within a 1D sorted array and
    returns the index of the value if it exists; otherwise, returns -1.

    Args:
        array (List[int]): A 1D sorted array.
        lower_bound (int): The lower bound from where search starts in the array.
        upper_bound (int): The upper bound where search ends in the array.
        value (int): The value to be searched in the array.

    Returns:
        int: The index of the value in the array if it exists; Otherwise, returns -1.

    Examples:
        >>> array = [1, 4, 7, 11, 15]
        >>> binary_search(array, 0, len(array) - 1, 1)
        0
        >>> binary_search(array, 0, len(array) - 1, 23)
        -1
    """

    # If lower_bound is greater than upper_bound, value is not in array
    if lower_bound > upper_bound:
        return -1

    mid = (lower_bound + upper_bound) // 2

    # If mid value matches the value, return mid index
    if array[mid] == value:
        return mid

    # If mid value is less than the value, repeat for right subarray
    if array[mid] < value:
        return binary_search(array, mid + 1, upper_bound, value)

    # If mid value is greater than the value, repeat for left subarray
    return binary_search(array, lower_bound, mid - 1, value)


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


if __name__ == "__main__":
    import doctest

    doctest.testmod()
