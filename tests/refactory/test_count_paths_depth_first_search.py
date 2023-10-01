from matrix.count_paths import *

import pytest
from typing import List, Set, Tuple


def test_depth_first_search():
    # Test if the function runs without errors
    grid1 = [[0, 0, 0, 0], [1, 1, 0, 0], [0, 0, 0, 1], [0, 1, 0, 0]]
    grid2 = [[0, 0, 0, 0, 0], [0, 1, 1, 1, 0], [0, 1, 1, 1, 0], [0, 0, 0, 0, 0]]
    visit = set()
    assert depth_first_search(grid1, 0, 0, visit) is not None
    assert depth_first_search(grid2, 0, 0, visit) is not None


def test_no_paths():
    # Test case where there are no paths from top left to bottom right
    grid = [[1, 0, 0, 0], [1, 1, 0, 0], [1, 0, 0, 1], [1, 1, 0, 0]]
    visit = set()
    assert depth_first_search(grid, 0, 0, visit) == 0


def test_single_path():
    # Test case where there is only one path from top left to bottom right
    grid = [[0, 0, 0, 0], [1, 1, 1, 0], [1, 1, 1, 0], [0, 0, 0, 0]]
    visit = set()
    assert depth_first_search(grid, 0, 0, visit) == 1


def test_multiple_paths():
    # Test case where there are many paths from top left to bottom right
    grid = [[0, 0, 1, 0], [0, 0, 0, 0], [1, 0, 0, 1], [0, 0, 0, 0]]
    visit = set()
    assert depth_first_search(grid, 0, 0, visit) > 1
