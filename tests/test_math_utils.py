import allure
import pytest

from src.math_utils import multiply

pytestmark = [
    allure.parent_suite("Тестирование собственных функций"),
    allure.suite("Тестирвоание калькулятора"),
]


@pytest.mark.parametrize(
    ("num1", "num2", "result"), [(2, 2, 4), (3, 5, 15), (-3, 5, -15), (-3, -5, 15)]
)
@allure.title("Проверка умножения чисел")
def test_multiply(num1, num2, result):
    assert multiply(num1, num2) == result, "функция отработала не правильно"
