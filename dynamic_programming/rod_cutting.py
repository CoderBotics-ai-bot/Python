"""
This module provides two implementations for the rod-cutting problem:
1. A naive recursive implementation which has an exponential runtime
2. Two dynamic programming implementations which have quadratic runtime

The rod-cutting problem is the problem of finding the maximum possible revenue
obtainable from a rod of length ``n`` given a list of prices for each integral piece
of the rod. The maximum revenue can thus be obtained by cutting the rod and selling the
pieces separately or not cutting it at all if the price of it is the maximum obtainable.

"""


from typing import List
import operator


def naive_cut_rod_recursive(n: int, prices: list):
    """
    Solves the rod-cutting problem via naively without using the benefit of dynamic
    programming. The results is the same sub-problems are solved several times
    leading to an exponential runtime

    Runtime: O(2^n)

    Arguments
    -------
    n: int, the length of the rod
    prices: list, the prices for each piece of rod. ``p[i-i]`` is the
    price for a rod of length ``i``

    Returns
    -------
    The maximum revenue obtainable for a rod of length n given the list of prices
    for each piece.

    Examples
    --------
    >>> naive_cut_rod_recursive(4, [1, 5, 8, 9])
    10
    >>> naive_cut_rod_recursive(10, [1, 5, 8, 9, 10, 17, 17, 20, 24, 30])
    30
    """

    _enforce_args(n, prices)
    if n == 0:
        return 0
    max_revue = float("-inf")
    for i in range(1, n + 1):
        max_revue = max(
            max_revue, prices[i - 1] + naive_cut_rod_recursive(n - i, prices)
        )

    return max_revue


def top_down_cut_rod(n: int, prices: list):
    """
    Constructs a top-down dynamic programming solution for the rod-cutting
    problem via memoization. This function serves as a wrapper for
    _top_down_cut_rod_recursive

    Runtime: O(n^2)

    Arguments
    --------
    n: int, the length of the rod
    prices: list, the prices for each piece of rod. ``p[i-i]`` is the
    price for a rod of length ``i``

    Note
    ----
    For convenience and because Python's lists using 0-indexing, length(max_rev) =
    n + 1, to accommodate for the revenue obtainable from a rod of length 0.

    Returns
    -------
    The maximum revenue obtainable for a rod of length n given the list of prices
    for each piece.

    Examples
    -------
    >>> top_down_cut_rod(4, [1, 5, 8, 9])
    10
    >>> top_down_cut_rod(10, [1, 5, 8, 9, 10, 17, 17, 20, 24, 30])
    30
    """
    _enforce_args(n, prices)
    max_rev = [float("-inf") for _ in range(n + 1)]
    return _top_down_cut_rod_recursive(n, prices, max_rev)


def _top_down_cut_rod_recursive(n: int, prices: List[int], max_rev: List[int]) -> int:
    """
    Construct and implement a top-down recursive approach for the rod-cutting problem using dynamic programming and memoization.

    The function takes in the total length of the rod (n), a list of prices for the rods of different lengths (prices) and
    a list to store the maximum revenue calculated for each rod length (max_rev).
    It calculates the maximum revenue possible by cutting the rod into different lengths and considering the various prices for each length.

    Arguments:
    n : int - The total length of the rod.
    prices : List[int] - A list where the element at index i represents the price of the rod of length i + 1.
    max_rev : List[int] - A list where the element at index i represents the maximum revenue which could be gathered for the rod of length i.

    Returns:
    int - The maximum revenue which can be gathered by cutting and selling the rod of length 'n'.

    Example:
    _top_down_cut_rod_recursive(5, [1, 5, 8, 9, 10], [0, 0, 0, 0, 0, 0]) --> 13
    """
    if max_rev[n] >= 0:
        return max_rev[n]
    elif n == 0:
        return 0
    else:
        max_rev[n] = _calculate_max_revenue(n, prices, max_rev)

    return max_rev[n]



def bottom_up_cut_rod(n: int, prices: List[int]) -> int:
    """
    Constructs a bottom-up dynamic programming solution for the rod-cutting problem

    Arguments:
    n: int, the maximum length of the rod.
    prices: list, the prices for each piece of rod. ``p[i-i]`` is the
    price for a rod of length ``i``

    Returns:
    The maximum revenue obtainable from cutting a rod of length n given
    the prices for each piece of rod.
    """
    _enforce_args(n, prices)
    max_rev = _init_max_rev(n)
    _calculate_max_revenue(n, prices, max_rev)
    return max_rev[n]



def _calculate_max_revenue(n: int, prices: List[int], max_rev: List[int]) -> int:
    """Helper function to calculate maximum revenue."""
    max_revenue = float("-inf")
    for i in range(1, n + 1):
        max_revenue = max(
            max_revenue,
            prices[i - 1] + _top_down_cut_rod_recursive(n - i, prices, max_rev),
        )
    return max_revenue


def _init_max_rev(n: int) -> List[int]:
    return [0] + [float("-inf") for _ in range(n)]


def main() -> None:
    """
    Main function to initialize the parameters, validate_max_revenues and check calculated revenue against expected
    revenue.
    As this is the main function, no parameters are passed and no return value is expected.
    """
    prices = [6, 10, 12, 15, 20, 23]
    n = len(prices)

    validate_max_revenues(n, prices)


def _enforce_args(n: int, prices: list):
    """
    Basic checks on the arguments to the rod-cutting algorithms

    n: int, the length of the rod
    prices: list, the price list for each piece of rod.

    Throws ValueError:

    if n is negative or there are fewer items in the price list than the length of
    the rod
    """
    if n < 0:
        msg = f"n must be greater than or equal to 0. Got n = {n}"
        raise ValueError(msg)

    if n > len(prices):
        msg = (
            "Each integral piece of rod must have a corresponding price. "
            f"Got n = {n} but length of prices = {len(prices)}"
        )
        raise ValueError(msg)

def calc_expected_max_revenue(prices: List[int]) -> int:
    """
    Calculate the expected maximum revenue from given prices. In this case, we are using the first price to represent
    the unit price and multiplying it with the total length.

    Arguments:
    prices: List[int] : list of prices corresponding to the lengths of the rod.

    Returns:
    int : Expected maximum revenue.
    """

    return prices[0] * len(prices)


def validate_max_revenues(n: int, prices: List[int]) -> None:
    """
    Check whether generated max revenues from the various approaches match expected max revenue.

    Arguments:
    n: int : length of the rod to be cut.
    prices : List[int] : list of prices corresponding to the lengths of the rod.

    Raises:
    exception: If the max revenues do not match.
    """

    expected_max_revenue = calc_expected_max_revenue(prices)

    max_rev_top_down = top_down_cut_rod(n, prices)
    max_rev_bottom_up = bottom_up_cut_rod(n, prices)
    max_rev_naive = naive_cut_rod_recursive(n, prices)

    assert (
        max_rev_top_down == max_rev_bottom_up == max_rev_naive == expected_max_revenue
    ), "Maximum revenues do not match"


if __name__ == "__main__":
    main()
