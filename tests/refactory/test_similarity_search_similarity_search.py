from machine_learning.similarity_search import *
import numpy as np
import pytest


def test_similarity_search():
    # Test no errors when function is executed
    dataset = np.array([[0, 0], [1, 1], [2, 2]])
    value_array = np.array([[0, 1]])
    result = similarity_search(dataset, value_array)
    assert result is not None

    # Test if it returns list of lists even for single dimension array
    dataset = np.array([[0], [1], [2]])
    value_array = np.array([[0]])
    result = similarity_search(dataset, value_array)
    assert type(result) is list
    assert type(result[0]) is list

    # Test if it returns correct nearest vector and distance for single dimensions
    dataset = np.array([[5], [15], [25]])
    value_array = np.array([[10]])
    result = similarity_search(dataset, value_array)
    assert result[0][0] == [5]
    assert result[0][1] == 5

    # Test if   it calculates correct euclidean distances
    dataset = np.array([[15, 15], [10, 10], [20, 20]])
    value_array = np.array([[12, 12]])
    result = similarity_search(dataset, value_array)
    assert result[0][0] == [10, 10]
    assert result[0][1] == np.sqrt(8)

    # Test if for multi-dimensions, it calculates euclidean distances
    dataset = np.array([[15, 15, 15], [10, 10, 10], [20, 20, 20]])
    value_array = np.array([[12, 12, 12]])
    result = similarity_search(dataset, value_array)
    assert result[0][0] == [10, 10, 10]
    assert result[0][1] == np.sqrt(12)

    # Test with wrong dimension
    dataset = np.array([[1]])
    value_array = np.array([1])
    with pytest.raises(ValueError):
        result = similarity_search(dataset, value_array)

    # Test with wrong shape
    dataset = np.array([[0, 0, 0], [0, 0, 1]])
    value_array = np.array([[0, 0], [1, 1], [2, 2]])
    with pytest.raises(ValueError):
        result = similarity_search(dataset, value_array)

    # Test with mismatched datatype
    dataset = np.array([[0, 0], [1, 1], [2, 2]], dtype=np.float32)
    value_array = np.array([[0, 0], [0, 1]], dtype=np.int32)
    with pytest.raises(TypeError):
        result = similarity_search(dataset, value_array)
