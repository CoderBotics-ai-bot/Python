from other.nested_brackets import *
import pytest


def test_is_balanced_no_errors():
    """Check if the function runs without errors"""
    s = "([])"
    result = is_balanced(s)
    assert result is not None


def test_is_balanced_balanced_string():
    """Check for a balanced string"""
    s = "([])"
    assert is_balanced(s) == True


def test_is_balanced_unbalanced_string():
    """Check for an unbalanced string"""
    s = "([{)"
    assert is_balanced(s) == False


def test_is_balanced_empty_string():
    """Check for an empty string"""
    s = ""
    assert is_balanced(s) == True


def test_is_balanced_string_with_no_brackets():
    """Check for a string with no brackets"""
    s = "abcdefg"
    assert is_balanced(s) == True
