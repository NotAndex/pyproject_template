from transformation_1.step_1 import addition
from transformation_2.step_1 import subtraction


def test_subtraction():
    assert subtraction(2, 2) == 0


def test_addition():
    assert addition(2, 2) == 4
