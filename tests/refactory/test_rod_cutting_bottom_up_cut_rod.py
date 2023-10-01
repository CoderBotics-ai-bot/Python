import pytest
from dynamic_programming.rod_cutting import *


def test_bottom_up_cut_rod():
    # Test to check if function is syntactically correct and all imported libraries work as expected
    assert bottom_up_cut_rod(4, [1, 5, 8, 9]) is not None


def test_bottom_up_cut_rod_zero_length():
    # Test to check that 0 length rod returns 0 revenue
    assert bottom_up_cut_rod(0, [1, 5, 8, 9]) == 0


def test_bottom_up_cut_rod_negative_length():
    # Test to check that negative length rod raises an error
    with pytest.raises(ValueError):
        bottom_up_cut_rod(-4, [1, 5, 8, 9])


def test_bottom_up_cut_rod_price_list_greater_than_length():
    # Test to check that the function handles the case when price list is longer than rod length
    assert bottom_up_cut_rod(4, [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]) is not None


def test_bottom_up_cut_rod_price_list_empty():
    # Test to check that the function handles the case when price list is empty
    with pytest.raises(ValueError):
        bottom_up_cut_rod(4, [])
