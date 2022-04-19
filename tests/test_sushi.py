import pytest


def test_sushi_fixture(sushi):
    """This test will run 8 times, 1 time for each parameter that defines in the 'sushi' fixture"""
    print(sushi.name)


@pytest.mark.parametrize(
    'sushi',
    ['Kappa Maki', 'Tamagoyaki', 'Inarizushi'],
    indirect=True
)
def test_sushi_fixture_indirect(sushi):
    """This test will run only 3 times, 1 time for each parameter that defines here.
    The 3 parameters here are being used, instead of the 8 parameters in the fixture itself.
    The 'sushi' is a fixture, and the parameters are passed to it"""
    print(sushi.name)

@pytest.mark.parametrize(
    'sushi',
    ['Kappa Maki', 'Tamagoyaki', 'Inarizushi']
)
def test_sushi_fixture_no_indirect(sushi):
    """In this test, the 'sushi' is just normal paramter. It is not fixture. It is a str paramter that will get 3
    different values each time"""
    print(sushi)