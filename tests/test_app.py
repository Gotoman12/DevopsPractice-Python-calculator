import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import app as calc

def test_addition():
    assert 2 + 3 == 5

def test_subtraction():
    assert 5 - 3 == 2

def test_multiplication():
    assert 2 * 4 == 8

def test_division():
    assert 10 / 2 == 5
