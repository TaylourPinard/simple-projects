'''
    unit testing for fib.py
'''

from fib import fib
import pytest

def test_invalid_input():
    with pytest.raises(TypeError):
        fib("cat")
    with pytest.raises(ValueError):
        fib(-1)
        fib(1)

def test_correct():
    assert fib(12) == [0, 1, 1, 2, 3, 5, 8]
    assert fib(20) == [0, 1, 1, 2, 3, 5, 8, 13]