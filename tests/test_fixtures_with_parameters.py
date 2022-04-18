import pytest


@pytest.fixture(params=[(3, 4), [3, 5]], ids=['TUPLE', 'LIST'])
def fixture01(request):
    return request.param


@pytest.fixture(params=["a", "b"])
def fixture02(request):
    return request.param


def test_fixture_params(fixture01):
    print(type(fixture01))
    assert 1 == 1


def test_fixture_params_2(fixture01, fixture02):
    print(type(fixture01))
    assert 1 == 1