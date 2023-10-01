from cellular_automata.conways_game_of_life import *
import pytest


@pytest.fixture
def sample_cells():
    return [
        [1, 1, 1, 1, 1],
        [0, 0, 1, 0, 0],
        [0, 0, 0, 1, 0],
        [0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0],
    ]


@pytest.fixture
def edge_case_cells():
    return [
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
    ]


def test_new_generation_execution(sample_cells):
    res = new_generation(sample_cells)
    assert res is not None, "Check that function executes and returns"


def test_new_generation_list_return(sample_cells):
    res = new_generation(sample_cells)
    assert isinstance(res, list), "result should be a list"


def test_new_generation_cell_count(sample_cells):
    res = new_generation(sample_cells)
    assert len(res) == len(sample_cells), "The number of cells should remain constant"


def test_new_generation_list_elements(sample_cells):
    res = new_generation(sample_cells)
    for row in res:
        for cell in row:
            assert cell in [0, 1], "Cell should be either alive(1) or dead(0)"


def test_new_generation_all_dead(edge_case_cells):
    res = new_generation(edge_case_cells)
    assert all(
        not any(row) for row in res
    ), "With no alive neighbours, all cells should remain dead"
