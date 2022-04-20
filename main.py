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

    if n >= 0:
        for _ in range(n):
            a, b = b + a, a
    else:
        for _ in range(abs(n)):
            a, b = b - a, a

    return a


def fibonacci_binet(n):
    """
    Binet’s formula

    Need some check, not all values round correct

    :param n: int - length
    :return: int - result
    """

    root_5 = sqrt(5)
    result = (1 / root_5) * (((1 + root_5) / 2) ** n - ((1 - root_5) / 2) ** n)

    return round(result)


def fib(n):
    """
    Computes fib(n) iteratively using fast doubling method
    """

    sign = n >= 0
    n = abs(n)

    bin_of_n = bin(n)[2:]
    f = [0, 1]

    for b in bin_of_n:
        f2i1 = f[1] ** 2 + f[0] ** 2
        f2i = f[0] * (2 * f[1] - f[0])

        if b == '0':
            f[0], f[1] = f2i, f2i1
        else:
            f[0], f[1] = f2i1, f2i1 + f2i

    if sign:
        return f[0]
    elif n % 2:
        return f[0]
    else:
        return f[0] * -1
