import os


import os

import pytest
from scripts.build_directory_md import *


@pytest.fixture
def file_structure(tmp_path):
    d = tmp_path / "dir"
    d.mkdir()
    subdir = d / "subdir"
    subdir.mkdir()
    python_file = subdir / "file.py"
    python_file.write_text("Python code...")
    ignore_dir = d / "scripts"
    ignore_dir.mkdir()
    ignore_file = ignore_dir / "file.txt"
    ignore_file.write_text("To be ignored...")
    return d


def test_good_file_paths_no_throw(file_structure):
    # Absence of exceptions and not None result is a good result for first test
    assert good_file_paths(str(file_structure)) is not None


def test_good_file_paths(file_structure):
    # We expect the Python file to be found, not other files and directories
    result = list(good_file_paths(str(file_structure)))
    assert len(result) == 1
    assert "file.py" in result[0]


def test_good_file_paths_no_py_files(file_structure):
    # If there are no .py files, result should be empty
    for python_file in file_structure.glob("**/*.py"):
        python_file.unlink()
    result = list(good_file_paths(str(file_structure)))
    assert len(result) == 0
