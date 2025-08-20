import allure


@allure.step("Умножение двух чисел")
def multiply(a: int, b: int) -> int:
    return a * b
