import pytest
from calculator import add, subtract  # example functions

def test_add():
    assert add(1, 2) == 3

def test_subtract():
    assert subtract(5, 3) == 2
