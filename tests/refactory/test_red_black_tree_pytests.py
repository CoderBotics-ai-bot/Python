import pytest
from data_structures.binary_tree.red_black_tree import *


def test_pytests():
    # Execute pytests function to verify that it runs without error.
    # The individual test functions are tested separately so we don't need to mock them here.
    # If pytests function or any individual test function that it is calling has an issue, an exception will be raised.
    try:
        pytests()
    except Exception as e:
        pytest.fail(f"pytests function failed due to error {e}")
