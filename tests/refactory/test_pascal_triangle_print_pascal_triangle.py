
import pytest
from matrix.pascal_triangle import *
from io import StringIO


import sys
from typing import List


def test_print_pascal_triangle() -> None:
    old_stdout = sys.stdout
    sys.stdout = StringIO()

    print_pascal_triangle(3)

    output_str = sys.stdout.getvalue()
    sys.stdout = old_stdout
    assert output_str is not None


def test_print_pascal_triangle_large_number() -> None:
    old_stdout = sys.stdout
    sys.stdout = StringIO()

    print_pascal_triangle(1000)

    output_str = sys.stdout.getvalue()
    sys.stdout = old_stdout
    assert output_str is not None


@pytest.mark.parametrize("num_rows", [-1, -2, -10])
def test_print_pascal_triangle_negative(num_rows: int) -> None:
    old_stdout = sys.stdout
    sys.stdout = StringIO()

    with pytest.raises(ValueError):
        print_pascal_triangle(num_rows)

    output_str = sys.stdout.getvalue()
    sys.stdout = old_stdout
    assert output_str == ""
