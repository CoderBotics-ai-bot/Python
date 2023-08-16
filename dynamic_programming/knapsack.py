"""
Given weights and values of n items, put these items in a knapsack of
capacity W to get the maximum total value in the knapsack.

Note that only the integer weights 0-1 knapsack problem is solvable
using dynamic programming.
"""


def mf_knapsack(i, wt, val, j):
    """
    This code involves the concept of memory functions. Here we solve the subproblems
    which are needed unlike the below example
    F is a 2D array with -1s filled up
    """
    global f  # a global dp table for knapsack
    if f[i][j] < 0:
        if j < wt[i - 1]:
            val = mf_knapsack(i - 1, wt, val, j)
        else:
            val = max(
                mf_knapsack(i - 1, wt, val, j),
                mf_knapsack(i - 1, wt, val, j - wt[i - 1]) + val[i - 1],
            )
        f[i][j] = val
    return f[i][j]


def knapsack(w, wt, val, n):
    dp = [[0] * (w + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w_ in range(1, w + 1):
            if wt[i - 1] <= w_:
                dp[i][w_] = max(val[i - 1] + dp[i - 1][w_ - wt[i - 1]], dp[i - 1][w_])
            else:
                dp[i][w_] = dp[i - 1][w_]

    return dp[n][w_], dp

def knapsack_with_example_solution(w: int, wt: list, val: list) -> Tuple[int, Set[int]]:
    """
    Solves the integer weights knapsack problem and returns one of the
    optimal subsets along with its total value.

    The knapsack problem is a problem in combinatorial optimization: Given a set of items,
    each with a weight and a value, determine the number of each item to include in a collection
    so that the total weight is less than or equal to a given limit and the total value is as large as possible.

    Parameters
    ----------
    w : int
        The total capacity of the knapsack i.e maximum weight that knapsack can hold.

    wt : list
        The list of weights for all items. wt[i] is the weight of the i-th item.

    val : list
        The list of values for all items. val[i] is the value of the i-th item.

    Returns
    -------
    Tuple[int, Set[int]]
        Returns a tuple where the first element is the optimal value for the given knapsack problem
        and the second element is a set of indices of one of the optimal subsets which gave rise to the optimal value.

    Raises
    ------
    ValueError
      If the number of weights is not equal to the number of values.
      If both the weights and values vectors are not either lists or tuples.

    TypeError
      If any weight in the list of weights is not an integer.

    Examples
    --------
    >>> knapsack_with_example_solution(10, [1, 3, 5, 2], [10, 20, 100, 22])
    (142, {2, 3, 4})
    >>> knapsack_with_example_solution(6, [4, 3, 2, 3], [3, 2, 4, 4])
    (8, {3, 4})
    """


def _construct_solution(dp: list, wt: list, i: int, j: int, optimal_set: set):
    """
    Recursively reconstructs one of the optimal subsets given
    a filled DP table and the vector of weights

    Parameters
    ---------

    dp: list of list, the table of a solved integer weight dynamic programming problem

    wt: list or tuple, the vector of weights of the items
    i: int, the index of the item under consideration
    j: int, the current possible maximum weight
    optimal_set: set, the optimal subset so far. This gets modified by the function.

    Returns
    -------
    None

    """
    # for the current item i at a maximum weight j to be part of an optimal subset,
    # the optimal value at (i, j) must be greater than the optimal value at (i-1, j).
    # where i - 1 means considering only the previous items at the given maximum weight
    if i > 0 and j > 0:
        if dp[i - 1][j] == dp[i][j]:
            _construct_solution(dp, wt, i - 1, j, optimal_set)
        else:
            optimal_set.add(i)
            _construct_solution(dp, wt, i - 1, j - wt[i - 1], optimal_set)


if __name__ == "__main__":
    """
    Adding test case for knapsack
    """
    val = [3, 2, 4, 4]
    wt = [4, 3, 2, 3]
    n = 4
    w = 6
    f = [[0] * (w + 1)] + [[0] + [-1] * (w + 1) for _ in range(n + 1)]
    optimal_solution, _ = knapsack(w, wt, val, n)
    print(optimal_solution)
    print(mf_knapsack(n, wt, val, w))  # switched the n and w

    # testing the dynamic programming problem with example
    # the optimal subset for the above example are items 3 and 4
    optimal_solution, optimal_subset = knapsack_with_example_solution(w, wt, val)
    assert optimal_solution == 8
    assert optimal_subset == {3, 4}
    print("optimal_value = ", optimal_solution)
    print("An optimal subset corresponding to the optimal value", optimal_subset)
