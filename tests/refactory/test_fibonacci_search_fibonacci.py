import pytest
from searches.fibonacci_search import *


import pytest


def test_fibonacci_no_error():
    assert fibonacci(5) is not None


def test_fibonacci_negative_number():
    with pytest.raises(ValueError):
        fibonacci(-1)


def test_fibonacci_not_integer():
    with pytest.raises(TypeError):
        fibonacci("a")


def test_fibonacci_zero_and_one():
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1


def test_fibonacci_cache():
    first_execution = fibonacci(15)
    second_execution = fibonacci(15)
    assert first_execution == second_execution
