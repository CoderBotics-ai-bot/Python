import os
import tempfile

import pytest
from searches.tabu_search import *


def test_generate_first_solution_no_error(dict_of_neighbours_fixture):
    # prepare test file
    with tempfile.NamedTemporaryFile(delete=False) as temp:
        temp.write(b"a")
        filepath = temp.name

    try:
        # run function
        result = generate_first_solution(filepath, dict_of_neighbours_fixture)
        # check if function runs without error and returns a result
        assert result is not None
    finally:
        # clean up test file
        os.remove(filepath)


def test_generate_first_solution_empty_file(dict_of_neighbours_fixture):
    # prepare empty test file
    with tempfile.NamedTemporaryFile(delete=False) as temp:
        filepath = temp.name

    try:
        with pytest.raises(Exception):
            result = generate_first_solution(filepath, dict_of_neighbours_fixture)
    finally:
        # clean up test file
        os.remove(filepath)


def test_generate_first_solution_single_line(dict_of_neighbours_fixture):
    # prepare test file with single line
    with tempfile.NamedTemporaryFile(delete=False) as temp:
        temp.write(b"a")
        filepath = temp.name

    try:
        # run function
        result = generate_first_solution(filepath, dict_of_neighbours_fixture)
        # check if function runs without error and returns an expected result
        assert result is not None
    finally:
        # clean up test file
        os.remove(filepath)


@pytest.fixture
def dict_of_neighbours_fixture():
    return {
        "a": [["b", "3"], ["c", "1"]],
        "b": [["a", "3"], ["c", "2"]],
        "c": [["a", "1"], ["b", "2"]],
    }
