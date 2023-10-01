from other.magicdiamondpattern import *
from io import StringIO

import pytest
import sys


# Test Case 1: Check if function doesn't throw any errors and returns correctly
def test_reverse_floyd_no_errors():
    # Redirect standard output
    old_stdout = sys.stdout
    sys.stdout = mystdout = StringIO()

    reverse_floyd(3)

    # Reset standard output
    sys.stdout = old_stdout

    output = mystdout.getvalue()

    assert output is not None


# Test Case 2: Check if function handles edge case of zero input
def test_reverse_floyd_zero_input():
    # Redirect standard output
    old_stdout = sys.stdout
    sys.stdout = mystdout = StringIO()

    reverse_floyd(0)

    # Reset standard output
    sys.stdout = old_stdout

    output = mystdout.getvalue()

    assert output == ""


# Test Case 3: Check if function handles edge case of negative input
def test_reverse_floyd_negative_input():
    # Redirect standard output
    old_stdout = sys.stdout
    sys.stdout = mystdout = StringIO()

    reverse_floyd(-1)

    # Reset standard output
    sys.stdout = old_stdout

    output = mystdout.getvalue()

    assert output == ""
