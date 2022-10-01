import pytest

from transformation_2.step_1 import subtraction
from transformation_1.step_1 import addition


def test_subtraction():
    assert subtraction(2,2) is 1

def test_addition():
    assert addition(2,2) is 3