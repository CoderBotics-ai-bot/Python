#from sorts.msd_radix_sort import *
#import pytest
#
#
#def test__msd_radix_sort_no_errors():
#    """Test if the function throws no errors."""
#    try:
#        _msd_radix_sort([12, 34, 29, 50], 5)
#    except Exception as e:
#        pytest.fail(f"An error has occured: {str(e)}")
#
#
#def test__msd_radix_sort_not_none():
#    """Test if the function result is not None."""
#    assert _msd_radix_sort([12, 34, 29, 50], 5) is not None
#
#
#def test__msd_radix_sort_empty_list():
#    """Test how function handles empty list."""
#    assert _msd_radix_sort([], 5) == []
#
#
#def test__msd_radix_sort_single_element_list():
#    """Test how function handles single element list."""
#    assert _msd_radix_sort([15], 5) == [15]
#
#
#def test__msd_radix_sort_negative_number():
#    """Test how function handles negative integers."""
#    assert _msd_radix_sort([-15, -34, 29, 50], 5) == [-34, 50, 29, -15]
#