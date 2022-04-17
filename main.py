from math import sqrt


def fibonacci_recursion(n):
    """
    Classic solution, recursion overflow possible

    :param n: int - length
    :return: int - result
    """

    if n in (0, 1):
        return n

    if n >= 0:
        return fibonacci_recursion(n - 1) + fibonacci_recursion(n - 2)

    return fibonacci_recursion(n + 2) - fibonacci_recursion(n + 1)


def fibonacci_classic(n):
    """
    Classic solution for test positive integers

    :param n:
    :return:
    """
    a, b = 0, 1

    for _ in range(n):
        a, b = b + a, a

    return a


def fib(n):
    """
    Binet’s formula

    :param n: int - length
    :return: int - result
    """

    root_5 = sqrt(5)
    result = (1 / root_5) * (((1 + root_5) / 2) ** n - ((1 - root_5) / 2) ** n)

    return int(result)
