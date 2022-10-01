import pytest

from transformation_1.step_1 import addition

def test_addition():
    assert addition(2,2) is 4