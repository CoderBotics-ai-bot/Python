# import pytest
# 
# 
# import pytest
# from ciphers.enigma_machine2 import *
# 
# 
# def test_plugboard_with_valid_input():
#     assert _plugboard("PICTURES") == {
#         "P": "I",
#         "I": "P",
#         "C": "T",
#         "T": "C",
#         "U": "R",
#         "R": "U",
#         "E": "S",
#         "S": "E",
#     }
#     assert _plugboard("POLAND") == {
#         "P": "O",
#         "O": "P",
#         "L": "A",
#         "A": "L",
#         "N": "D",
#         "D": "N",
#     }
# 
# 
# def test_plugboard_with_empty_string():
#     assert _plugboard("") == {}
# 
# 
# def test_plugboard_with_odd_number_of_symbols():
#     with pytest.raises(Exception) as e:
#         _plugboard("POLAN")
#     assert str(e.value) == "Odd number of symbols (5)"
# 
# 
# def test_plugboard_with_non_string_input():
#     with pytest.raises(TypeError) as e:
#         _plugboard(12345)
#     assert str(e.value) == "Plugboard setting isn't type string (<class 'int'>)"
# 
# 
# def test_plugboard_with_duplicate_symbols():
#     with pytest.raises(Exception) as e:
#         _plugboard("POLLL")
#     assert str(e.value) == "Duplicate symbol (L)"
# 
# 
# def test_plugboard_with_symbols_not_in_list():
#     with pytest.raises(Exception) as e:
#         _plugboard("POL*")
#     assert str(e.value) == "'*' not in list of symbols"
# 