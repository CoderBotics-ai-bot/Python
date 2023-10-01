
import pytest
from other.dijkstra_bankers_algorithm import *
from typing import List


def test_bankers_algorithm_processes_resource_summation_no_error(
    bankers_algorithm_instance,
):
    try:
        bankers_algorithm_instance._BankersAlgorithm__processes_resource_summation()
    except Exception as e:
        pytest.fail(f"Test failed, got unexpected error: {str(e)}")


def test_bankers_algorithm_processes_resource_summation_returns_list(
    bankers_algorithm_instance,
):
    result = (
        bankers_algorithm_instance._BankersAlgorithm__processes_resource_summation()
    )
    assert isinstance(result, List), "Expected a result of List type"


def test_bankers_algorithm_processes_resource_summation_returns_int_elements(
    bankers_algorithm_instance,
):
    result = (
        bankers_algorithm_instance._BankersAlgorithm__processes_resource_summation()
    )
    assert all(
        isinstance(i, int) for i in result
    ), "Expected all elements in result list to be of int type"


@pytest.fixture
def bankers_algorithm_instance():
    claim_vector = [2, 1, 2]
    allocated_resources_table = [[2, 1, 1], [1, 2, 1], [1, 1, 2]]
    maximum_claim_table = [[3, 2, 2], [2, 3, 2], [2, 2, 3]]
    return BankersAlgorithm(
        claim_vector, allocated_resources_table, maximum_claim_table
    )
