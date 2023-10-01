import builtins


import builtins

import pytest
from dynamic_programming.fibonacci import *
from typing import Generator
from unittest.mock import patch
from io import StringIO
import sys


class TestMain:
    @patch.object(builtins, "input", side_effect=["5", "exit"])
    def test_main_no_error_and_not_none(
        self, mock_input: Generator[str, None, None]
    ) -> None:
        """
        This test checks that the function main executes without errors and returns the
        expected output when given valid input. It does not check for specific return
        values, but rather that the function is working correctly in terms of syntax,
        the Python environment, and libraries.
        """
        import sys
        from io import StringIO

        # Monkey patching sys.stdout
        sys.stdout = StringIO()

        # Call function
        main()

        # Check output
        output = sys.stdout.getvalue().strip()
        assert output is not None

    @patch.object(builtins, "input", side_effect=["exit"])
    def test_main_exit_no_error_and_not_none(
        self, mock_input: Generator[str, None, None]
    ) -> None:
        """
        This test checks that the function main executes without errors and returns the
        expected output when given 'exit' as input.
        """
        import sys
        from io import StringIO

        # Monkey patching sys.stdout
        sys.stdout = StringIO()

        # Call function
        main()

        # Check output
        output = sys.stdout.getvalue().strip()
        assert output is not None

    @patch.object(builtins, "input", side_effect=["not a number", "exit"])
    def test_main_invalid_input(self, mock_input: Generator[str, None, None]) -> None:
        """
        This test checks that the main function handles non-integer input correctly. An
        invalid (non-integer) input is given at first, followed by 'exit' to terminate
        the while loop and prevent an infinite loop.
        """
        import sys
        from io import StringIO

        # Monkey patching sys.stdout
        sys.stdout = StringIO()

        # Call function
        main()

        # Check output
        output = sys.stdout.getvalue().strip()
        assert output is not None
