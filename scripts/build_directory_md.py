#!/usr/bin/env python3

import os
from collections.abc import Iterator


import os
from typing import Iterator
from typing import Iterator, List
from typing import List
from typing import Iterator, List, Tuple

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

def print_directory_md(top_dir: str = ".") -> None:
    """
    Prints the directory structure of a given directory in the format of a markdown document.

    This function gets all valid file paths from the specified directory (by default, the current directory),
    orders them, and then prints them. The output is indented and formatted as links in a markdown document,
    providing a clickable directory tree when rendered.

    Arguments:
    top_dir: str, optional, default is ".".
             The root directory from which to start generating the directory structure.

    Returns:
    None

    Note:
    - Each directory and file is printed as a markdown link, making the directory structure clickable when rendered as markdown.
    - Files and directories starting with '.' or '_' or named 'scripts' are excluded.
    - The '__init__.py' files are also excluded.
    """
    old_path = ""
    for filepath in sorted(good_file_paths(top_dir)):
        old_path = print_path_update_filepath(filepath, old_path)
        file_url, file_name = generate_md_link(filepath)
        print(f"{md_prefix(indent)} [file_name](file_url)")

def print_path(old_path: str, new_path: str) -> str:
    old_parts = old_path.split(os.sep)
    new_parts = new_path.split(os.sep)

    for i, new_part in enumerate(new_parts):
        if new_part and _has_changed(i, old_parts, new_part):
            print(f"{md_prefix(i)} {new_part.replace('_', ' ').title()}")

    return new_path


def print_path_update_filepath(filepath: str, old_path: str) -> str:
    """
    Print the path if it has changed and return the updated filepath.

    Arguments:
    filepath: str, The file path to process.
    old_path: str, The previous file path.

    Returns:
    str: The updated file path.
    """
    filepath, filename = os.path.split(filepath)
    if filepath != old_path:
        old_path = print_path(old_path, filepath)
    return old_path


def generate_md_link(filepath: str) -> tuple:
    """
    Generate a markdown link for a given file path.

    Arguments:
    filepath: str, The file path for which to generate a markdown link.

    Returns:
    tuple: A tuple with the file's url and file name.
    """
    indent = (filepath.count(os.sep) + 1) if filepath else 0
    url = f"{filepath}/{filename}".replace(" ", "%20")
    filename = os.path.splitext(filename.replace("_", " ").title())[0]
    return url, filename


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


def _has_changed(i: int, old_parts: List[str], new_part: str) -> bool:
    return i + 1 > len(old_parts) or old_parts[i] != new_part


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


if __name__ == "__main__":
    print_directory_md(".")
