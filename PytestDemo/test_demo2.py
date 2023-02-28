import pytest


def test_firstProgram():
    msg = "Hello"
    assert msg == "Hello"


@pytest.mark.smoke
def test_SecondCreditCard():
    a = 4
    b = 6
    assert a + 2 == 6, "Addition do not match"



def test_fixtureDemo():
    print("I will execute in fixture Demo method")
