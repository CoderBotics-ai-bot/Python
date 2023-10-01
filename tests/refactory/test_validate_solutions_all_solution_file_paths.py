#
#import pytest
#import pytest
#
#
#import pathlib
#from scripts.validate_solutions import *
#
#
#@pytest.fixture
#def mock_files_structure(tmp_path: pathlib.Path) -> pathlib.Path:
#    main_dir = tmp_path / "main_directory"
#    main_dir.mkdir()
#
#    directories = ["_dir", "dir1", "dir2"]
#    files = [
#        (("_file.py", "file.py", "test_file.py"), "_dir"),
#        (("file1.py", "_file1.py", "test_file1.py"), "dir1"),
#        (("file2.py", "_file2.py", "test_file2.py"), "dir2"),
#    ]
#
#    for dir_name in directories:
#        subdir = main_dir / dir_name
#        subdir.mkdir()
#
#        for file_tup in files:
#            if dir_name == file_tup[1]:
#                for file in file_tup[0]:
#                    (subdir / file).touch()
#
#    return main_dir
#
#
#def test_all_solution_file_paths_existence(setup_mock: None) -> None:
#    result = all_solution_file_paths()
#    assert result is not None
#
#
#def test_all_solution_file_paths_correctness(setup_mock: None) -> None:
#    result = all_solution_file_paths()
#    for res in result:
#        assert not res.name.startswith(
#            ("_", "test")
#        ), f"{res.name} starts with underscore or 'test'"
#        assert res.suffix == ".py", f"{res.name} is not a python file"
#