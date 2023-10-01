from typing import Any, List, Tuple, Union

import pytest
from collections.abc import Iterable
from other.davisb_putnamb_logemannb_loveland import *


@pytest.fixture
def generate_sample_input() -> Tuple[Any]:
    model = {"A1": True, "A2": False, "A3": None, "A4": True, "A5": False}
    clauses = [Clause(["A1", "A2'", "A3"]), Clause(["A5'", "A2'", "A1"])]
    symbols = ["A1", "A2", "A3", "A4", "A5"]
    return clauses, symbols, model


def test_find_pure_symbols_does_not_throw(generate_sample_input: Tuple) -> None:
    clauses, symbols, model = generate_sample_input
    try:
        find_pure_symbols(clauses, symbols, model)
    except Exception as error:
        pytest.fail(f"find_pure_symbols() raised an exception: {str(error)}")


def test_find_pure_symbols_return_is_not_none(generate_sample_input: Tuple) -> None:
    clauses, symbols, model = generate_sample_input
    result = find_pure_symbols(clauses, symbols, model)
    assert result is not None, "find_pure_symbols() returned None"


def test_find_pure_symbols_correct_return_structure(
    generate_sample_input: Tuple,
) -> None:
    clauses, symbols, model = generate_sample_input
    result = find_pure_symbols(clauses, symbols, model)
    assert isinstance(result, tuple), "find_pure_symbols() should return a tuple"
    assert len(result) == 2, "find_pure_symbols() tuple should have two elements"
    pure_symbols, assignment = result
    assert isinstance(pure_symbols, list), "First element of the tuple should be a list"
    assert isinstance(assignment, dict), "Second element of the tuple should be a dict"


def test_find_pure_symbols_correct_return_types(generate_sample_input: Tuple) -> None:
    clauses, symbols, model = generate_sample_input
    result = find_pure_symbols(clauses, symbols, model)
    pure_symbols, assignment = result
    assert all(
        [isinstance(symbol, str) for symbol in pure_symbols]
    ), "All symbols should be strings"
    assert all(
        [
            isinstance(key, str) and isinstance(value, (bool, type(None)))
            for key, value in assignment.items()
        ]
    ), "All keys should be string and values should be bool or None"
