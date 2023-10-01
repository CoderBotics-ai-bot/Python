#import pytest
#from dynamic_programming.viterbi import *
#
#
#def test__validate_list_no_errors():
#    """
#    Test _validate_list function to ensure no errors are thrown with proper input
#    """
#    try:
#        _validate_list(["a"], "mock_name")
#    except:
#        pytest.fail("_validate_list threw an error despite receiving valid input")
#
#
#def test__validate_list_non_list_input():
#    """
#    Test _validate_list function to ensure it raises an error with non-list input
#    """
#    with pytest.raises(ValueError) as excinfo:
#        _validate_list("invalid input", "mock_name")
#
#    assert "mock_name must be a list" in str(excinfo.value)
#
#
#def test__validate_list_non_string_list_elements():
#    """
#    Test _validate_list function to ensure it raises an error when list elements are not strings
#    """
#    with pytest.raises(ValueError) as excinfo:
#        _validate_list([1, 2, 3], "mock_name")
#
#    assert "mock_name must be a list of strings" in str(excinfo.value)
#
#
#def test__validate_list_none_input():
#    """
#    Test _validate_list function to ensure it raises an error when input is None
#    """
#    with pytest.raises(ValueError) as excinfo:
#        _validate_list(None, "mock_name")
#
#    assert "mock_name must be a list" in str(excinfo.value)
#