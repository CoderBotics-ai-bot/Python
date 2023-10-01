#from pytest import fixture, mark
#from other.dijkstra_bankers_algorithm import *
#import pytest
#from _pytest.capture import CaptureFixture
#
### GENERATED PYTESTS:
#
#
#@fixture
#def bankers_algorithm_instance() -> BankersAlgorithm:
#    claim_vector = [7, 5, 3]
#    allocated_resources_table = [[0, 1, 0], [2, 0, 0], [3, 0, 2]]
#    maximum_claim_table = [[7, 5, 3], [3, 2, 2], [9, 0, 2]]
#
#    return BankersAlgorithm(
#        claim_vector, allocated_resources_table, maximum_claim_table
#    )
#
#
#def test_pretty_data_no_error(bankers_algorithm_instance: BankersAlgorithm):
#    bankers_algorithm_instance._BankersAlgorithm__pretty_data()
#
#
#@mark.parametrize(
#    ("index", "expected_alloc", "expected_claim"),
#    [
#        (0, "P1       0       1       0", "P1       7       5       3"),
#        (1, "P2       2       0       0", "P2       3       2       2"),
#        (2, "P3       3       0       2", "P3       9       0       2"),
#    ],
#)
#def test_pretty_data_prints(
#    bankers_algorithm_instance: BankersAlgorithm,
#    capsys: CaptureFixture,
#    index: int,
#    expected_alloc: str,
#    expected_claim: str,
#):
#    bankers_algorithm_instance._BankersAlgorithm__pretty_data()
#
#    captured = capsys.readouterr()
#    output = captured.out.split("\n")
#    # Extract only processed lines removing the ending whitespaces
#    allocated_resource_table = [line.rstrip() for line in output[1:4]]
#    maximum_claim_table = [line.rstrip() for line in output[6:9]]
#
#    assert allocated_resource_table[index] == expected_alloc
#    assert maximum_claim_table[index] == expected_claim
#