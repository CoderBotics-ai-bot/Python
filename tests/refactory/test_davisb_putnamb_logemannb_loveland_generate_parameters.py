from other.davisb_putnamb_logemannb_loveland import Clause, Formula
import pytest
from other.davisb_putnamb_logemannb_loveland import *


@pytest.fixture
def sample_formula():
    return Formula([Clause(["A1", "A2'", "A3"]), Clause(["A5'", "A2'", "A1"])])


def test_generate_parameters_no_errors(sample_formula):
    try:
        generate_parameters(sample_formula)
    except Exception as e:
        pytest.fail(f"generate_parameters function raised exception {e}")


def test_generate_parameters_not_none(sample_formula):
    response = generate_parameters(sample_formula)
    assert (
        response is not None
    ), "The function must return a value, but it returned None"


def test_generate_parameters_output_type(sample_formula):
    response = generate_parameters(sample_formula)
    assert isinstance(
        response, tuple
    ), "The output type is incorrect. It should be a tuple."
    assert len(response) == 2, "The output tuple's size is not correct. It should be 2."

    clauses, symbols = response

    assert isinstance(clauses, list), "Returned clauses should be of type list"
    assert isinstance(symbols, list), "Returned symbols should be of type list"

    for clause in clauses:
        assert isinstance(
            clause, Clause
        ), "Elements in the clauses list should be of Clause type"

    for symbol in symbols:
        assert isinstance(
            symbol, str
        ), "Elements in the symbols list should be of str type"


def test_generate_parameters_no_duplicates_and_size(sample_formula):
    _, symbols = generate_parameters(sample_formula)
    assert len(symbols) == len(
        set(symbols)
    ), "The symbols list should not contain duplicates"
    assert (
        len(symbols) == 4
    ), "The size of the symbols list is incorrect. It should be 4."


def test_generate_parameters_symbol_names(sample_formula):
    _, symbols = generate_parameters(sample_formula)
    assert (
        symbols.sort() == ["A1", "A2", "A3", "A5"].sort()
    ), "The names of the symbols are not correct."
