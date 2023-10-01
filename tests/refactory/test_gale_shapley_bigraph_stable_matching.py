import pytest
from graphs.gale_shapley_bigraph import *


def test_stable_matching_not_throws():
    donor_pref = [[0, 1, 3, 2], [0, 2, 3, 1], [1, 0, 2, 3], [0, 3, 1, 2]]
    recipient_pref = [[3, 1, 2, 0], [3, 1, 0, 2], [0, 3, 1, 2], [1, 0, 3, 2]]
    result = stable_matching(donor_pref, recipient_pref)
    assert result is not None


def test_stable_matching_with_single_item_lists():
    donor_pref = [[0]]
    recipient_pref = [[0]]
    result = stable_matching(donor_pref, recipient_pref)
    assert result == [0]


def test_stable_matching_with_two_items_lists():
    donor_pref = [[0, 1], [1, 0]]
    recipient_pref = [[0, 1], [1, 0]]
    result = stable_matching(donor_pref, recipient_pref)
    assert result == [0, 1]


def test_stable_matching_with_mismatched_prefs():
    donor_pref = [[0, 1, 3, 2], [0, 2, 3, 1], [1, 0, 2, 3], [0, 3, 1, 2]]
    recipient_pref = [[3, 1, 2, 0], [3, 1, 0, 2], [0, 3, 1, 2]]
    with pytest.raises(AssertionError):
        result = stable_matching(donor_pref, recipient_pref)
