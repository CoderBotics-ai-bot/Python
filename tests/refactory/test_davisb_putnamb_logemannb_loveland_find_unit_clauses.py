import pytest
from other.davisb_putnamb_logemannb_loveland import *


def test_find_unit_clauses_no_errors():
    clause1 = Clause(["A4", "A3", "A5'", "A1", "A3'"])
    clause2 = Clause(["A4"])
    clause3 = Clause(["A3"])
    clauses, symbols = generate_parameters(Formula([clause1, clause2, clause3]))
    try:
        find_unit_clauses(clauses, {})
    except Exception as e:
        pytest.fail(f"find_unit_clauses() raised {type(e).__name__} unexpectedly!")


def test_find_unit_clauses_return_is_not_none():
    clause1 = Clause(["A4", "A3", "A5'", "A1", "A3'"])
    clause2 = Clause(["A4"])
    clause3 = Clause(["A3"])
    clauses, symbols = generate_parameters(Formula([clause1, clause2, clause3]))
    assert (
        find_unit_clauses(clauses, {}) is not None
    ), "find_unit_clauses() returned None!"


def test_find_unit_clauses_return_type():
    clause1 = Clause(["A4", "A3", "A5'", "A1", "A3'"])
    clause2 = Clause(["A4"])
    clause3 = Clause(["A3"])
    clauses, symbols = generate_parameters(Formula([clause1, clause2, clause3]))
    unit_symbols, assignment = find_unit_clauses(clauses, {})
    assert isinstance(unit_symbols, list), "Expected list, but got %s." % type(
        unit_symbols
    )
    assert isinstance(assignment, dict), "Expected dict, but got %s." % type(assignment)


def test_find_unit_clauses_empty_input():
    assert find_unit_clauses([], {}) == (
        [],
        {},
    ), "Empty input should return empty list and dict"
