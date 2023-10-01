from matrix.nth_fibonacci_using_matrix_exponentiation import *
import pytest


def test_main(capfd):
    main()
    out, err = capfd.readouterr()
    assert out is not None
    assert err == ""
