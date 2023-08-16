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

def abbr(a: str, b: str) -> bool:
    """
    Checks if string `a` can be abbreviated to string `b`.

    This function uses a dynamic programming approach to determine if string `a` can be abbreviated to string `b`
    by deleting zero or more characters from `a`.

    Arguments:
    a: str - The first string.
    b: str - The string we want to abbreviate to.

    Returns:
    bool: True if string `a` can be abbreviated to string `b`, otherwise False.

    Examples:
    >>> abbr("daBcd", "ABC")
    True
    >>> abbr("dBcd", "ABC")
    False
    """
    n = len(a)
    m = len(b)
    dp = [[False for _ in range(m + 1)] for _ in range(n + 1)]
    dp[0][0] = True
    for i in range(n):
        for j in range(m + 1):
            if dp[i][j]:
                if j < m and a[i].upper() == b[j]:
                    dp[i + 1][j + 1] = True
                if a[i].islower():
                    dp[i + 1][j] = True
    return dp[n][m]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
