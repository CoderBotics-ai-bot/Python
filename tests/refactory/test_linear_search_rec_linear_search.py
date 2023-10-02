from searches.linear_search import *
import pytest


def test_rec_linear_search_does_not_throw():
    sequence = [0, 30, 500, 100, 700]
    low = 0
    high = 4
    target = 30
    output = None

    try:
        output = rec_linear_search(sequence, low, high, target)
    except Exception:
        pytest.fail("rec_linear_search() raised Exception unexpectedly!")

    assert output is not None


def test_rec_linear_search_invalid_bounds():
    with pytest.raises(Exception):
        assert rec_linear_search([0, 30, 500, 100, 700], -1, 4, 0)


def test_rec_linear_search_found_at_first_element():
    sequence = [0, 30, 500, 100, 700]
    assert rec_linear_search(sequence, 0, len(sequence) - 1, 0) == 0


def test_rec_linear_search_found_at_last_element():
    sequence = [0, 30, 500, 100, 700]
    assert rec_linear_search(sequence, 0, len(sequence) - 1, 700) == 4


def test_rec_linear_search_element_not_found():
    sequence = [0, 30, 500, 100, 700]
    assert rec_linear_search(sequence, 0, len(sequence) - 1, 999) == -1
