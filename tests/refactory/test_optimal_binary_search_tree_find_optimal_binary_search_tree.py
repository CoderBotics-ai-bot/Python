

from collections import namedtuple
import pytest
from contextlib import redirect_stdout
from dynamic_programming.optimal_binary_search_tree import *
from io import StringIO


def test_find_optimal_binary_search_tree_no_error():
    Node = namedtuple("Node", ["key", "freq"])
    nodes = [
        Node(12, 8),
        Node(10, 34),
        Node(20, 50),
        Node(42, 3),
        Node(25, 40),
        Node(37, 30),
    ]
    out = StringIO()
    with redirect_stdout(out):
        find_optimal_binary_search_tree(nodes)
    assert out.getvalue() != ""


def test_find_optimal_binary_search_tree_single_node_no_error():
    Node = namedtuple("Node", ["key", "freq"])
    nodes = [Node(10, 34)]
    out = StringIO()
    with redirect_stdout(out):
        find_optimal_binary_search_tree(nodes)
    assert out.getvalue() != ""


# test with input that has duplicate keys
def test_find_optimal_binary_search_tree_duplicate_keys_no_error():
    Node = namedtuple("Node", ["key", "freq"])
    nodes = [Node(10, 34), Node(10, 32), Node(20, 20), Node(20, 18)]
    out = StringIO()
    with redirect_stdout(out):
        find_optimal_binary_search_tree(nodes)
    assert out.getvalue() != ""
