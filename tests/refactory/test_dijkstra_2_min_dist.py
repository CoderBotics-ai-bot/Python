from graphs.dijkstra_2 import *
import pytest


def test_min_dist_no_errors():
    mdist = [0, 7, 6, 2, float("inf"), float("inf")]
    vset = [False, False, False, False, False, False]
    v = 6
    assert min_dist(mdist, vset, v) is not None


def test_min_dist_with_empty_mdist_and_vset():
    mdist = []
    vset = []
    v = 0
    assert min_dist(mdist, vset, v) == -1


def test_min_dist_with_all_infinities():
    mdist = [float("inf"), float("inf"), float("inf")]
    vset = [False, False, False]
    v = 3
    assert min_dist(mdist, vset, v) == -1


def test_min_dist_with_all_vset_trues():
    mdist = [5, 6, 7, 8]
    vset = [True, True, True, True]
    v = 4
    assert min_dist(mdist, vset, v) == -1
