#from contextlib import redirect_stdout
#
#import pytest
#import os
#
#
#import os
#from io import StringIO
#from scripts.build_directory_md import *
#
#
#@pytest.fixture
#def mock_files_in_directory():
#    return [
#        {"filepath": ".", "filename": "file1.py"},
#        {"filepath": "sub_directory", "filename": "file2.py"},
#    ]
#
#
#@pytest.fixture
#def mock_good_file_paths(monkeypatch, mock_files_in_directory):
#    def mock_func(*args, **kwargs):
#        for file in mock_files_in_directory:
#            yield os.path.join(file["filepath"], file["filename"])
#
#    monkeypatch.setattr("scripts.build_directory_md.good_file_paths", mock_func)
#
#
#def test_print_directory_md_no_exception(mock_good_file_paths):
#    with redirect_stdout(StringIO()) as output:
#        print_directory_md()
#        assert output.getvalue() != ""
#
#
#def test_print_directory_md_prints_correct_output(mock_good_file_paths):
#    with redirect_stdout(StringIO()) as output:
#        print_directory_md()
#        lines = output.getvalue().split("\n")
#        assert "[File1](./File1.Py)" in lines
#        assert "## [File2](Sub_Directory/File2.Py)" in lines
#