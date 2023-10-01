"""
Given weights and values of n items, put these items in a knapsack of
capacity W to get the maximum total value in the knapsack.

Note that only the integer weights 0-1 knapsack problem is solvable
using dynamic programming.
"""


from typing import List, Tuple


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



def knapsack(
    w: int, wt: List[int], val: List[int], n: int
) -> Tuple[int, List[List[int]]]:
    """
    Refactored knapsack 0/1 problem solver. Utilizing helper functions initialize_dp and calculate_dp.
    """

    dp = initialize_dp(w, n)

    return calculate_dp(dp, wt, val, w, n)

def knapsack_with_example_solution(
    w: int, wt: List[int], val: List[int]
) -> Tuple[int, set]:
    """
    Solves the 0/1 Knapsack problem using dynamic programming. It also
    constructs an example set of item indices which gives the optimal solution.

    Parameters:
    - w (int): Total weight that the knapsack can carry.
    - wt (List[int]): The weights of the items.
    - val (List[int]): The values of the items.

    Returns:
    Tuple[int, set]: A tuple where the first element is the maximum value that
                     can be carried in the knapsack and the second element is
                     a set of item indices that make up this optimal solution.
    """
    validate_inputs(wt, val)
    validate_weights(wt)

    num_items = len(wt)

    optimal_val, dp_table = knapsack(w, wt, val, num_items)
    example_optional_set: set = set()

    _construct_solution(dp_table, wt, num_items, w, example_optional_set)

    return optimal_val, example_optional_set


def initialize_dp(w: int, n: int) -> List[List[int]]:
    """
    Initialize a 2D array dp of size (n+1) x (w+1) filled with zeros.
    """
    return [[0 for _ in range(w + 1)] for _ in range(n + 1)]

def _construct_solution(
    dp: List[List[int]], wt: List[int], i: int, j: int, optimal_set: set
) -> None:
    """
    Recursively reconstructs one of the optimal subsets given a filled DP table and the vector of weights.

    This function modifies the optimal_set parameter by adding item indexes to it.
    Each index in the optimal_set represents an item in the subset that contributes to the maximum subset sum.

    Parameters
    ----------
    dp : List[List[int]]
        The table of a solved integer weight dynamic programming problem.
    wt : List[int]
        The vector of weights of the items.
    i : int
        The index of the current item under consideration.
    j : int
        The current possible maximum weight.
    optimal_set : set
        The optimal subset so far. This gets modified by the function.

    Returns
    -------
    None
    """
    if i == 0 or j == 0:
        return

    previous_item = dp[i - 1][j]
    if dp[i][j] != previous_item:
        optimal_set.add(i)
        j -= wt[i - 1]

    _construct_solution(dp, wt, i - 1, j, optimal_set)


def validate_inputs(wt: List[int], val: List[int]) -> None:
    """
    Validate that the weights and values are lists or tuples and that
    they have the same number of elements.

    Parameters:
    - wt (List[int]): The weights of the items.
    - val (List[int]): The values of the items.
    """
    if not isinstance(wt, (list, tuple)) or not isinstance(val, (list, tuple)):
        raise ValueError("Weights and values must be a list or a tuple.")

    if len(wt) != len(val):
        raise ValueError(
            "The number of weights must be the same as the number of values."
        )


def validate_weights(wt: List[int]) -> None:
    """
    Validate that all weights are integers.

    Parameters:
    - wt (List[int]): The weights of the items.
    """
    for i, weight in enumerate(wt):
        if not isinstance(weight, int):
            raise TypeError(
                f"All weights must be integers but got weight of type {type(weight)} at index {i}."
            )


def calculate_dp(
    dp: List[List[int]], wt: List[int], val: List[int], w: int, n: int
) -> Tuple[int, List[List[int]]]:
    """
    Utilize dynamic programming approach to calculate the maximum value that could be put in a knapsack of capacity w.
    """
    for i in range(1, n + 1):
        for w_ in range(1, w + 1):
            if wt[i - 1] <= w_:
                dp[i][w_] = max(val[i - 1] + dp[i - 1][w_ - wt[i - 1]], dp[i - 1][w_])
            else:
                dp[i][w_] = dp[i - 1][w_]

    return dp[n][w], dp


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
