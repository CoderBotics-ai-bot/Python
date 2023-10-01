from computer_vision.mosaic_augmentation import *
import os
from unittest.mock import mock_open, patch
from typing import List

import pytest


def test_get_dataset():
    # Test if the get_dataset function doesn't throw errors when it's executed
    dataset = get_dataset("label_dir", "img_dir")
    assert dataset is not None


@patch("builtins.open", new_callable=mock_open, read_data="0 0.5 0.5 0.1 0.1\n")
def test_get_dataset_with_valid_data(mock_data):
    # Test get_dataset function when given valid data
    with patch("glob.glob") as mock_glob:
        mock_glob.return_value = ["path/to/label/file.txt"]
        dataset = get_dataset("path/to/label", "path/to/image")
        assert len(dataset) == 2
        assert len(dataset[0]) == 1
        assert len(dataset[1]) == 1
        assert dataset[0][0] == "path/to/image/file.jpg"
        assert dataset[1][0][0] == [0, 0.45, 0.45, 0.55, 0.55]


def test_get_dataset_with_empty_label():
    # Test get_dataset function when label file is empty
    with patch("glob.glob") as mock_glob, patch(
        "builtins.open", new_callable=mock_open, read_data=""
    ) as mock_data:
        mock_glob.return_value = ["path/to/label/file.txt"]
        dataset = get_dataset("path/to/label", "path/to/image")
        assert len(dataset) == 2
        assert len(dataset[0]) == 0
        assert len(dataset[1]) == 0


def test_get_dataset_with_no_label_files():
    # Test get_dataset function when there are no label files
    with patch("glob.glob") as mock_glob:
        mock_glob.return_value = []
        dataset = get_dataset("path/to/label", "path/to/image")
        assert len(dataset) == 2
        assert len(dataset[0]) == 0
        assert len(dataset[1]) == 0
