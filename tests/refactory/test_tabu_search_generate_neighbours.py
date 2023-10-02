import os

import pytest
from typing import Dict, List
from searches.tabu_search import *


def test_generate_neighbours_no_error():
    test_file_path = "test.txt"
    with open(test_file_path, "w") as file:
        file.write("a b 1\nb c 2")

    try:
        result = generate_neighbours(test_file_path)
        assert result != None
    finally:
        os.remove(test_file_path)


def test_generate_neighbours_empty_file():
    test_file_path = "test.txt"
    with open(test_file_path, "w") as file:
        file.write("")

    try:
        result = generate_neighbours(test_file_path)
        assert len(result) == 0
    finally:
        os.remove(test_file_path)


def test_generate_neighbours_single_line():
    test_file_path = "test.txt"
    with open(test_file_path, "w") as file:
        file.write("a b 1\n")

    try:
        result = generate_neighbours(test_file_path)
        assert len(result) == 2
        assert "a" in result
        assert "b" in result
        assert result["a"] == [["b", "1"]]
        assert result["b"] == [["a", "1"]]
    finally:
        os.remove(test_file_path)


def test_generate_neighbours_multi_lines():
    test_file_path = "test.txt"
    with open(test_file_path, "w") as file:
        file.write("a b 1\nc d 2\n")

    try:
        result = generate_neighbours(test_file_path)
        assert len(result) == 4
        assert "a" in result
        assert "b" in result
        assert "c" in result
        assert "d" in result
        assert result["a"] == [["b", "1"]]
        assert result["b"] == [["a", "1"]]
        assert result["c"] == [["d", "2"]]
        assert result["d"] == [["c", "2"]]
    finally:
        os.remove(test_file_path)
