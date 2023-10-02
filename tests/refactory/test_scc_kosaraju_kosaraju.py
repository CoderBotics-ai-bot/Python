#import pytest
#from graphs.scc_kosaraju import *
#
## global variables used in Kosaraju's
#graph = reversed_graph = visit = stack = None
#n = scc = component = None
#
#
#@pytest.fixture(scope="module")
#def setup_global_variables():
#    """
#    Setup global variables used in the Kosaraju's algorithm.
#    """
#    global n, graph, reversed_graph, scc, component, visit, stack
#
#    # let's create a graph with 5 vertices
#    n = 5
#    graph = {i: [] for i in range(n)}
#    reversed_graph = graph.copy()
#    visit = [False] * n
#    stack = []
#    scc = []
#    component = []
#
#    # let's setup dummy data, assuming dfs does a breadth-first search to fill data
#    for i in range(n):
#        dfs(i)
#
#    yield  # this is where the testing happens
#
#    # Teardown : clean-up actions (e.g., close db connections, stop server, clean files) after the tests have run.
#    n = None
#
#
#def test_kosaraju(setup_global_variables):
#    """
#    Test that the Kosaraju's Algorithm executes without errors, without checking correctness of output
#    """
#    assert kosaraju() is not None
#
#
## Write this line at the end of your file, it loads all the fixtures to the file
#pytest.main()
#