from other.scoring_algorithm import *
import pytest


import pytest


def test_get_data_no_errors():
    """Test if the function executes without throwing any errors"""
    assert get_data([[20, 60, 2012], [23, 90, 2015], [22, 50, 2011]]) is not None


def test_get_data_output_type():
    """Test if the function returns output of correct type"""
    output = get_data([[20, 60, 2012], [23, 90, 2015], [22, 50, 2011]])
    assert isinstance(output, list)
    for sublist in output:
        assert isinstance(sublist, list)
        for item in sublist:
            assert isinstance(item, float)


def test_get_data_empty_list():
    """Test how the function handles input that is an empty list"""
    assert get_data([]) == []


def test_get_data_contents_of_output():
    """Test if the contents of the output list are correct"""
    result = get_data([[1.0, 2.0], [3.0, 4.0]])
    assert result == [[1.0, 3.0], [2.0, 4.0]]


def test_get_data_with_non_numbers_in_input():
    """Test how the function handles input lists with non-number elements"""
    with pytest.raises(ValueError):
        get_data([["string1", "string2"], ["string3", "string4"]])
