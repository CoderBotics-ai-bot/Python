#from graphs.page_rank import *
#
#import pytest
#from typing import List, NamedTuple
#
#
## Defining this class as a substitute for the Node class in scope,
## since I don't have the complete code for the Node class.
#class Node(NamedTuple):
#    name: str
#    outbound: List[str]
#    inbound: List[str]
#
#
#def test_page_rank_no_errors(capfd):
#    nodes = [Node("name1", ["name2"], ["name3"]), Node("name2", ["name3"], ["name1"])]
#    page_rank(nodes)
#    captured = capfd.readouterr()
#    assert "======= Iteration 1 =======" in captured.out
#
#
#def test_page_rank_with_no_nodes(capfd):
#    nodes = []
#    page_rank(nodes)
#    captured = capfd.readouterr()
#    assert captured.out == ""
#
#
#def test_page_rank_with_single_node_no_links(capfd):
#    nodes = [Node("name1", [], [])]
#    page_rank(nodes)
#    captured = capfd.readouterr()
#    assert "======= Iteration 1 =======" in captured.out
#
#
#def test_page_rank_with_single_node_self_link(capfd):
#    nodes = [Node("name1", ["name1"], ["name1"])]
#    page_rank(nodes)
#    captured = capfd.readouterr()
#    assert "======= Iteration 1 =======" in captured.out
#
#
#def test_page_rank_with_two_nodes_no_links_to_each_other(capfd):
#    nodes = [Node("name1", [], []), Node("name2", [], [])]
#    page_rank(nodes)
#    captured = capfd.readouterr()
#    assert "======= Iteration 1 =======" in captured.out
#
#
#def test_page_rank_with_two_nodes_link_to_each_other(capfd):
#    nodes = [Node("name1", ["name2"], ["name2"]), Node("name2", ["name1"], ["name1"])]
#    page_rank(nodes)
#    captured = capfd.readouterr()
#    assert "======= Iteration 1 =======" in captured.out
#