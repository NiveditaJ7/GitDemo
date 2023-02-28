import pytest


@pytest.mark.usefixtures("setup")
class TestExample:
    def test_fixtureDemo(self):
        print("I will excute in FixtureDemo method")
    def test_fixtureDemo1(self):
        print("I will execute in FixtureDemo1 method ")
    def test_fixtureDemo2(self):
         print("I will execute in fixtureDemo3 method")  