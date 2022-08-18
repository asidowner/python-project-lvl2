import pytest
from gendiff.generate_diff import generate_diff
from gendiff.utils.exception import NotSupportedFormatError
from gendiff.utils.exception import NotSupportedFileSuffixError
from tests.conftest import get_path_to_test_data


@pytest.mark.parametrize(
    'first_file_name,second_file_name,expected_file_name,format_',
    [
        (
            'file1.json',
            'file2.json',
            'stylish_result.txt',
            'stylish'
        ),
        (
            'file1_nested.json',
            'file2_nested.json',
            'plain_result_nested.txt',
            'plain'
        ),
        (
            'file1.yml',
            'file2.yaml',
            'stylish_result.txt',
            'stylish'
        ),
        (
            'file1_nested.yml',
            'file2_nested.yml',
            'json_result_nested.txt',
            'json'
        ),
        (
            'file1.json',
            'file2.yaml',
            'stylish_result.txt',
            'stylish'
        ),
        (
            'file1_nested.json',
            'file2_nested.yml',
            'stylish_result_nested.txt',
            'stylish'
        ),
        (
            'file1_nested.json',
            'file2_nested.yml',
            'stylish_result_nested.txt',
            'stylish'
        )
    ]
)
def test_generate_diff(first_file_name,
                       second_file_name,
                       expected_file_name,
                       format_):
    expected_path = get_path_to_test_data(expected_file_name)
    first_file_path = get_path_to_test_data(first_file_name)
    second_file_path = get_path_to_test_data(second_file_name)

    with open(expected_path) as f:
        assert generate_diff(first_file_path,
                             second_file_path,
                             format_) == f.read()


def test_unknown_format():
    with pytest.raises(NotSupportedFormatError) as errmsg:
        generate_diff(get_path_to_test_data('file1.yml'),
                      get_path_to_test_data('file2.yaml'),
                      'asdsdg')

        assert 'Unknown format, try gendiff -h' == str(errmsg.value)


def test_bad_path():
    wrong_path = 'asd/asdvzxcv/asf'
    with pytest.raises(FileNotFoundError) as errmsg:
        generate_diff('asd/asdvzxcv/asf',
                      get_path_to_test_data('file2.yaml'),
                      'stylish')
        assert f'Check your file path: {wrong_path}' == str(errmsg.value)


def test_bad_suffix():
    with pytest.raises(NotSupportedFileSuffixError):
        generate_diff(get_path_to_test_data('file1_nested.txt'),
                      get_path_to_test_data('file2.yaml'),
                      'stylish')
