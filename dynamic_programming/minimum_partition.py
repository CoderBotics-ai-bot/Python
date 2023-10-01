"""
Partition a set into two subsets such that the difference of subset sums is minimum
"""


from typing import List


def find_min(arr: List[int]) -> int:
    """
    Find the minimum difference between the sum of elements in two subsets from the given list.
    (as detailed in the original documentation)

    Args:
        arr (List[int]): List of array elements.

    Retruns:
        int: Minimum difference between the sum of two subsets.
    """
    n = len(arr)
    s = sum(arr)
    dp = init_dp(n, s)
    fill_dp(dp, arr, n, s)
    return find_diff(dp, n, s)



def init_dp(n: int, s: int) -> List[List[bool]]:
    """
    Initialize dynamic programming table.

    Args:
        n (int): Number of elements in array.
        s (int): Sum of array elements.

    Returns:
        List[List[bool]]: 2D dynamic programming table.
    """
    dp = [[False for _ in range(s + 1)] for _ in range(n + 1)]
    for i in range(n + 1):
        dp[i][0] = True
    return dp


def fill_dp(dp: List[List[bool]], arr: List[int], n: int, s: int) -> None:
    """
    Fill dynamic programming table.

    Args:
        dp (List[List[bool]]): 2D dynamic programming table.
        arr (List[int]): Array of integers.
        n (int): Number of elements in array.
        s (int): Sum of array elements.
    """
    for i in range(1, n + 1):
        for j in range(1, s + 1):
            dp[i][j] = dp[i - 1][j]
            if arr[i - 1] <= j:
                dp[i][j] |= dp[i - 1][j - arr[i - 1]]


def find_diff(dp: List[List[bool]], n: int, s: int) -> int:
    """
    Compute minimum difference.

    Args:
        dp (List[List[bool]]): 2D dynamic programming table.
        n (int): Number of elements in array.
        s (int): Sum of array elements.

    Returns:
        int: Minimum difference.
    """
    for j in range(s // 2, -1, -1):
        if dp[n][j]:
            return s - 2 * j
