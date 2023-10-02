from searches.simulated_annealing import *

import pytest
import math
from typing import Any


class SearchProblemMock:
    def __init__(
        self, score: float, x: float, y: float, neighbors: "SearchProblemMock" = None
    ):
        self._score = score
        self.x = x
        self.y = y
        self.neighbors = neighbors if neighbors else []

    def score(self):
        return self._score

    def get_neighbors(self):
        return self.neighbors


@pytest.fixture
def mock_search_problem() -> SearchProblemMock:
    neighbors = [
        SearchProblemMock(50, 5, 5),
        SearchProblemMock(60, 6, 6),
        SearchProblemMock(70, 7, 7),
    ]
    search_problem = SearchProblemMock(40, 2, 2, neighbors)
    return search_problem


def test_simulated_annealing_no_error(mock_search_problem):
    result = simulated_annealing(mock_search_problem)
    assert result is not None


def test_simulated_annealing_score_increase(mock_search_problem):
    result = simulated_annealing(mock_search_problem)
    assert result.score() >= mock_search_problem.score()


def test_simulated_annealing_bounds(mock_search_problem):
    result = simulated_annealing(mock_search_problem, max_x=3, max_y=3)
    assert result.x <= 3
    assert result.y <= 3
