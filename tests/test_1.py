#teardown

import pytest

def add(a, b):
    return a + b


def test_add_1():
    assert add(1, 2) == 3
    assert add(2, 3) == 5


def test_add_2():
    assert add(-1, 1) == 0
    assert add(0, 0) == 0



@pytest.fixture
def db_connection():
    connection = {'connected': True}
    yield connection # Pro
    connection['connected'] = False

def test_db_connection(db_connection):
    assert db_connection['connected'] == True




@pytest.mark.parametrize("a, b, expected", [
    (2, 3 ,5),
    (1, 1, 2),
    (0, 0 ,3),
    (-1, -1, -2)
])
def test_add_3(a, b, expected):
    assert add(a, b) == expected
