#
#import pytest
#from graphs.edmonds_karp_multiple_source_and_sink import *
#from typing import Any
#
#
#@pytest.fixture
#def flow_network() -> Any:
#    graph = [
#        [0, 16, 15, 0, 0, 0],
#        [0, 0, 15, 12, 0, 0],
#        [0, 4, 0, 0, 15, 0],
#        [0, 0, 10, 0, 0, 20],
#        [0, 0, 0, 8, 0, 4],
#        [0, 0, 0, 0, 0, 0],
#    ]
#    sources = [0]
#    sinks = [5]
#    fn = FlowNetwork(graph, sources, sinks)
#    fn.maximum_flow_algorithm = MaximumFlowAlgorithmExecutor(fn)
#    return fn
#
#
#def test_find_maximum_flow_does_not_throw(flow_network: Any) -> None:
#    try:
#        result = flow_network.find_maximum_flow()
#    except Exception:
#        pytest.fail("The method find_maximum_flow did throw an exception")
#
#
#def test_find_maximum_flow_without_algorithm(flow_network: Any) -> None:
#    flow_network.maximum_flow_algorithm = None
#    with pytest.raises(
#        Exception, match="You need to set maximum flow algorithm before."
#    ):
#        flow_network.find_maximum_flow()
#
#
#def test_find_maximum_flow_without_source_or_sink(flow_network: Any) -> None:
#    flow_network.source_index = None
#    flow_network.sink_index = None
#    assert (
#        flow_network.find_maximum_flow() == 0
#    ), "The function should return 0 if there is no source or sink"
#