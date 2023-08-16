# 
# import pytest
# from typing import Tuple
# from ciphers.enigma_machine2 import *
# 
# # Test data
# ROTOR1 = "TOHXPIEZSLBCJUVARNDKQGMWFY"
# ROTOR2 = "VOLZAEKFBYITUJMXDQHRCSWNPG"
# ROTOR3 = "JDZNRBAYVOFLICXMUTKPSETGHQ"
# 
# 
# @pytest.fixture
# def setup_data() -> Tuple[str, Tuple[int, int, int], Tuple[str, str, str], str]:
#     text = "HELLO WORLD!"
#     rotor_position = (1, 2, 1)
#     rotor_selection = (ROTOR1, ROTOR2, ROTOR3)
#     plugb = "pictures"
#     return text, rotor_position, rotor_selection, plugb
# 
# 
# def test_enigma_with_valid_data(setup_data):
#     text, rotor_position, rotor_selection, plugb = setup_data
#     expected_result = "CPROF DVBZA!"
#     assert enigma(text, rotor_position, rotor_selection, plugb) == expected_result
# 
# 
# def test_enigma_with_lower_case_text(setup_data):
#     text, rotor_position, rotor_selection, plugb = setup_data
#     text = text.lower()
#     expected_result = "CPROF DVBZA!"
#     assert enigma(text, rotor_position, rotor_selection, plugb) == expected_result
# 
# 
# def test_enigma_with_special_characters_in_text(setup_data):
#     text, rotor_position, rotor_selection, plugb = setup_data
#     text = "@#$%HELLO WORLD!^&*()"
#     expected_result = "@#$%CPROF DVBZA!^&*()"
#     assert enigma(text, rotor_position, rotor_selection, plugb) == expected_result
# 
# 
# def test_enigma_with_numeric_characters_in_text(setup_data):
#     text, rotor_position, rotor_selection, plugb = setup_data
#     text = "123HELLO WORLD!456"
#     expected_result = "123CPROF DVBZA!456"
#     assert enigma(text, rotor_position, rotor_selection, plugb) == expected_result
# 
# 
# def test_enigma_with_invalid_rotor_position(setup_data):
#     text, _, rotor_selection, plugb = setup_data
#     rotor_position = (27, 1, 1)  # Rotor position value out of range
#     with pytest.raises(ValueError):
#         enigma(text, rotor_position, rotor_selection, plugb)
# 