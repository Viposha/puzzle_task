import pytest
from main import first_two_dict,get_numbers_from_file,get_longest_chain, fix_chain, main
from unittest.mock import patch, mock_open


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


def test_main(capsys, tmp_path):
    # Simulate the contents of numbers.txt
    data = '776543\n435689\n564543\n893422\n664477\n668713'

    # Create a temporary file
    file_path = tmp_path / "numbers.txt"
    file_path.write_text(data)

    # Mock the open() call in get_numbers_from_file
    with patch("builtins.open", mock_open(read_data=data)):
        # Run the main function
        with patch("main.get_numbers_from_file") as mock_get_numbers:
            mock_get_numbers.return_value = ['776543', '435689', '564543', '893422', '664477', '668713']

            main()

    # Capture the output
    captured = capsys.readouterr()

    # Assert statements for the output
    assert "Longest chain length: 4 numbers" in captured.out
    assert "Result: 664477654356893422" in captured.out  # Adjust based on actual result logic
    assert "There are 18 characters in result" in captured.out





