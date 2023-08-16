# import pytest
# from matrix.spiral_print import *
# 
# 
# def test_spiral_print_clockwise_square_matrix():
#     old_stdout = sys.stdout
#     sys.stdout = mystdout = StringIO()
# 
#     spiral_print_clockwise(
#         [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
#     )
#     sys.stdout = old_stdout
#     output = mystdout.getvalue()
# 
#     assert output == "1\n2\n3\n4\n8\n12\n16\n15\n14\n13\n9\n5\n6\n7\n11\n10\n"
# 
# 
# def test_spiral_print_clockwise_single_row():
#     old_stdout = sys.stdout
#     sys.stdout = mystdout = StringIO()
# 
#     spiral_print_clockwise([[1, 2, 3, 4]])
#     sys.stdout = old_stdout
#     output = mystdout.getvalue()
# 
#     assert output == "1\n2\n3\n4\n"
# 
# 
# def test_spiral_print_clockwise_single_cell():
#     old_stdout = sys.stdout
#     sys.stdout = mystdout = StringIO()
# 
#     spiral_print_clockwise([[1]])
#     sys.stdout = old_stdout
#     output = mystdout.getvalue()
# 
#     assert output == "1\n"
# 