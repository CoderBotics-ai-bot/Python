
import pytest
from graphs.tarjans_scc import *
from collections import deque


def test_tarjan_no_errors():
    default_graph = [[2, 3], [0], [1], [4], []]
    assert tarjan(default_graph) is not None


def test_tarjan_type_errors():
    with pytest.raises(TypeError):
        tarjan("123")
        tarjan(123)
        tarjan(None)


def test_tarjan_index_errors():
    with pytest.raises(IndexError):
        tarjan([[1]])
