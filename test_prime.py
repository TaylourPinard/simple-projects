'''
    Unit tests for prime.py
'''

from prime import is_prime
import pytest

def test_prime():
    assert is_prime(7) == "7 is prime"
    assert is_prime(13) == "13 is prime"

def test_zero_and_one():
    assert is_prime(0) == "0 is prime"
    assert is_prime(1) == "1 is prime"

def test_not_prime():
    assert is_prime(4) == "Not prime"
    assert is_prime(12) == "Not prime"

def test_invalid_input():
    assert is_prime("cat") == "Bad input"
    
def test_negative():
    with pytest.raises(ValueError):
        is_prime(-1)
        is_prime(-20)