# pip install -U pytest



def func(x):
    return x + 1


def test_answer():
    assert func(3) == 5

def test_answer2():
    assert func(3) == 4


def test_answer3():
    assert func(3) == 4