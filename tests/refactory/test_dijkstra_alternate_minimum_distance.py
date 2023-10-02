from graphs.dijkstra_alternate import *
import pytest


def test_minimum_distance_execution():
    g = Graph(3)
    assert g.minimum_distance([1, 2, 3], [False, False, True]) is not None


def test_minimum_distance_for_one_vertex():
    g = Graph(1)
    assert g.minimum_distance([2], [False]) == 0


def test_minimum_distance_no_visited_vertex():
    g = Graph(4)
    assert g.minimum_distance([2, 3, 4, 5], [False, False, False, False]) == 0


def test_minimum_distance_with_zero_distance():
    g = Graph(3)
    assert g.minimum_distance([0, 2, 3], [False, False, True]) == 0


def test_minimum_distance_with_same_distances():
    g = Graph(3)
    assert g.minimum_distance([1, 1, 1], [False, False, True]) == 0


def test_minimum_distance_with_negative_distances():
    g = Graph(3)
    assert g.minimum_distance([-1, -2, -3], [False, True, True]) == 0
