import pytest
from sorts.shell_sort import *


import pytest


def test_shell_sort_no_errors():
    result = shell_sort([0, 5, 3, 2, 2])
    assert result is not None


def test_shell_sort_correct_sorting():
    result = shell_sort([0, 5, 3, 2, 2])
    assert result == [0, 2, 2, 3, 5]


def test_shell_sort_empty_input():
    result = shell_sort([])
    assert result == []


def test_shell_sort_negative_values():
    result = shell_sort([-2, -5, -45])
    assert result == [-45, -5, -2]


def test_shell_sort_single_element():
    result = shell_sort([3])
    assert result == [3]


def test_shell_sort_same_elements():
    result = shell_sort([3, 3, 3])
    assert result == [3, 3, 3]
