

import pytest
from dynamic_programming.edit_distance import *
import pytest


def test_min_dist_bottom_up():
    edit_distance = EditDistance()

    # Test when both strings are empty
    assert edit_distance.min_dist_bottom_up("", "") == 0

    # Test when the second string is empty
    assert edit_distance.min_dist_bottom_up("abc", "") == 3

    # Test when both strings are the same
    assert edit_distance.min_dist_bottom_up("abc", "abc") == 0

    # Test when strings have some common characters but in different places
    assert edit_distance.min_dist_bottom_up("abc", "acb") == 2

    # Test when strings do not have any common characters
    assert edit_distance.min_dist_bottom_up("abc", "xyz") == 3

    # Test when one string is the reverse of the other string
    assert edit_distance.min_dist_bottom_up("abc", "cba") == 2
