import pytest
from main import first_two_dict,get_numbers_from_file,get_longest_chain, fix_chain


@pytest.fixture
def test_numbers():
    numbers = ['776543', '435689', '564543', '893422', '664477', '668713']
    return numbers


@pytest.fixture
def test_file(tmp_path):
    data = '776543\n435689\n564543\n893422\n664477\n668713'
    test_file = tmp_path / "test_numbers.txt"
    test_file.write_text(data)
    return test_file


def test_get_first_two_dict(test_numbers):
    result = first_two_dict(test_numbers)
    assert result['66'] == ['664477', '668713']
    assert result['43'] == ['435689']


def test_get_numbers_from_file(test_file):
    result = get_numbers_from_file(test_file)
    assert len(result) == 6
    assert '435689' in result


def test_get_numbers_from_error_file():
    result = get_numbers_from_file('error.txt')
    assert result == []


@pytest.mark.parametrize(
    "chain, result_fake",
    [
        ([776543, 435689, 893422], '77654356893422'),
        ([223344, 445566], '2233445566')
    ],
)
def test_fix_chain(chain, result_fake):
    answer = fix_chain(chain)
    assert answer == result_fake


def test_get_longest_chain(test_numbers):
    dict_of_two = first_two_dict(test_numbers)
    longest_chain = get_longest_chain(test_numbers, dict_of_two)
    assert len(longest_chain) == 4
    assert longest_chain[0] == '664477'
    assert longest_chain[-1] == '893422'





