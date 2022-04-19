import pytest
from utils.util import get_data


@pytest.mark.parametrize("id, name, course, city", get_data())
def test_with_data_provider(id, name, course, city):
    print(f'{id}, {name}, {course}, {city}')
    assert 1 == 1
