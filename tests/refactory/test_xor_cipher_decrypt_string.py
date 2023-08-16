import pytest
from ciphers.xor_cipher import *


def test_decrypt_string():
    xor_cipher = XORCipher(key=120)
    encrypted_content = "".join(chr(ord(ch) ^ 120) for ch in "test string")
    assert xor_cipher.decrypt_string(encrypted_content, key=120) == "test string"


def test_decrypt_string_no_key():
    xor_cipher = XORCipher()
    encrypted_content = "".join(
        chr(ord(ch) ^ 1) for ch in "test string"
    )  # If no key is passed, key defaults to 1
    assert xor_cipher.decrypt_string(encrypted_content) == "test string"


def test_decrypt_string_zero_key():
    xor_cipher = XORCipher(key=0)
    encrypted_content = "".join(
        chr(ord(ch) ^ 1) for ch in "test string"
    )  # If key is 0, key defaults to 1
    assert xor_cipher.decrypt_string(encrypted_content, key=0) == "test string"


def test_decrypt_string_large_key():
    xor_cipher = XORCipher(key=10240)
    encrypted_content = "".join(
        chr(ord(ch) ^ (10240 % 255)) for ch in "test string"
    )  # Key is reduced modulo 255 until it's less than 255
    assert xor_cipher.decrypt_string(encrypted_content, key=10240) == "test string"


def test_decrypt_string_assertion_error():
    xor_cipher = XORCipher(key=10240)
    with pytest.raises(AssertionError):
        xor_cipher.decrypt_string(content="test string", key="10240")  # key is a string
