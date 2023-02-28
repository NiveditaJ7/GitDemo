import pytest


@pytest.fixture(scope="class")
def setup():
    print("I will execute first")
    yield
    print("I will execute last")


@pytest.fixture()
def dataLoad():
    print("user profile data is being created")
    return ["Nivedita", "Jagtap", "niveditajagtap.com"]


@pytest.fixture(params=[("chrome", "Nivedita"), ("firefox","Jagtap"), "IE"])
def crossBrowser(request):
    return request.param
