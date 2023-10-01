#
#
#from typing import List
#from dynamic_programming.knapsack import *
#import pytest
#
#
#def test_construct_solution_base_case():
#    """Tests the base case where there are no items or weight"""
#    optimal_set: set = set()
#    dp: List[List[int]] = [[0]]
#    wt: List[int] = [0]
#    i: int = 0
#    j: int = 0
#    _construct_solution(dp, wt, i, j, optimal_set)
#    assert not optimal_set  # optimal_set should remain empty
#
#
#def test_construct_solution_normal_case():
#    """Tests a normal case where items can be included in the optimal subset"""
#    optimal_set: set = set()
#    dp: List[List[int]] = [[0, 0, 0], [0, 1, 1], [0, 1, 2]]
#    wt: List[int] = [1, 2]
#    i: int = 2
#    j: int = 2
#    _construct_solution(dp, wt, i, j, optimal_set)
#    assert optimal_set == {2}  # second item should be included
#
#
#def test_construct_solution_multiple_choices():
#    """Tests case where there are multiple combinations that lead to an optimal subset"""
#    optimal_set: set = set()
#    dp: List[List[int]] = [[0, 0, 0, 0], [0, 1, 1, 1], [0, 1, 2, 2], [0, 1, 2, 3]]
#    wt: List[int] = [1, 2, 3]
#    i: int = 3
#    j: int = 3
#    _construct_solution(dp, wt, i, j, optimal_set)
#    assert (
#        2 <= len(optimal_set) <= 3
#    )  # either item 2 and 3 or items 1, 2, and 3 should be included
#
#
#def test_construct_solution_zero_weight():
#    """Tests the case where the max weight is 0"""
#    optimal_set: set = set()
#    dp: List[List[int]] = [[0, 0, 0], [0, 1, 1], [0, 1, 2]]
#    wt: List[int] = [1, 2]
#    i: int = 2
#    j: int = 0
#    _construct_solution(dp, wt, i, j, optimal_set)
#    assert not optimal_set  # there is no weight, so no items should be included
#