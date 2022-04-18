import pytest


def test_1(setup01):
    print(setup01)


def test_del_item(setup01):
    del setup01[-1]
    assert setup01 == pytest.weekdays1


def test_request(setup04):
    assert 1 == 1
