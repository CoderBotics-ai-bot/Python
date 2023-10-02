from typing import List, Union
from backtracking.all_permutations import *

import pytest


def test_create_state_space_tree_does_not_throw():
    sequence = [1, 2, "a"]
    current_sequence = []
    index = 0
    index_used = [0, 0, 0]

    create_state_space_tree(sequence, current_sequence, index, index_used)


def test_create_state_space_tree_with_empty_sequence():
    sequence = []
    current_sequence = []
    index = 0
    index_used = []

    create_state_space_tree(sequence, current_sequence, index, index_used)


def test_create_state_space_tree_with_single_element():
    sequence = [1]
    current_sequence = []
    index = 0
    index_used = [0]

    create_state_space_tree(sequence, current_sequence, index, index_used)
