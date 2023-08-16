import pytest
from data_structures.binary_tree.red_black_tree import *


from pytest import fixture as Fixture


@pytest.fixture
def red_black_tree_fixture() -> RedBlackTree:
    """Fixture to set up a basic RedBlackTree."""
    tree = RedBlackTree(0)
    tree.insert(8)
    tree.insert(-8)
    tree.insert(4)
    tree.insert(12)
    tree.insert(10)
    tree.insert(11)
    return tree


def test_search_through_tree_for_values_not_present(
    red_black_tree_fixture: Fixture,
) -> None:
    """Tests for searching not present elements inside the tree."""
    assert 5 not in red_black_tree_fixture
    assert -6 not in red_black_tree_fixture
    assert -10 not in red_black_tree_fixture
    assert 13 not in red_black_tree_fixture


def test_search_through_tree_for_values_present(
    red_black_tree_fixture: Fixture,
) -> None:
    """Tests for searching present elements inside the tree."""
    assert 11 in red_black_tree_fixture
    assert 12 in red_black_tree_fixture
    assert -8 in red_black_tree_fixture
    assert 0 in red_black_tree_fixture
