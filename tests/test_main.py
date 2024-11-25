import pytest
from main import first_two_dict,get_numbers_from_file,get_longest_chain

@pytest.fixture
def test_numbers():
    numbers = ['776543', '435689', '564543', '893422', '664477', '668713']
    return numbers


def test_get_first_two_dict(test_numbers):
    result = first_two_dict(test_numbers)
    assert result['66'] == ['664477', '668713']
    assert result['43'] == ['435689']

