

from typing import List


def is_sum_subset(arr: list[int], required_sum: int) -> bool:
    """
    Checks if a subset exists within a given array of integers which carries up to a specified target sum.

    Args:
        arr (list[int]): List of integers to search for subsets.
        required_sum (int): The target sum for the subset to reach.

    Returns:
        bool: Returns True if a subset that adds to the required_sum is found, otherwise False.
    """
    arr_len = len(arr)
    subset = initialize_subset(arr_len, required_sum)

    # for each arr value, a sum of zero(0) can be formed by not taking any element
    # hence True/1
    for i in range(arr_len + 1):
        subset[i][0] = True

    # start from 1 since we already handled case for sum 0
    for i in range(1, arr_len + 1):
        for j in range(1, required_sum + 1):
            subset_value = subset[i - 1][j]

            if arr[i - 1] <= j:
                subset_value = subset_value or subset[i - 1][j - arr[i - 1]]

            subset[i][j] = subset_value

    return subset[arr_len][required_sum]


if __name__ == "__main__":
    import doctest

    doctest.testmod()

def initialize_subset(arr_len: int, required_sum: int) -> list[list[bool]]:
    """
    Initializes and returns a 2D list (subset) with dimensions arr_len+1 and required_sum+1
    """
    return [[False for _ in range(required_sum + 1)] for _ in range(arr_len + 1)]
