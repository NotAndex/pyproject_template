from module_a.simple_math import add, sub


def test_subtraction():
    assert sub(2, 2) == 0


def test_addition():
    assert add(2, 2) == 4
