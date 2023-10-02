#
#import pytest
#from graphs.a_star import *
#from typing import List
#
#
## Test fixtures
#@pytest.fixture
#def grid() -> List[List[int]]:
#    return [[0, 1, 0, 0], [0, 0, 0, 0]]
#
#
#@pytest.fixture
#def init() -> List[int]:
#    return [0, 0]
#
#
#@pytest.fixture
#def goal() -> List[int]:
#    return [1, 2]
#
#
#@pytest.fixture
#def cost() -> int:
#    return 1
#
#
#@pytest.fixture
#def heuristic() -> List[List[int]]:
#    return [[1, 2, 1, 1], [1, 1, 0, 1]]
#
#
#@pytest.fixture
#def DIRECTIONS() -> List[List[int]]:
#    return [[-1, 0], [0, -1], [1, 0], [0, 1]]
#
#
## Unit tests
## Valid case, no error should happen
#def test_search_does_not_error_with_valid_input(
#    grid, init, goal, cost, heuristic, DIRECTIONS
#):
#    try:
#        result = search(grid, init, goal, cost, heuristic, DIRECTIONS)
#        assert result is not None
#    except:
#        pytest.fail("The search() function raised an error unexpectedly!")
#
#
## The heuristics and grid doesn't match due to their size, so an error should be raised
#def test_search_heuristic_and_grid_mismatch(grid, init, goal, cost, DIRECTIONS):
#    heuristic = [[0, 0, 0]]
#    with pytest.raises(IndexError):
#        search(grid, init, goal, cost, heuristic, DIRECTIONS)
#
#
## The initial position is out of grid, then error should be raised
#def test_search_initial_position_out_of_grid(grid, goal, cost, DIRECTIONS, heuristic):
#    init = [-1, 2]
#    with pytest.raises(IndexError):
#        search(grid, init, goal, cost, heuristic, DIRECTIONS)
#
#
## The goal position is out of grid, then error should be raised
#def test_search_goal_position_out_of_grid(grid, init, cost, DIRECTIONS, heuristic):
#    goal = [100, 0]
#    with pytest.raises(ValueError):
#        search(grid, init, goal, cost, heuristic, DIRECTIONS)
#