import pytest
from scripts.build_directory_md import *


def test_print_path_no_throw():
    assert print_path("old/sample/path", "new/sample/path") is not None


def test_print_path_empty_strings():
    assert print_path("", "") == ""


def test_print_path_single_part_paths():
    assert print_path("old", "new") == "new"


def test_print_path_substring_old_path():
    assert print_path("sample", "sample/path") == "sample/path"


def test_print_path_substring_new_path():
    assert print_path("sample/path", "sample") == "sample"


@pytest.mark.parametrize(
    "old_path,new_path",
    [
        ("old/folder/path", "new/folder/path"),
        ("/old/folder/path", "new/folder/path"),
        ("old/folder/path/", "/new/folder/path"),
    ],
)
def test_print_path_variants(old_path, new_path):
    assert print_path(old_path, new_path) == new_path
