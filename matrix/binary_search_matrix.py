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



def mat_bin_search(value: int, matrix: List[List[int]]) -> List[int]:
    """
    Performs binary search in a 2D sorted matrix and returns the row index and column index if value is found; otherwise, returns [-1, -1].

    Args:
        value (int): The value to be searched in the matrix.
        matrix (List[List[int]]): A 2D sorted matrix.

    Returns:
        List[int]: a list containing the row index and the column index of the value if it is found in the matrix; If not found, returns [-1, -1].
    """

    for row_index, row in enumerate(matrix):
        if value_in_range(row[0], row[-1], value):
            col_index = binary_search(row, 0, len(row) - 1, value)
            if col_index != -1:
                return [row_index, col_index]

    return [-1, -1]


if __name__ == "__main__":
    import doctest

    doctest.testmod()


def value_in_range(low: int, high: int, value: int) -> bool:
    """
    Checks if a value lies within an inclusive range.

    Args:
        low (int): The low end of the range.
        high (int): The high end of the range.
        value (int): The value to check.

    Returns:
        bool: Whether or not the value is within the range.
    """
    return low <= value <= high
