"""
https://www.hackerrank.com/challenges/abbr/problem
You can perform the following operation on some string, :

1. Capitalize zero or more of 's lowercase letters at some index i
   (i.e., make them uppercase).
2. Delete all of the remaining lowercase letters in .

Example:
a=daBcd and b="ABC"
daBcd -> capitalize a and c(dABCd) -> remove d (ABC)
"""


from typing import List


def abbr(a: str, b: str) -> bool:
    """
    ...Same as before
    """
    n, m = len(a), len(b)
    dp = initialize_dp(n, m)
    dp[0][0] = True

    for i in range(n):
        for j in range(m + 1):
            check_case(a, b, i, j, dp)

    return dp[n][m]


if __name__ == "__main__":
    import doctest

    doctest.testmod()

def initialize_dp(n: int, m: int) -> List[List[bool]]:
    """
    Helper function to initialize dp matrix of boolean values.
    """
    return [[False for _ in range(m + 1)] for _ in range(n + 1)]


def check_case(a: str, b: str, i: int, j: int, dp: List[List[bool]]) -> None:
    """
    Helper function to abstract comparison logic.
    """
    if dp[i][j]:
        if j < len(b) and a[i].upper() == b[j]:
            dp[i + 1][j + 1] = True
        if a[i].islower():
            dp[i + 1][j] = True
