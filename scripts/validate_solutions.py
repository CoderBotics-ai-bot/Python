#!/usr/bin/env python3
import hashlib
import importlib.util
import json
import os
import pathlib
from types import ModuleType

import pytest
import requests


from typing import List

PROJECT_EULER_DIR_PATH = pathlib.Path.cwd().joinpath("project_euler")
PROJECT_EULER_ANSWERS_PATH = pathlib.Path.cwd().joinpath(
    "scripts", "project_euler_answers.json"
)

with open(PROJECT_EULER_ANSWERS_PATH) as file_handle:
    PROBLEM_ANSWERS: dict[str, str] = json.load(file_handle)


def convert_path_to_module(file_path: pathlib.Path) -> ModuleType:
    """Converts a file path to a Python module"""
    spec = importlib.util.spec_from_file_location(file_path.name, str(file_path))
    module = importlib.util.module_from_spec(spec)  # type: ignore
    spec.loader.exec_module(module)  # type: ignore
    return module


def all_solution_file_paths() -> List[pathlib.Path]:
    """
    Collects all the solution file paths in the Project Euler directory.

    This function iterates over all the directories in the Project Euler directory
    and extracts all solution files.

    Returns:
        A list of pathlib.Path instances representing the file paths of all solution files.
    """
    euler_content = PROJECT_EULER_DIR_PATH.iterdir()
    solution_dirs = filter(
        lambda p: p.is_dir() and not p.name.startswith("_"), euler_content
    )

    solution_file_paths = []
    for dir_path in solution_dirs:
        solution_file_paths.extend(extract_solution_file_paths_in_dir(dir_path))

    return solution_file_paths


def get_files_url() -> str:
    """Return the pull request number which triggered this action."""
    with open(os.environ["GITHUB_EVENT_PATH"]) as file:
        event = json.load(file)
    return event["pull_request"]["url"] + "/files"

def is_valid_solution_file(file_path: pathlib.Path) -> bool:
    """
    Checks if a path represents a valid solution file.

    Args:
        file_path: A pathlib.Path instance representing a file path.

    Returns:
        True if the path is a valid solution file, else False.
    """
    return file_path.suffix == ".py" and not file_path.name.startswith(("_", "test"))


def extract_solution_file_paths_in_dir(dir_path: pathlib.Path) -> List[pathlib.Path]:
    """
    Extracts all the solution file paths in a directory.

    Args:
        dir_path: A pathlib.Path instance representing a directory path.

    Returns:
        A list of pathlib.Path instances representing the file paths of all solution files in the directory.
    """
    dir_content = dir_path.iterdir()
    solution_files = filter(is_valid_solution_file, dir_content)
    return list(solution_files)


def added_solution_file_path() -> list[pathlib.Path]:
    """Collects only the solution file path which got added in the current
    pull request.

    This will only be triggered if the script is ran from GitHub Actions.
    """
    solution_file_paths = []
    headers = {
        "Accept": "application/vnd.github.v3+json",
        "Authorization": "token " + os.environ["GITHUB_TOKEN"],
    }
    files = requests.get(get_files_url(), headers=headers).json()
    for file in files:
        filepath = pathlib.Path.cwd().joinpath(file["filename"])
        if (
            filepath.suffix != ".py"
            or filepath.name.startswith(("_", "test"))
            or not filepath.name.startswith("sol")
        ):
            continue
        solution_file_paths.append(filepath)
    return solution_file_paths


def collect_solution_file_paths() -> list[pathlib.Path]:
    if os.environ.get("CI") and os.environ.get("GITHUB_EVENT_NAME") == "pull_request":
        # Return only if there are any, otherwise default to all solutions
        if filepaths := added_solution_file_path():
            return filepaths
    return all_solution_file_paths()


@pytest.mark.parametrize(
    "solution_path",
    collect_solution_file_paths(),
    ids=lambda path: f"{path.parent.name}/{path.name}",
)
def test_project_euler(solution_path: pathlib.Path) -> None:
    """Testing for all Project Euler solutions"""
    # problem_[extract this part] and pad it with zeroes for width 3
    problem_number: str = solution_path.parent.name[8:].zfill(3)
    expected: str = PROBLEM_ANSWERS[problem_number]
    solution_module = convert_path_to_module(solution_path)
    answer = str(solution_module.solution())  # type: ignore
    answer = hashlib.sha256(answer.encode()).hexdigest()
    assert (
        answer == expected
    ), f"Expected solution to {problem_number} to have hash {expected}, got {answer}"
