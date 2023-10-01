#from dynamic_programming.viterbi import *
#
#import pytest
#from typing import Any, Type
#
#
#def test_validate_dict_does_not_throw():
#    valid_dict = {"a": 1, "b": 2}
#    try:
#        _validate_dict(valid_dict, "valid_dict", int)
#    except Exception:
#        pytest.fail("_validate_dict is throwing an exception on valid input")
#
#
#def test_validate_dict_non_dict_type():
#    invalid_value = "not_a_dict"
#    with pytest.raises(ValueError) as excinfo:
#        _validate_dict(invalid_value, "invalid_value", int)
#    assert str(excinfo.value) == "invalid_value must be a dict"
#
#
#def test_validate_dict_wrong_value_type():
#    invalid_dict = {"a": "not_an_int", "b": 2}
#    with pytest.raises(ValueError) as excinfo:
#        _validate_dict(invalid_dict, "invalid_dict", int)
#    assert str(excinfo.value) == "invalid_dict all values must be int"
#
#
#def test_validate_dict_non_string_keys():
#    invalid_dict = {1: 1, 2: 2}
#    with pytest.raises(ValueError) as excinfo:
#        _validate_dict(invalid_dict, "invalid_dict", int)
#    assert str(excinfo.value) == "invalid_dict all keys must be strings"
#
#
#def test_validate_dict_nested_dict():
#    valid_dict = {"a": {"b": 1}, "c": {"d": 2}}
#    try:
#        _validate_dict(valid_dict, "valid_dict", dict, nested=True)
#    except Exception:
#        pytest.fail("_validate_dict is throwing an exception on valid input")
#
#
#def test_validate_dict_invalid_nested_dict():
#    invalid_dict = {"a": {"b": "not_an_int"}, "c": {"d": 2}}
#    with pytest.raises(ValueError) as excinfo:
#        _validate_dict(invalid_dict, "invalid_dict", dict, nested=True)
#    assert (
#        str(excinfo.value) == "invalid_dict nested dictionary all values must be dict"
#    )
#