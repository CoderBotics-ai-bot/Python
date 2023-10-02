#from arithmetic_analysis.newton_forward_interpolation import *
#import pytest
#
#
#def test_main_does_not_throw(monkeypatch):
#    inputs = ["2", "1 2", "1.0", "1"]
#    input_generator = (i for i in inputs)
#    monkeypatch.setattr("builtins.input", lambda _: next(input_generator))
#    assert main() is None
#
#
#def test_main_handle_empty_string(monkeypatch):
#    inputs = ["", "", "", ""]
#    input_generator = (i for i in inputs)
#    monkeypatch.setattr("builtins.input", lambda _: next(input_generator))
#    with pytest.raises(ValueError):
#        main()
#
#
#def test_main_handle_incorrect_input(monkeypatch):
#    inputs = ["abc", "1 2", "1.0", "1"]
#    input_generator = (i for i in inputs)
#    monkeypatch.setattr("builtins.input", lambda _: next(input_generator))
#    with pytest.raises(ValueError):
#        main()
#