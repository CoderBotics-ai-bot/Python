
import pytest
import pytest
from searches.tabu_search import *


def test_find_neighborhood_no_error():
    solution = ["a", "c", "b", "d", "e", "a"]
    dict_of_neighbours = {
        "a": [["b", "20"], ["c", "18"], ["d", "22"], ["e", "26"]],
        "c": [["a", "18"], ["b", "10"], ["d", "23"], ["e", "24"]],
        "b": [["a", "20"], ["c", "10"], ["d", "11"], ["e", "12"]],
        "e": [["a", "26"], ["b", "12"], ["c", "24"], ["d", "40"]],
        "d": [["a", "22"], ["b", "11"], ["c", "23"], ["e", "40"]],
    }
    assert find_neighborhood(solution, dict_of_neighbours) is not None


### **Import Statements**

from typing import Dict, List
