from maths.pollard_rho import *


import pytest
import pytest


def test_pollard_rho():
    assert pollard_rho(18446744073709551617) == 274177
    assert pollard_rho(97546105601219326301) == 9876543191
    assert pollard_rho(100) == 2
    assert pollard_rho(17) is None
    assert pollard_rho(17**3) == 17
    assert pollard_rho(17**3, attempts=1) is None
    assert pollard_rho(3 * 5 * 7) == 21
    with pytest.raises(ValueError):
        pollard_rho(1)
