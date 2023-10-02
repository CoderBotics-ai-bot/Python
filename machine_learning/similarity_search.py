"""
Similarity Search : https://en.wikipedia.org/wiki/Similarity_search
Similarity search is a search algorithm for finding the nearest vector from
vectors, used in natural language processing.
In this algorithm, it calculates distance with euclidean distance and
returns a list containing two data for each vector:
    1. the nearest vector
    2. distance between the vector and the nearest vector (float)
"""
from __future__ import annotations

import math

import numpy as np
from numpy.linalg import norm


from typing import List


from typing import List, Tuple


def euclidean(input_a: np.ndarray, input_b: np.ndarray) -> float:
    """
    Calculates euclidean distance between two data.
    :param input_a: ndarray of first vector.
    :param input_b: ndarray of second vector.
    :return: Euclidean distance of input_a and input_b. By using math.sqrt(),
             result will be float.

    >>> euclidean(np.array([0]), np.array([1]))
    1.0
    >>> euclidean(np.array([0, 1]), np.array([1, 1]))
    1.0
    >>> euclidean(np.array([0, 0, 0]), np.array([0, 0, 1]))
    1.0
    """
    return math.sqrt(sum(pow(a - b, 2) for a, b in zip(input_a, input_b)))

def similarity_search(
    dataset: np.ndarray, value_array: np.ndarray
) -> list[list[list[float] | float]]:
    """
    Find vectors in the dataset closest to the vectors in value_array.

    This function traverses the dataset and calculates the Euclidean distance
    between each vector in the dataset and the vectors in value_array.
    The function returns the vectors in the dataset closest to the vectors in
    value_array together with their respective distances.

    Arguments:
    dataset -- nd-array of vectors forming the dataset.
    value_array -- nd-array of vectors for which closest vectors in dataset are to be found.

    Returns:
    A list of lists where each sub-list contains the closest vector from the dataset to the
    corresponding vector in value_array and the calculated distance between them.
    """
    _validate_input(dataset, value_array)

    return [
        [vector, distance]
        for vector, distance in map(
            _find_closest_vector, value_array, [dataset] * len(value_array)
        )
    ]


def cosine_similarity(input_a: np.ndarray, input_b: np.ndarray) -> float:
    """
    Calculates cosine similarity between two data.
    :param input_a: ndarray of first vector.
    :param input_b: ndarray of second vector.
    :return: Cosine similarity of input_a and input_b. By using math.sqrt(),
             result will be float.

    >>> cosine_similarity(np.array([1]), np.array([1]))
    1.0
    >>> cosine_similarity(np.array([1, 2]), np.array([6, 32]))
    0.9615239476408232
    """
    return np.dot(input_a, input_b) / (norm(input_a) * norm(input_b))


def _validate_input(dataset: np.ndarray, value_array: np.ndarray) -> None:
    if dataset.ndim != value_array.ndim:
        raise ValueError(
            f"Wrong input data's dimensions... dataset : {dataset.ndim}, value_array : {value_array.ndim}"
        )

    if dataset.dtype != value_array.dtype:
        raise TypeError(
            f"Input data have different datatype... dataset : {dataset.dtype}, value_array : {value_array.dtype}"
        )

    if dataset.shape[1] != value_array.shape[1]:
        raise ValueError(
            f"Wrong input data's shape... dataset : {dataset.shape[1]}, value_array : {value_array.shape[1]}"
        )


def _find_closest_vector(
    value_array: np.ndarray, dataset: np.ndarray
) -> Tuple[List[float], float]:
    vector_dist_pairs = (
        (vector.tolist(), euclidean(value_array, vector)) for vector in dataset
    )
    return min(vector_dist_pairs, key=lambda pair: pair[1])


if __name__ == "__main__":
    import doctest

    doctest.testmod()
