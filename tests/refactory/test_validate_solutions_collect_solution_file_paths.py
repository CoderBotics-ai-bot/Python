#import os
#from scripts.validate_solutions import *
#
#import pytest
#import pathlib
#
#
#def test_collect_solution_file_paths_doesnt_throw_error(monkeypatch):
#    def mock_added_solution_file_path():
#        return [pathlib.Path("path/to/solution.py")]
#
#    monkeypatch.setattr(
#        "os.environ", {"CI": "true", "GITHUB_EVENT_NAME": "pull_request"}
#    )
#    monkeypatch.setitem(os.environ, "CI", "True")
#    monkeypatch.setitem(os.environ, "GITHUB_EVENT_NAME", "pull_request")
#
#    monkeypatch.setattr(
#        "scripts.validate_solutions.added_solution_file_path",
#        mock_added_solution_file_path,
#    )
#
#    try:
#        output = collect_solution_file_paths()
#        assert output is not None, "The function output should not be None"
#    except Exception as e:
#        pytest.fail(
#            f"Function 'collect_solution_file_paths' raised {type(e).__name__} unexpectedly!"
#        )
#
#
#def test_collect_solution_file_paths_without_ci_env_var(monkeypatch):
#    def mock_all_solution_file_paths():
#        return [pathlib.Path("path/to/solution.py")]
#
#    monkeypatch.setattr(
#        "scripts.validate_solutions.all_solution_file_paths",
#        mock_all_solution_file_paths,
#    )
#
#    monkeypatch.setitem(os.environ, "CI", "False")
#    monkeypatch.setitem(os.environ, "GITHUB_EVENT_NAME", "pull_request")
#
#    output = collect_solution_file_paths()
#
#    assert isinstance(output, list), "The function output should be a list"
#    assert all(
#        isinstance(item, pathlib.Path) for item in output
#    ), "All items in the output list should be instances of 'pathlib.Path'"
#
#
#def test_collect_solution_file_paths_with_no_paths(monkeypatch):
#    def mock_added_solution_file_path():
#        return []
#
#    monkeypatch.setattr(
#        "os.environ", {"CI": "true", "GITHUB_EVENT_NAME": "pull_request"}
#    )
#    monkeypatch.setitem(os.environ, "CI", "True")
#    monkeypatch.setitem(os.environ, "GITHUB_EVENT_NAME", "pull_request")
#
#    monkeypatch.setattr(
#        "scripts.validate_solutions.added_solution_file_path",
#        mock_added_solution_file_path,
#    )
#
#    output = collect_solution_file_paths()
#
#    assert output == [], "The output list should be empty"
#