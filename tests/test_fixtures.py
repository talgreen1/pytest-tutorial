import pytest

weekdays1 = ['mon', 'tue', 'wed']
weekdays2 = ['fri', 'sat', 'sun']


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


# def test_extend_list(setup01):
#     setup01.extend(weekdays2)
#     assert setup01 == ['mon', 'tue', 'wed', 'thur', 'fri', 'sat', 'sun']


def test_len(setup01, setup02):
    assert len(weekdays1 + setup02) == len(setup01 + weekdays2)
