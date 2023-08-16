from other.lfu_cache import *
import pytest


def test_lfu_cache_put_method():
    # Test for adding a new key-value pair when cache isn't full
    cache = LFUCache(5)
    cache.put("test1", "value1")

    # The cache should contain one item now
    assert cache.num_keys == 1
    assert cache.list.head.next.key == "test1"
    assert cache.cache["test1"].val == "value1"

    # Test for adding a new key-value pair when cache is full
    cache.put("test2", "value2")
    cache.put("test3", "value3")
    cache.put("test4", "value4")
    cache.put("test5", "value5")

    # The cache should contain five items now
    assert cache.num_keys == 5

    # Try adding another key-value pair, forcing deletion of the least frequently used item
    cache.put("test6", "value6")
    assert "test1" not in cache.cache.keys()  # "test1" should have been removed
    assert cache.list.head.next.key != "test1"

    # Test for updating the value of an existing key
    cache.put("test2", "newvalue")
    assert cache.cache["test2"].val == "newvalue"
