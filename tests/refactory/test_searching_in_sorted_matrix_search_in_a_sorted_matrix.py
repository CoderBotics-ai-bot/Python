from matrix.searching_in_sorted_matrix import *
import pytest


def test_search_in_a_sorted_matrix_MONKEYPATCHED(monkeypatch):
    inputs = {"print": []}
    monkeypatch.setattr("builtins.print", lambda x: inputs["print"].append(x))

    search_in_a_sorted_matrix(
        [[2, 5, 7], [4, 8, 13], [9, 11, 15], [12, 17, 20]], 3, 3, 5
    )
    assert inputs["print"] == ["Key 5 found at row- 1 column- 2"]

    inputs["print"].clear()
    search_in_a_sorted_matrix(
        [[2, 5, 7], [4, 8, 13], [9, 11, 15], [12, 17, 20]], 3, 3, 21
    )
    assert inputs["print"] == ["Key 21 not found"]

    inputs["print"].clear()
    search_in_a_sorted_matrix(
        [[2.1, 5, 7], [4, 8, 13], [9, 11, 15], [12, 17, 20]], 3, 3, 2.1
    )
    assert inputs["print"] == ["Key 2.1 found at row- 1 column- 1"]

    inputs["print"].clear()
    search_in_a_sorted_matrix(
        [[2.1, 5, 7], [4, 8, 13], [9, 11, 15], [12, 17, 20]], 3, 3, 2.2
    )
    assert inputs["print"] == ["Key 2.2 not found"]


def test_search_in_a_sorted_matrix_edge_cases_MONKEYPATCHED(monkeypatch):
    inputs = {"print": []}
    monkeypatch.setattr("builtins.print", lambda x: inputs["print"].append(x))

    # Case when m or n is 0
    search_in_a_sorted_matrix([], 0, 0, 5)
    assert inputs["print"] == ["Key 5 not found"]

    # Case when matrix is 1x1
    inputs["print"].clear()
    search_in_a_sorted_matrix([[5]], 1, 1, 5)
    assert inputs["print"] == ["Key 5 found at row- 1 column- 1"]

    # Case when key is not in the matrix but is between two elements in the matrix
    inputs["print"].clear()
    search_in_a_sorted_matrix(
        [[2, 5, 7], [4, 8, 13], [9, 11, 15], [12, 17, 20]], 3, 3, 6
    )
    assert inputs["print"] == ["Key 6 not found"]

    # Case when key is not in the matrix and is less than any elements in the matrix
    inputs["print"].clear()
    search_in_a_sorted_matrix(
        [[2, 5, 7], [4, 8, 13], [9, 11, 15], [12, 17, 20]], 3, 3, 1
    )
    assert inputs["print"] == ["Key 1 not found"]

    # Case when key is not in the matrix and is greater than any elements in the matrix
    inputs["print"].clear()
    search_in_a_sorted_matrix(
        [[2, 5, 7], [4, 8, 13], [9, 11, 15], [12, 17, 20]], 3, 3, 21
    )
    assert inputs["print"] == ["Key 21 not found"]
