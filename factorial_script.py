"""Скрипт вычисления факториала (задание 1875, PEP 8 + Git).

Простой скрипт, оформленный по стандартам PEP 8:
snake_case для имён, docstring, защита точки входа.
"""


def factorial(n):
    """Возвращает факториал неотрицательного целого числа n."""
    if n < 0:
        raise ValueError("факториал определён только для n >= 0")
    result = 1
    for i in range(2, n + 1):
        result = result * i
    return result


def main():
    """Печатает факториалы чисел от 0 до 7."""
    for number in range(8):
        print(str(number) + "! =", factorial(number))


if __name__ == "__main__":
    main()
