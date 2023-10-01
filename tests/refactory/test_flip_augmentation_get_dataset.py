

import pytest
from computer_vision.flip_augmentation import *
import pytest


def test_get_dataset_no_errors(tmp_path):
    # Preparation
    label_dir = tmp_path / "labels"
    label_dir.mkdir()
    img_dir = tmp_path / "images"
    img_dir.mkdir()

    label_file = label_dir / "test.txt"
    label_file.write_text("0 0.1 0.2 0.3 0.4\n")

    image_file = img_dir / "test.jpg"
    image_file.write_text("test image")

    # Execution
    result = get_dataset(str(label_dir), str(img_dir))

    # Verification
    assert result is not None
    assert isinstance(result, tuple)
    assert len(result) == 2
    assert all(isinstance(i, list) for i in result)


def test_get_dataset_empty_dir(tmp_path):
    # Preparation
    label_dir = tmp_path / "labels"
    label_dir.mkdir()
    img_dir = tmp_path / "images"
    img_dir.mkdir()

    # Execution
    result = get_dataset(str(label_dir), str(img_dir))

    # Verification
    assert result is not None
    assert isinstance(result, tuple)
    assert len(result) == 2
    assert all(isinstance(i, list) for i in result)
    assert all(len(i) == 0 for i in result)
