
import numpy as np
import pytest
from typing import Dict, List, Tuple
from graphs.multi_heuristic_astar import *
import sys


def test_do_something_no_exception():
    """
    This test checks if the function do_something is executed without any exception
    """
    back_pointer = {
        (2, 3): (1, 3),
        (1, 3): (0, 3),
        (0, 3): (0, 2),
        (0, 2): (0, 1),
        (0, 1): (0, 0),
    }
    goal = (2, 3)
    start = (0, 0)
    try:
        do_something(back_pointer, goal, start)
    except SystemExit:
        pass


def test_do_something_with_empty_back_pointer():
    """
    This test checks if the function do_something handles the case when the back_pointer is empty
    """
    back_pointer = {}
    goal = (2, 3)
    start = (0, 0)

    with pytest.raises(KeyError):
        do_something(back_pointer, goal, start)
