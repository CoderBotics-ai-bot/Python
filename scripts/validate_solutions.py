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


from typing import List, Dict

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

    It traverses through the directory and checks each file. If the file is a
    Python file and its name doesn't start with either underscore or "test",
    then it is considered a solution file.

    Returns:
        List[pathlib.Path]: A list of solution file paths.
    """
    solution_file_paths = [
        file_path
        for problem_dir_path in PROJECT_EULER_DIR_PATH.iterdir()
        if problem_dir_path.is_dir() and not problem_dir_path.name.startswith("_")
        for file_path in problem_dir_path.iterdir()
        if file_path.suffix == ".py" and not file_path.name.startswith(("_", "test"))
    ]
    return solution_file_paths


def get_files_url() -> str:
    """Return the pull request number which triggered this action."""
    with open(os.environ["GITHUB_EVENT_PATH"]) as file:
        event = json.load(file)
    return event["pull_request"]["url"] + "/files"

def added_solution_file_path() -> List[pathlib.Path]:
    """
    Collects the file paths of newly added solution files in the current pull request.
    The function filters only the Python files excluding the ones starting with an underscore (_) or "test".
    The function is intended to be run from GitHub Actions and requires the following environment variables:
    GITHUB_EVENT_PATH: The path of the file with the complete webhook event payload. For more information, see "GitHub Actions: Webhook events"
    GITHUB_TOKEN: GitHub automatically creates a GITHUB_TOKEN secret to use in your workflow

    Returns:
        solution_file_paths (List[pathlib.Path]): List of paths to the added solution files
    Notes:
        Only .py files are considered as solution files.
    """
    headers = get_auth_headers()
    added_files = parse_files_from_payload(get_files_url(), headers)
    return [filepath for filepath in added_files if is_solution_file(filepath)]

def collect_solution_file_paths() -> List[pathlib.Path]:
    """
    Collects the file paths of solution files.

    It collects the paths of all solution files if the environment variable CI isn't set
    or the environment variable GITHUB_EVENT_NAME isn't "pull_request". However, if these conditions
    are not met (which is typically the case in GitHub Actions environment when a pull request is made),
    it collects only the file paths of the solution files that are newly added in this pull request.

    Returns:
        list[pathlib.Path]: A list of solution file paths.
    """
    is_ci = os.environ.get("CI")
    is_pr = os.environ.get("GITHUB_EVENT_NAME") == "pull_request"
    if is_ci and is_pr:
        filepaths = added_solution_file_path()
        if filepaths:  # Guard clause to return early if filepaths exist
            return filepaths
    return all_solution_file_paths()


def get_auth_headers() -> dict:
    return {
        "Accept": "application/vnd.github.v3+json",
        "Authorization": "token " + os.environ["GITHUB_TOKEN"],
    }


def parse_files_from_payload(url: str, headers: dict) -> list:
    return requests.get(url, headers=headers).json()


def is_solution_file(file: dict) -> bool:
    filepath = pathlib.Path.cwd().joinpath(file["filename"])
    return (
        filepath.suffix == ".py"
        and not filepath.name.startswith(("_", "test"))
        and filepath.name.startswith("sol")
    )


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
