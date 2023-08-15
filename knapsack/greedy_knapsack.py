# To get an insight into Greedy Algorithm through the Knapsack problem


"""
A shopkeeper has bags of wheat that each have different weights and different profits.
eg.
profit 5 8 7 1 12 3 4
weight 2 7 1 6  4 2 5
max_weight 100

Constraints:
max_weight > 0
profit[i] >= 0
weight[i] >= 0
Calculate the maximum profit that the shopkeeper can make given maxmum weight that can
be carried.
"""


from typing import List


def calc_profit(profit: List[int], weight: List[int], max_weight: int) -> int:
    """
    Calculate the maximum profit by carrying items with maximum profit to weight ratio.
    """
    validate_input(profit, weight, max_weight)
    return calc_max_profit(profit, weight, max_weight)


if __name__ == "__main__":
    print(
        "Input profits, weights, and then max_weight (all positive ints) separated by "
        "spaces."
    )

    profit = [int(x) for x in input("Input profits separated by spaces: ").split()]
    weight = [int(x) for x in input("Input weights separated by spaces: ").split()]
    max_weight = int(input("Max weight allowed: "))

    # Function Call
    calc_profit(profit, weight, max_weight)

def validate_input(profit: List[int], weight: List[int], max_weight: int) -> None:
    """
    Validate the input parameters.
    """
    if len(profit) != len(weight):
        raise ValueError("The length of profit and weight must be the same.")
    if max_weight <= 0:
        raise ValueError("Max weight must be greater than zero.")
    if any(p < 0 for p in profit):
        raise ValueError("Profit must not contain a negative value.")
    if any(w < 0 for w in weight):
        raise ValueError("Weight must not contain a negative value.")


def calc_max_profit(profit: List[int], weight: List[int], max_weight: int) -> int:
    """
    Calculate the maximum profit based on the profit to weight ratio.
    """
    profit_by_weight = [p / w for p, w in zip(profit, weight)]
    current_weight = 0
    current_profit = 0
    while current_weight < max_weight and profit_by_weight:
        max_index = profit_by_weight.index(max(profit_by_weight))
        if weight[max_index] <= max_weight - current_weight:
            current_weight += weight[max_index]
            current_profit += profit[max_index]
        profit_by_weight[max_index] = -1

    return current_profit
