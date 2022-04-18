import pytest
import os

weekdays1 = ['mon', 'tue', 'wed']
weekdays2 = ['fri', 'sat', 'sun']
filename = "file.txt"


@pytest.fixture
def setup01():
    print("\n In setup01: Starting")
    weekdays1.append('thur')
    yield weekdays1
    print("\n In setup01: After yield")
    weekdays1.pop()


@pytest.fixture
def setup02():
    print("\n In setup02: Starting")
    weekdays2.insert(0, 'thur')
    yield weekdays2
    print("\n In setup02: After yield")
    weekdays1.pop()


@pytest.fixture
def setup03():
    f = open(filename, 'w')
    f.write("Hello world!")
    f.close()
    f = open(filename, 'r+')
    yield f
    os.remove(filename)


def test_extend_list(setup01):
    setup01.extend(weekdays2)
    assert setup01 == ['mon', 'tue', 'wed', 'thur', 'fri', 'sat', 'sun']


def test_len(setup01, setup02):
    assert len(weekdays1 + setup02) == len(setup01 + weekdays2)


def test_testfile(setup03):
    assert setup03.readline() == "Hello world!"
