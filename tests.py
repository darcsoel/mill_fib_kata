from main import fib, fibonacci_classic
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
    result = 43466557686937456435688527675040625802564660517371780402481729089536555417949051890403879840079255169295922593080322634775209689623239873322471161642996440906533187938298969649928516003704476137795166849228875
    assert fib(1000) == result


def test_neg6():
    assert fib(-6) == -8


def test_compare_with_classic_solution():
    for number in range(100):
        assert fib(number) == fibonacci_classic(number)
