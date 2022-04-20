from main import fib
# from main import fibonacci_classic as fib
from main import fibonacci_classic
# from main import fibonacci_recursion as fib


def test0():
    assert fib(0) == 0


def test1():
    assert fib(1) == 1


def test2():
    assert fib(2) == 1


def test3():
    assert fib(3) == 2


def test4():
    assert fib(4) == 3


def test5():
    assert fib(5) == 5


def test71():
    assert fib(71) == 308061521170129


def test72():
    assert fib(72) == 498454011879264


def test1000():
    assert fib(1000) == fibonacci_classic(1000)


def test_neg6():
    assert fib(-6) == -8


def test_neg85():
    assert fib(-85) == 259695496911122585


def test_compare_with_classic_solution():
    for number in range(100):
        assert fib(number) == fibonacci_classic(number)


def test_negative_compare_with_classic_solution():
    for number in range(-100, 0):
        assert fib(number) == fibonacci_classic(number)
