import pytest

from transformation_2.step_1 import subtraction

def test_subtraction():
    assert subtraction(2,2) is 0
    assert subtraction(4,2) is 1