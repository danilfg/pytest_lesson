from src.math_utils import multiply


def test_basic_math():
    assert 2 * 2 == 4

def test_multiply():
    assert multiply(3, 5) == 15, "функция отработала не правильно"

def test_multiple_negative():
    assert multiply(-3, 5) == -15, "функция отработала не правильно"