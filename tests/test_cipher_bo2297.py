import pytest
from cipher_bo2297.cipher_func import cipher

def test_cipher_negative():
    actual=cipher("bengusu", -1, encrypt=True)
    assert actual == "admftrt"