#import math
#from unittest.mock import Mock
#
#
#import math
#
#import pytest
#from searches.hill_climbing import *
#from typing import List
#
#
#def get_mock_search_problem(x: float, y: float, score: float) -> SearchProblem:
#    search_prob = SearchProblem(x=x, y=y, function_to_optimize=Mock(return_value=1))
#    search_prob.score = Mock(return_value=score)
#    return search_prob
#
#
#@pytest.fixture
#def mock_search_problem() -> SearchProblem:
#    return get_mock_search_problem(x=0, y=0, score=1)
#
#
#def test_hill_climbing_does_not_throw(mock_search_problem: SearchProblem):
#    mock_search_problem.get_neighbors = Mock(return_value=[])
#    assert hill_climbing(mock_search_problem) is not None
#
#
#def test_hill_climbing_with_neighbors(mock_search_problem: SearchProblem):
#    neighbor1 = get_mock_search_problem(x=0, y=1, score=2)
#    neighbor2 = get_mock_search_problem(x=1, y=0, score=3)
#
#    mock_search_problem.get_neighbors = Mock(return_value=[neighbor1, neighbor2])
#
#    result = hill_climbing(mock_search_problem)
#    assert result.score() == 3
#
#
#def test_hill_climbing_with_boundaries(mock_search_problem: SearchProblem):
#    neighbor1 = get_mock_search_problem(x=-1, y=-1, score=2)
#    neighbor2 = get_mock_search_problem(x=1, y=1, score=3)
#
#    mock_search_problem.get_neighbors = Mock(return_value=[neighbor1, neighbor2])
#
#    result = hill_climbing(
#        mock_search_problem, min_x=-0.5, max_x=0.5, min_y=-0.5, max_y=0.5
#    )
#    assert result.score() == 1
#
#
#def test_hill_climbing_with_max_iterations(mock_search_problem: SearchProblem):
#    neighbor1 = get_mock_search_problem(x=0, y=1, score=2)
#    neighbor2 = get_mock_search_problem(x=1, y=0, score=3)
#
#    mock_search_problem.get_neighbors = Mock(return_value=[neighbor1, neighbor2])
#
#    result = hill_climbing(mock_search_problem, max_iter=1)
#    assert result.score() == 1
#