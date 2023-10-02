#
#
#from typing import List, Tuple
#
#import pytest
#from graphs.dijkstra_algorithm import *
#from typing import List, Tuple
#from source_file import PriorityQueue
#
#
#def test_priority_queue_min_heapify_no_errors(priority_queue_instance):
#    priority_queue_instance.array = [(3, "Node1"), (1, "Node2"), (2, "Node3")]
#    priority_queue_instance.cur_size = 3
#    priority_queue_instance.min_heapify(0)
#    assert priority_queue_instance.array[0][0] != 3
#    assert priority_queue_instance.array[0][1] == "Node2"
#
#
#def test_priority_queue_min_heapify_no_reordering_needed(priority_queue_instance):
#    priority_queue_instance.array = [(1, "Node1"), (2, "Node2"), (3, "Node3")]
#    priority_queue_instance.cur_size = 3
#    priority_queue_instance.min_heapify(0)
#    assert priority_queue_instance.array[0][0] == 1
#    assert priority_queue_instance.array[0][1] == "Node1"
#
#
#def test_priority_queue_min_heapify_empty_queue(priority_queue_instance):
#    with pytest.raises(IndexError):
#        priority_queue_instance.min_heapify(0)
#
#
#def test_priority_queue_min_heapify_single_element(priority_queue_instance):
#    priority_queue_instance.array = [(1, "Node1")]
#    priority_queue_instance.cur_size = 1
#    priority_queue_instance.min_heapify(0)
#    assert priority_queue_instance.array[0][0] == 1
#    assert priority_queue_instance.array[0][1] == "Node1"
#
#
#@pytest.fixture
#def priority_queue_instance() -> PriorityQueue:
#    return PriorityQueue()
#