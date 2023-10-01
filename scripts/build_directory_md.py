#!/usr/bin/env python3

import os
from collections.abc import Iterator


import os
from typing import Iterator
from typing import Iterator, List

def good_file_paths(top_dir: str = ".") -> Iterator[str]:
    """
    This function generates file paths of certain file types from a specified directory.
    It excludes files from certain subdirectories and files with certain names.

    Arguments:
    top_dir: str, optional, default is ".".
             The root directory from which to start the search.

    Returns:
    An iterator yielding file paths as strings.

    Note:
    - Skips directories named 'scripts' and those starting with '.' or '_'.
    - Excludes files named '__init__.py'
    - Only includes '.py' or '.ipynb' files.
    """
    for dir_path, dir_names, filenames in os.walk(top_dir):
        dir_names[:] = do_not_recurse_in(dir_names)
        for filename in filenames:
            if is_valid_file(filename):
                yield os.path.join(dir_path, filename).lstrip("./")


def md_prefix(i):
    return f"{i * '  '}*" if i else "\n##"


def do_not_recurse_in(dir_names: list) -> list:
    """
    Helper function to filter out unwanted directories.

    Arguments:
    dir_names: list
               The list of directory names.

    Returns:
    A list of directory names to traverse in for os.walk.
    """
    return [d for d in dir_names if d != "scripts" and d[0] not in "._"]


def is_valid_file(filename: str) -> bool:
    """
    Helper function to check if a file is valid.

    Arguments:
    filename: str
              The name of the file.

    Returns:
    Bool. True if the file is valid; False otherwise.
    """
    return filename != "__init__.py" and os.path.splitext(filename)[1] in (
        ".py",
        ".ipynb",
    )


def print_path(old_path: str, new_path: str) -> str:
    old_parts = old_path.split(os.sep)
    for i, new_part in enumerate(new_path.split(os.sep)):
        if (i + 1 > len(old_parts) or old_parts[i] != new_part) and new_part:
            print(f"{md_prefix(i)} {new_part.replace('_', ' ').title()}")
    return new_path


def print_directory_md(top_dir: str = ".") -> None:
    old_path = ""
    for filepath in sorted(good_file_paths(top_dir)):
        filepath, filename = os.path.split(filepath)
        if filepath != old_path:
            old_path = print_path(old_path, filepath)
        indent = (filepath.count(os.sep) + 1) if filepath else 0
        url = f"{filepath}/{filename}".replace(" ", "%20")
        filename = os.path.splitext(filename.replace("_", " ").title())[0]
        print(f"{md_prefix(indent)} [{filename}]({url})")


if __name__ == "__main__":
    print_directory_md(".")
