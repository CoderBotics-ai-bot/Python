#import glob
#from computer_vision.mosaic_augmentation import *
#
#import pytest
#import os
#
#
## Prepare test data for testing
#@pytest.fixture
#def test_data(tmp_path):
#    img_dir = tmp_path / "images"
#    img_dir.mkdir()
#    label_dir = tmp_path / "labels"
#    label_dir.mkdir()
#
#    txt_file = label_dir / "label1.txt"
#    txt_file.write_text("1 0.3 0.4 0.6 0.8")
#
#    # fake jpg file
#    jpg_file = img_dir / "label1.jpg"
#    jpg_file.write_text("fake jpg file")
#
#    return str(label_dir), str(img_dir)
#
#
#def test_get_dataset_no_exception(test_data):
#    label_dir, img_dir = test_data
#    result = get_dataset(label_dir, img_dir)
#    assert result is not None
#
#
#def test_get_dataset_content_check(test_data):
#    label_dir, img_dir = test_data
#    img_paths, labels = get_dataset(label_dir, img_dir)
#
#    assert len(img_paths) == 1
#    assert len(labels) == 1
#
#    # Check the contents
#    assert all(isinstance(item, str) for item in img_paths)
#    assert all(isinstance(sublist, list) for sublist in labels)
#    assert all(len(lst) == 5 for lst in labels)
#
#
#def test_get_dataset_empty_label_dir(tmp_path):
#    img_dir = tmp_path / "images"
#    img_dir.mkdir()
#    label_dir = tmp_path / "empty_labels"
#    label_dir.mkdir()
#
#    img_paths, labels = get_dataset(str(label_dir), str(img_dir))
#
#    assert len(img_paths) == 0
#    assert len(labels) == 0
#
#
#def test_get_dataset_nonexistent_dirs():
#    img_paths, labels = get_dataset("nonexistent", "nonexistent")
#
#    assert len(img_paths) == 0
#    assert len(labels) == 0
#