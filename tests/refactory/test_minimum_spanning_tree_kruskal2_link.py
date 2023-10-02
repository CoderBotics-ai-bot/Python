
import pytest
from typing import Generic, TypeVar
from graphs.minimum_spanning_tree_kruskal2 import *

T = TypeVar("T")


class Node(Generic[T]):
    def __init__(self, rank: int):
        self.rank = rank
        self.parent = None


@pytest.fixture
def create_nodes() -> tuple[Node[T], Node[T]]:
    return Node(1), Node(2)


@pytest.fixture
def create_tree():
    return DisjointSetTree()


def test_link_not_throwing_errors(create_tree, create_nodes):
    node1, node2 = create_nodes
    assert create_tree.link(node1, node2) is None


def test_link_nodes_with_different_ranks(create_nodes):
    tree = DisjointSetTree()
    node1, node2 = create_nodes
    node1.rank = 2
    node2.rank = 1
    tree.link(node1, node2)
    assert node2.parent is node1


def test_link_nodes_with_same_ranks(create_nodes):
    tree = DisjointSetTree()
    node1, node2 = create_nodes
    node1.rank = node2.rank = 2
    tree.link(node1, node2)
    assert node1.parent is node2
    assert node2.rank == 3
