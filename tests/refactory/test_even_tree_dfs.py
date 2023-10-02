#from graphs.even_tree import *
#import pytest
#
#
#import pytest
#
#
#def test_dfs_not_crashing():
#    """
#    Here we are not focusing on the correctness or behavior of the function dfs, instead we
#    are just checking if the function is syntactically correct, doesn't crash with the expected inputs,
#    the Python environment is working properly and all imported libraries work as expected.
#    """
#
#    try:
#        global visited
#        visited = {}
#        global cuts
#        cuts = []
#        global tree
#        tree = {1: [2], 2: [3], 3: [4, 5], 4: [], 5: []}
#        assert dfs(1) is not None
#    except:
#        pytest.fail("Unexpected Error ..")
#
#
#def test_dfs_raises_error():
#    # Test: start of DFS not in global tree
#    try:
#        global visited
#        visited = {}
#        global cuts
#        cuts = []
#        global tree
#        tree = {1: [2], 2: [3], 3: [4, 5], 4: [], 5: []}
#        with pytest.raises(KeyError):
#            dfs(7)
#    except:
#        pytest.fail("Unexpected Error ..")
#