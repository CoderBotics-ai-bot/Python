from dynamic_programming.optimal_binary_search_tree import *

import pytest
from typing import List


def test_print_binary_search_tree_no_error():
    # Initialize mock data
    key = [3, 8, 9, 10, 17, 21]
    root = [
        [0, 1, 1, 1, 1, 1],
        [0, 1, 1, 1, 1, 3],
        [0, 0, 2, 3, 3, 3],
        [0, 0, 0, 3, 3, 3],
        [0, 0, 0, 0, 4, 5],
        [0, 0, 0, 0, 0, 5],
    ]

    # Function execution
    result = print_binary_search_tree(root, key, 0, 5, -1, False)
    # Check if the function runs successfully
    assert result is None


def test_print_binary_search_tree_empty_input_no_error():
    root = []
    key = []

    result = print_binary_search_tree(root, key, 0, 0, -1, False)
    # Check if the function runs successfully
    assert result is None


def test_print_binary_search_tree_invalid_input_no_error():
    # Initialize mock data
    key = [8, 10, 1, 3, 7, 6]
    root = [
        [1, 2, 3, 4, 5, 6],
        [7, 8, 9, 10, 11, 12],
        [13, 14, 15, 16, 17, 18],
        [19, 20, 21, 22, 23, 24],
        [25, 26, 27, 28, 29, 30],
        [31, 32, 33, 34, 35, 36],
    ]

    result = print_binary_search_tree(root, key, 6, 0, 10, False)
    assert result is None


def test_print_binary_search_tree_negative_input_no_error():
    # Initialize mock data
    key = [-8, -10, -1, -3, -7, -6]
    root = [
        [1, 2, 3, 4, 5, 6],
        [7, 8, 9, 10, 11, 12],
        [13, 14, 15, 16, 17, 18],
        [19, 20, 21, 22, 23, 24],
        [25, 26, 27, 28, 29, 30],
        [31, 32, 33, 34, 35, 36],
    ]

    result = print_binary_search_tree(root, key, 6, 0, -10, False)
    assert result is None
