import pytest
from ciphers.xor_cipher import *


import pytest
from ciphers.xor_cipher import XORCipher


@pytest.fixture
def cipher() -> XORCipher:
    return XORCipher(key=5)


def test_decrypt(cipher: XORCipher) -> None:
    assert cipher.decrypt(["M"], 5) == ["H"]


def test_decrypt_large_key(cipher: XORCipher) -> None:
    assert cipher.decrypt(["M"], 260) == ["H"]


def test_decrypt_no_key(cipher: XORCipher) -> None:
    assert cipher.decrypt(["M"], 0) == ["H"]


def test_decrypt_empty_string(cipher: XORCipher) -> None:
    assert cipher.decrypt([], 5) == []


def test_decrypt_invalid_content(cipher: XORCipher) -> None:
    with pytest.raises(AssertionError):
        cipher.decrypt(123, 5)


def test_decrypt_invalid_key(cipher: XORCipher) -> None:
    with pytest.raises(AssertionError):
        cipher.decrypt(["M"], "invalid")


def test_decrypt_invalid_data(cipher: XORCipher) -> None:
    with pytest.raises(AssertionError):
        cipher.decrypt(123, "invalid")
