from main import fib


def test1():
    assert fib(0) == 0


def test2():
    assert fib(1) == 1


def test3():
    assert fib(2) == 1


def test4():
    assert fib(3) == 2


def test5():
    assert fib(4) == 3


def test6():
    assert fib(5) == 5


def test7():
    result = 43466557686937456435688527675040625802564660517371780402481729089536555417949051890403879840079255169295922593080322634775209689623239873322471161642996440906533187938298969649928516003704476137795166849228875
    assert fib(1000) == result


def test_neg1():
    assert fib(-6) == -8
