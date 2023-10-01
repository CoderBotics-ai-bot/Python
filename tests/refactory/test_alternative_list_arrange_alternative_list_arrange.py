import pytest
from other.alternative_list_arrange import *


def test_alternative_list_arrange_no_error():
    assert alternative_list_arrange(["A", "B", "C", "D"], [1, 2, 3, 4]) is not None
    assert alternative_list_arrange([1, 2, 3, 4], ["A", "B", "C", "D"]) is not None
    assert alternative_list_arrange([], []) is not None
    assert alternative_list_arrange(["A", "B", "C", "D"], []) is not None
    assert alternative_list_arrange([1, 2, 3, 4], []) is not None
    assert alternative_list_arrange([], ["A", "B", "C", "D"]) is not None
    assert alternative_list_arrange([], [1, 2, 3, 4]) is not None


def test_alternative_list_arrange_expected():
    assert alternative_list_arrange([1, 2, 3, 4], ["A", "B", "C", "D"]) == [
        1,
        "A",
        2,
        "B",
        3,
        "C",
        4,
        "D",
    ]
    assert alternative_list_arrange(["A", "B", "C", "D"], [1, 2, 3, 4]) == [
        "A",
        1,
        "B",
        2,
        "C",
        3,
        "D",
        4,
    ]
    assert alternative_list_arrange([1, 2, 3, 4], []) == [1, 2, 3, 4]
    assert alternative_list_arrange([], ["A", "B", "C", "D"]) == ["A", "B", "C", "D"]


def test_alternative_list_arrange_one_more_item():
    assert alternative_list_arrange([1, 2, 3, 4, 5], ["A", "B", "C", "D"]) == [
        1,
        "A",
        2,
        "B",
        3,
        "C",
        4,
        "D",
        5,
    ]
    assert alternative_list_arrange(["A", "B", "C", "D", "E"], [1, 2, 3, 4]) == [
        "A",
        1,
        "B",
        2,
        "C",
        3,
        "D",
        4,
        "E",
    ]


def test_alternative_list_arrange_types():
    assert alternative_list_arrange(
        [1, "B", 3.1, "D", True], ["A", 2, "C", 4.2, False]
    ) == [1, "A", "B", 2, 3.1, "C", "D", 4.2, True, False]
