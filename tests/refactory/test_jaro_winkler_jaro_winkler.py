import pytest
from strings.jaro_winkler import *


def test_jaro_winkler():
    # Test 1: Check with strings that only have transpositions
    assert abs(jaro_winkler("martha", "marhta") - 0.9611111111111111) < 1e-9

    # Test 2: Check with strings having same characters but different order
    assert abs(jaro_winkler("CRATE", "TRACE") - 0.7333333333333334) < 1e-9

    # Test 3: Check with totally different strings
    assert abs(jaro_winkler("test", "dbdbdbdb") - 0.0) < 1e-9

    # Test 4: Check with exactly same strings
    assert abs(jaro_winkler("test", "test") - 1.0) < 1e-9

    # Test 5: Check with strings having same text but different case and character replacements
    assert abs(jaro_winkler("hello world", "HeLLo W0rlD") - 0.6363636363636364) < 1e-9

    # Test 6: Check with one empty string
    assert abs(jaro_winkler("test", "") - 0.0) < 1e-9

    # Test 7: Check with totally different words
    assert abs(jaro_winkler("hello", "world") - 0.4666666666666666) < 1e-9

    # Test 8: Check with strings including symbols
    assert abs(jaro_winkler("hell**o", "*world") - 0.4365079365079365) < 1e-9
