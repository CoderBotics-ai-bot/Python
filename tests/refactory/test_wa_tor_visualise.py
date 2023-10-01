

import io
from cellular_automata.wa_tor import *

import pytest
import io
import sys


def test_visualise_no_exception():
    """
    Test visualise function to ensure no exception is thrown
    """
    wt = WaTor(30, 30)
    wt.set_planet(
        [
            [Entity(True, coords=(0, 0)), Entity(False, coords=(0, 1)), None],
            [Entity(False, coords=(1, 0)), None, Entity(False, coords=(1, 2))],
            [None, Entity(True, coords=(2, 1)), None],
        ]
    )
    try:
        visualise(wt, 0, colour=False)
        no_exception = True
    except Exception:
        no_exception = False
    assert no_exception


def test_visualise_content():
    """
    Test visualise function to ensure the output string contains the expected char
    """
    wt = WaTor(30, 30)
    wt.set_planet(
        [
            [Entity(True, coords=(0, 0)), Entity(False, coords=(0, 1)), None],
            [Entity(False, coords=(1, 0)), None, Entity(False, coords=(1, 2))],
            [None, Entity(True, coords=(2, 1)), None],
        ]
    )
    captured_output = io.StringIO()  # without importing StringIO
    sys.stdout = captured_output
    visualise(wt, 0, colour=False)
    sys.stdout = sys.__stdout__
    assert "#" in captured_output.getvalue()
    assert "x" in captured_output.getvalue()
