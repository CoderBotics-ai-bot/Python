from typing import Dict, List, Tuple

import pytest
from searches.tabu_search import *


def test_tabu_search_no_error():
    first_solution: List[str] = ["A", "B", "C", "D", "E", "A"]
    distance_of_first_solution: int = 10
    dict_of_neighbours: Dict[str, List[List[Union[str, int]]]] = {
        "A": [["B", 1], ["C", 2], ["D", 3], ["E", 4]],
        "B": [["A", 1], ["C", 1], ["D", 2], ["E", 3]],
        "C": [["A", 2], ["B", 1], ["D", 1], ["E", 2]],
        "D": [["A", 3], ["B", 2], ["C", 1], ["E", 1]],
        "E": [["A", 4], ["B", 3], ["C", 2], ["D", 1]],
    }
    iters: int = 10
    size: int = 5
    result = tabu_search(
        first_solution, distance_of_first_solution, dict_of_neighbours, iters, size
    )
    assert result is not None, "Test failed, Expected result not to be None"


def test_tabu_search_single_iteration():
    first_solution: List[str] = ["A", "B", "C", "D", "E", "A"]
    distance_of_first_solution: int = 10
    dict_of_neighbours: Dict[str, List[List[Union[str, int]]]] = {
        "A": [["B", 1], ["C", 2], ["D", 3], ["E", 4]],
        "B": [["A", 1], ["C", 1], ["D", 2], ["E", 3]],
        "C": [["A", 2], ["B", 1], ["D", 1], ["E", 2]],
        "D": [["A", 3], ["B", 2], ["C", 1], ["E", 1]],
        "E": [["A", 4], ["B", 3], ["C", 2], ["D", 1]],
    }
    iters: int = 1
    size: int = 5
    result = tabu_search(
        first_solution, distance_of_first_solution, dict_of_neighbours, iters, size
    )
    assert result is not None, "Test failed, Expected result not to be None"


def test_tabu_search_small_tabu_list():
    first_solution: List[str] = ["A", "B", "C", "D", "E", "A"]
    distance_of_first_solution: int = 10
    dict_of_neighbours: Dict[str, List[List[Union[str, int]]]] = {
        "A": [["B", 1], ["C", 2], ["D", 3], ["E", 4]],
        "B": [["A", 1], ["C", 1], ["D", 2], ["E", 3]],
        "C": [["A", 2], ["B", 1], ["D", 1], ["E", 2]],
        "D": [["A", 3], ["B", 2], ["C", 1], ["E", 1]],
        "E": [["A", 4], ["B", 3], ["C", 2], ["D", 1]],
    }
    iters: int = 10
    size: int = 1
    result = tabu_search(
        first_solution, distance_of_first_solution, dict_of_neighbours, iters, size
    )
    assert result is not None, "Test failed, Expected result not to be None"
