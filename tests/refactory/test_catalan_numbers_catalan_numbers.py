from dynamic_programming.catalan_numbers import *
import pytest


def test_catalan_numbers_no_errors():
    assert catalan_numbers(5) is not None


def test_catalan_numbers_negative():
    with pytest.raises(ValueError):
        catalan_numbers(-1)


def test_catalan_numbers_zero():
    assert len(catalan_numbers(0)) == 1


def test_catalan_numbers_positive():
    assert len(catalan_numbers(10)) == 11


def test_catalan_numbers_values_non_negative():
    assert all(i >= 0 for i in catalan_numbers(10))
