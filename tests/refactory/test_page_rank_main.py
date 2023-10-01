from graphs.page_rank import *

import pytest
import pytest


from unittest.mock import patch


def test_main_no_exception():
    with patch(
        "builtins.input", side_effect=["Node1 Node2 Node3", "1 0 0\n0 1 0\n0 0 1"]
    ):
        try:
            main()
        except Exception as e:
            pytest.fail(f"main() function threw an exception: {e}")


def test_main_invalid_graph_input():
    with patch(
        "builtins.input", side_effect=["Node1 Node2 Node3", "1 0\n0 1 0\n0 0 1"]
    ):
        try:
            main()
        except Exception as e:
            pytest.fail(f"main() function threw an exception: {e}")
