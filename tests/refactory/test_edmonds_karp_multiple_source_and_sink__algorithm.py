#
#import pytest
#from PushRelabelExecutor import PushRelabelExecutor
#from FlowNetwork import FlowNetwork
#from graphs.edmonds_karp_multiple_source_and_sink import *
#from typing import List
#
#
#@pytest.fixture
#def flow_network() -> FlowNetwork:
#    # Create a flow network object with some vertices and edges
#    fn = FlowNetwork()
#    return fn
#
#
#@pytest.fixture
#def push_relabel_executor(flow_network) -> PushRelabelExecutor:
#    # Create a PushRelabelExecutor object using flow network fixture
#    pre = PushRelabelExecutor(flow_network)
#    return pre
#
#
#def test_algorithm_no_exception(push_relabel_executor):
#    try:
#        push_relabel_executor._algorithm()
#        assert True
#    except Exception:
#        assert False
#
#
#def test_possible_push_relabel(push_relabel_executor):
#    push_relabel_executor._algorithm()
#
#    assert all(
#        e >= 0 for e in push_relabel_executor.excesses
#    ), "Excesses should be greater than or equal to 0"
#
#
#def test_heights_not_null(push_relabel_executor):
#    push_relabel_executor._algorithm()
#
#    assert push_relabel_executor.heights is not None, "Heights should be initialized"
#
#
#def test_maximum_flow_not_null(push_relabel_executor):
#    push_relabel_executor._algorithm()
#
#    assert (
#        push_relabel_executor.maximum_flow is not None
#    ), "Maximum flow should be calculated"
#
#
#def test_preflow_not_null(push_relabel_executor):
#    push_relabel_executor._algorithm()
#
#    assert push_relabel_executor.preflow is not None, "Preflow should be initialized"
#
#
#def test_excesses_not_null(push_relabel_executor):
#    push_relabel_executor._algorithm()
#
#    assert push_relabel_executor.excesses is not None, "Excesses should be initialized"
#
#
#def test_greater_height(push_relabel_executor):
#    push_relabel_executor._algorithm()
#    source_height = push_relabel_executor.heights[push_relabel_executor.source_index]
#
#    assert (
#        source_height == push_relabel_executor.verticies_count
#    ), "Height of source vertex should be equal to total vertices count"
#
#
#configfile: pytest.ini
#
#
## Generate tests for func.name='_algorithm' following the Test Generation Guidelines.
#