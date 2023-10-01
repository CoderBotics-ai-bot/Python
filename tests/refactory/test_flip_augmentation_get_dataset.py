from os.path import join


from glob import glob
import pytest

import pytest
from computer_vision.flip_augmentation import *


def test_get_dataset_no_errors(tmpdir):
    file = tmpdir.mkdir("sub").join(".txt")
    file.write("0 0.1 0.2 0.3 0.4")
    assert get_dataset(str(tmpdir), str(tmpdir)) is not None


def test_get_dataset_empty_file(tmpdir):
    file = tmpdir.mkdir("sub").join(".txt")
    file.write("")
    assert get_dataset(str(tmpdir), str(tmpdir)) == ([], [])


def test_get_dataset_multiple_files(tmpdir):
    file1 = tmpdir.mkdir("sub1").join(".txt")
    file1.write("0 0.1 0.2 0.3 0.4")
    file2 = tmpdir.mkdir("sub2").join(".txt")
    file2.write("1 0.2 0.3 0.4 0.5")
    assert get_dataset(str(tmpdir), str(tmpdir)) is not None


def test_get_dataset_file_does_not_exist(tmpdir):
    assert get_dataset(str(tmpdir), str(tmpdir)) == ([], [])
