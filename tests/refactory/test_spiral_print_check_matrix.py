# import pytest
# 
# 
# from typing import Any, List
# 
# import pytest
# from matrix.spiral_print import *
# 
# 
# @pytest.mark.parametrize(
#     "matrix, expected",
#     [
#         ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], True),  # valid matrix
#         ([[1]], True),  # single element matrix
#         ([[], [], []], True),  # valid matrix but empty rows
#         (
#             [[1, 2, 3], ["foo", "bar", "baz"], [7, 8, 9]],
#             False,
#         ),  # invalid matrix, different types in the rows
#     ],
# )
# def test_check_matrix(matrix: List[List[Any]], expected: bool):
#     assert check_matrix(matrix) == expected
# 