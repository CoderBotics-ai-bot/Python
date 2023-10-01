"""
You have m types of coins available in infinite quantities
where the value of each coins is given in the array S=[S0,... Sm-1]
Can you determine number of ways of making change for n units using
the given types of coins?
https://www.hackerrank.com/challenges/coin-change/problem
"""


from typing import List

def dp_count(s: List[int], n: int) -> int:
    """Counts the total possible arrangements for `s` (where `s`
    are available denominations of points, each can be used
    unlimited number of times) that add up to `n`.

    This function uses Dynamic Programming. It creates an
    array `dp[]` such that `dp[i]` will be storing
    the total arrangements of `s` that adds up to `i`.

    Args:
        s (List[int]):
            The list of available denominations of points.

        n (int):
            Target amount, the arrangements of `s` is aimed
            at adding up to `n`.

    Returns:
        int:
            The total number of possible arrangements for `s`
            that add up to `n`.

    Examples:
        >>> dp_count([1, 2, 3], 4)
        4
        >>> dp_count([1, 2, 3], 7)
        8
        >>> dp_count([2, 5, 3, 6], 10)
        5
        >>> dp_count([10], 99)
        0
        >>> dp_count([4, 5, 6], 0)
        1
        >>> dp_count([1, 2, 3], -5)
        0
    """
    if n < 0:
        return 0
    dp = [0] * (n + 1)
    dp[0] = 1
    update_dp_table(s, dp, n)
    return dp[n]


if __name__ == "__main__":
    import doctest

    doctest.testmod()


def update_dp_table(s: List[int], dp: List[int], n: int) -> None:
    """Update the `dp` table for each coin value in `s`.

    Args:
        s (List[int]):
            The list of available denominations of points.

        dp (List[int]):
            The dynamic programming table.

        n (int):
            Target amount, the arrangements of `s` is aimed
            at adding up to `n`.
    """
    for coin_val in s:
        for j in range(coin_val, n + 1):
            dp[j] += dp[j - coin_val]
