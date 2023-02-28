#Any pytest file should start with test_ or end with _test
#pytest method names should start with test
#Any code should be wrapped in method only
#Method name should have sense
#-k stands for method names execution, -s
# You can mark test with @pytest.mark.smoke tag and then run with -m
#You can skip test with @pytest.mark.skip
#fixtures are used for setup and tear down methods for test cases - confest file to generalise fixture and make it available to all test cases
#data driven and paramaterization can be done with the return statements with tuple format
#When you define fixture scope to class only,it will run before class is initiated
import pytest


#@pytest.mark.smoke
def test_firstProgram():
    print("Hello")

def test_CreditCard():
    print("Good Morning")


def test_crossBrowser(crossBrowser):
    print(crossBrowser)
  #  print(crossBrowser[0])