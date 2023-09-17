from typing import List


def binary_search(array: List[int], value: int) -> int:
    """
    Function to initial call to recursive binary search helper.
    """
    return binary_search_helper(array, 0, len(array) - 1, value)

def mat_bin_search(value: int, matrix: List[List[int]]) -> List[int]:
    """
    Conducts binary search for a value in a sorted 2D matrix.

    This function iterates over each 1D list in the given 2D matrix and performs binary search.
    If the value is found, it returns the indices [row, column] where the value is located.
    If the value is not present in the matrix, it returns [-1, -1].

    Args:
        value (int): The value to search for in the matrix.
        matrix (List[List[int]]): The sorted 2D matrix to search.

    Returns:
        List[int]: A list with two elements, [row, column] which
                   represent the indices where the value is located
                   in the matrix. If the value is not present in the matrix,
                   [-1, -1] is returned.

    Examples:
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
    for i, row in enumerate(matrix):
        if row[0] <= value:
            found_at = binary_search(row, 0, len(row) - 1, value)
            if found_at != -1:
                return [i, found_at]
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
