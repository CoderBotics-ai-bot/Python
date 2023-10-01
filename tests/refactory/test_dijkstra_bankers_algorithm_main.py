#from other.dijkstra_bankers_algorithm import *
#import pytest
#
#
#def test_main_no_error(bankers_algorithm_instance: BankersAlgorithm):
#    try:
#        bankers_algorithm_instance.main(describe=True)
#    except Exception as e:
#        pytest.fail(f"BankersAlgorithm.main() raised exception {e}")
#
#
#def test_main_unsafe_state(bankers_algorithm_instance: BankersAlgorithm, capsys):
#    bankers_algorithm_instance.main(describe=False)
#    captured = capsys.readouterr()
#    output = captured.out
#    expected_substring = "System in unsafe state. Aborting..."
#    assert expected_substring in output, f"{expected_substring} not found in output"
#