#from graphs.multi_heuristic_astar import *
#import pytest
#
#
#def test_expand_state():
#    s = (0, 0)
#    j = 0
#    visited: Set[TPos] = set()
#    g_function: Dict[TPos, float] = {s: 0}
#    close_list_anchor: Set[TPos] = set()
#    close_list_inad: Set[TPos] = set()
#    open_list: TOpenList = [PriorityQueue() for _ in range(2)]
#    back_pointer: Dict[TPos, TPos] = {s: None}
#
#    expand_state(
#        s,
#        j,
#        visited,
#        g_function,
#        close_list_anchor,
#        close_list_inad,
#        open_list,
#        back_pointer,
#    )
#
#    assert g_function[s] == 0
#    assert s in visited
#    assert open_list[0].qsize() == 0
#    assert all([node not in close_list_anchor for node in open_list[0]])
#    assert all([node not in close_list_inad for node in open_list[0]])
#