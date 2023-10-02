from graphs.multi_heuristic_astar import *
import pytest


def test_make_common_ground_no_exception():
    """Test if make_common_ground() function is executed without any exceptions."""
    try:
        make_common_ground()
    except Exception:
        assert False, "make_common_ground() function raised an exception."


def test_make_common_ground_not_none():
    """Test if make_common_ground() function returns not None value."""
    assert (
        make_common_ground() is not None
    ), "make_common_ground() function returned None."


def test_make_common_ground_element_types():
    """Test if make_common_ground() function returns list of tuples with two integers each."""
    result = make_common_ground()
    assert all(
        isinstance(i, tuple) and len(i) == 2 and all(isinstance(j, int) for j in i)
        for i in result
    ), "make_common_ground() didn't return list of tuples with two integers each."
