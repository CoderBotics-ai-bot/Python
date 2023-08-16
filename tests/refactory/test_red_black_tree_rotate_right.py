import pytest
from data_structures.binary_tree.red_black_tree import *


def test_rotate_right():
    # creating a basic RedBlackTree with few nodes
    root = RedBlackTree(7)
    root.left = RedBlackTree(5, parent=root)
    root.right = RedBlackTree(9, parent=root)

    # executing a rotate right operation
    new_root = root.rotate_right()

    # validating if the operation was correctly performed
    # if so, the new root should be 5
    assert new_root.label == 5
    # checking if the previous root (7) is now to the right of new root
    assert new_root.right.label == 7
    # also checking if the right child of the previous root is now to the right of the new right child
    assert new_root.right.right.label == 9

    # edge case of a single node: checking if the rotation does not affect a tree with a single node.
    single_node_tree = RedBlackTree(1)
    single_node_tree = single_node_tree.rotate_right()
    assert single_node_tree.label == 1
