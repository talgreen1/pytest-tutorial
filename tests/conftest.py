import os

import pytest

weekdays1 = ['mon', 'tue', 'wed']
weekdays2 = ['fri', 'sat', 'sun']
filename = "file.txt"


def pytest_configure():
    pytest.weekdays1 = ['mon', 'tue', 'wed']
    pytest.weekdays2 = ['fri', 'sat', 'sun']


@pytest.fixture
def setup01():
    print("\n In setup01: Starting")
    wk = pytest.weekdays1.copy()
    wk.append('thur')
    yield wk
    print("\n In setup01: After yield")


@pytest.fixture
def setup02():
    print("\n In setup02: Starting")
    wk2 = pytest.weekdays2.copy()
    wk2.insert(0, 'thur')
    yield wk2
    print("\n In setup02: After yield")


@pytest.fixture
def setup03():
    f = open(filename, 'w')
    f.write("Hello world!")
    f.close()
    f = open(filename, 'r+')
    yield f
    os.remove(filename)

@pytest.fixture()
def setup04(request):
    print ("\n In Setup04\n")
    print ('\n Fixture score: ' + request.scope)
    print ('\n Calling function: ' + request.function.__name__)