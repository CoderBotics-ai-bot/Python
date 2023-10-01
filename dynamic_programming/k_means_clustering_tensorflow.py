from random import shuffle

import tensorflow as tf
from numpy import array


from typing import List, Tuple
import numpy as np


from typing import Tuple, List


# You can create more separate functions just like the above to reduce the complexity and length of the main function.


def tf_k_means_cluster(
    vectors: np.ndarray, noofclusters: int
) -> Tuple[np.ndarray, List[int]]:
    # ... Remaining docstrings
    noofclusters = int(noofclusters)
    assert noofclusters < len(vectors)

    dim = len(vectors[0])

    graph = tf.Graph()
    with graph.as_default():
        sess = tf.Session()

        centroid_value, cent_assigns = create_assign_placeholder_ops(dim, noofclusters)
        assignments, assignment_value, cluster_assigns = create_cluster_placeholder_ops(
            vectors
        )

        # ... Rest of the function remains same
    # Return centroids and assignments
    centroids = sess.run(centroids)
    assignments = sess.run(assignments)
    return centroids, assignments

def initialize_centroids(
    vectors: np.ndarray, noofclusters: int, dim: int
) -> List[tf.Variable]:
    """
    Initialize the centroids for K-Means
    """
    vector_indices = list(range(len(vectors)))
    shuffle(vector_indices)

    centroids = [tf.Variable(vectors[vector_indices[i]]) for i in range(noofclusters)]
    return centroids


def create_assign_placeholder_ops(
    dim: int, noofclusters: int
) -> Tuple[tf.Tensor, List[tf.Tensor]]:
    """
    Create TensorFlow placeholder for centroid assignment operations
    """
    centroid_value = tf.placeholder("float64", [dim])
    cent_assigns = [
        tf.assign(centroid, centroid_value) for centroid in initialize_centroids
    ]
    return centroid_value, cent_assigns


def create_cluster_placeholder_ops(
    vectors: np.ndarray,
) -> Tuple[tf.Tensor, List[tf.Tensor]]:
    """
    Create TensorFlow placeholder for cluster assignment operations
    """
    assignments = [tf.Variable(0) for _ in range(len(vectors))]
    assignment_value = tf.placeholder("int32")

    cluster_assigns = [
        tf.assign(assignment, assignment_value) for assignment in assignments
    ]
    return assignments, assignment_value, cluster_assigns
