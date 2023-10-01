#from dynamic_programming.minimum_partition import *
#import pytest
#
#
#def test_find_min_no_errors():
#    """Test that find_min runs without error with a valid list of integers"""
#    result = find_min([1, 6, 11, 5])
#    assert result is not None
#
#
#def test_find_min_single_item_list():
#    """Test that find_min returns the single item value when given a list with a single item"""
#    result = find_min([7])
#    assert result == 0
#
#
#def test_find_min_with_zero():
#    """Test that find_min deals correctly with a list containing a zero"""
#    result = find_min([0, 10, -10])
#    assert result == 0
#