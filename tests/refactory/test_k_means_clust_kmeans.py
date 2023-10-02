from machine_learning.k_means_clust import *
import pytest


def test_kmeans_empty_data():
    empty_data = pd.DataFrame()
    k = 2
    initial_centroids = np.array([[0, 0], [1, 0]])
    with pytest.raises(ValueError):
        _, _ = kmeans(empty_data, k, initial_centroids)


def test_kmeans_single_data_points():
    single_point_data = pd.DataFrame({"x": [1], "y": [5]})
    k = 1
    initial_centroids = np.array([[0, 0]])
    centroids, cluster_assignment = kmeans(single_point_data, k, initial_centroids)
    assert centroids is not None
    assert cluster_assignment is not None
