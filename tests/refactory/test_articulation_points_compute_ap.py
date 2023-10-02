from graphs.articulation_points import *

import pytest
import pytest


from unittest.mock import patch


def test_compute_ap_no_errors():
    # Test with a simple graph in a list format
    graph = [[0, 2], [1, 2], [0, 1, 3], [2, 4, 5, 7], [3, 6], [3], [4, 7], [3, 6]]
    with patch("builtins.print") as mocked_print:
        ret_val = None
        try:
            compute_ap(graph)
        except Exception as e:
            pytest.fail(f"compute_ap() raised an exception: {e}")
    mocked_print.assert_called()


def test_compute_ap_empty():
    # Test with an empty list
    graph = []
    # Assert function doesn't fail with the empty input
    ret_val = None
    with patch("builtins.print") as mocked_print:
        try:
            compute_ap(graph)
        except Exception as e:
            pytest.fail(f"compute_ap() raised an exception: {e}")
    mocked_print.assert_not_called()
