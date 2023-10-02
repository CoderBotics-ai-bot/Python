#from machine_learning.self_organizing_map import *
#import pytest
#
#
#def test_get_winner_no_errors():
#    som = SelfOrganizingMap()
#    weights = [[1, 2, 3], [4, 5, 6]]
#    sample = [1, 2, 3]
#    assert som.get_winner(weights, sample) is not None
#
#
#def test_get_winner_return_type():
#    som = SelfOrganizingMap()
#    weights = [[1, 2, 3], [4, 5, 6]]
#    sample = [1, 2, 3]
#    result = som.get_winner(weights, sample)
#    assert isinstance(result, int)
#
#
#def test_get_winner_equal_weights():
#    som = SelfOrganizingMap()
#    weights = [[1, 2, 3], [1, 2, 3]]
#    sample = [1, 2, 3]
#    result = som.get_winner(weights, sample)
#    assert result == 0
#
#
#def test_get_winner_different_weights():
#    som = SelfOrganizingMap()
#    weights = [[1, 2, 3], [4, 5, 6]]
#    sample = [1, 2, 3]
#    result = som.get_winner(weights, sample)
#    assert result == 0
#