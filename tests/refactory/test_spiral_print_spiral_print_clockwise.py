from unittest.mock import call, patch
from contextlib import redirect_stdout

import pytest


from contextlib import redirect_stdout
from io import StringIO
from matrix.spiral_print import *
from typing import List


@pytest.fixture
def input_data() -> List[List[int]]:
    return [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]


@pytest.fixture
def edge_case_empty_list() -> List[List[int]]:
    return []


@pytest.fixture
def edge_case_single_element() -> List[List[int]]:
    return [[1]]


def test_spiral_print_clockwise_no_error(input_data):
    with patch("builtins.print") as mocked_print:
        spiral_print_clockwise(input_data)
    assert mocked_print.called


def test_spiral_print_clockwise_edge_case_empty_list(edge_case_empty_list):
    with patch("builtins.print") as mocked_print:
        spiral_print_clockwise(edge_case_empty_list)
    mocked_print.assert_called_once_with("Not a valid matrix")


def test_spiral_print_clockwise_edge_case_single_element(edge_case_single_element):
    with patch("builtins.print") as mocked_print:
        spiral_print_clockwise(edge_case_single_element)
    mocked_print.assert_called_once_with(1)


def test_spiral_print_clockwise_output(input_data):
    with StringIO() as buf, redirect_stdout(buf):
        spiral_print_clockwise(input_data)
        output = buf.getvalue()
    expected_output = (
        "\n".join(map(str, [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7])) + "\n"
    )
    assert output == expected_output
