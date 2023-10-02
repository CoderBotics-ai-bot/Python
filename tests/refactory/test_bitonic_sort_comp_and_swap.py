from sorts.bitonic_sort import *
import pytest


def test_comp_and_swap_no_exceptions():
    array = [1, 2, 3]
    try:
        comp_and_swap(array, 1, 2, 1)
    except Exception:
        pytest.fail("comp_and_swap() raised Exception unexpectedly!")


def test_comp_and_swap_not_none():
    array = [1, 2, 3]
    result = comp_and_swap(array, 1, 2, 1)
    assert result is None, "comp_and_swap() should not return anything."


def test_comp_and_swap_ascendingsort():
    array = [3, 2, 1]
    comp_and_swap(array, 0, 2, 1)
    assert array == [1, 2, 3]


def test_comp_and_swap_descendingsort():
    array = [1, 2, 3]
    comp_and_swap(array, 0, 2, 0)
    assert array == [3, 2, 1]


def test_comp_and_swap_edgcase_same_elements():
    array = [2, 2, 2]
    comp_and_swap(array, 0, 2, 1)
    assert array == [2, 2, 2], "Function failed with array with identical elements."
