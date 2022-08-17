import pytest
from gendiff.generate_diff import generate_diff
from gendiff.utils.exception import NotSupportedFormatError
from gendiff.utils.exception import NotSupportedFileSuffixError
from tests.conftest import get_path_to_test_data


@pytest.mark.parametrize(
    'first_file_path,second_file_path,expected,format_',
    [
        (
            get_path_to_test_data('file1.json'),
            get_path_to_test_data('file2.json'),
            get_path_to_test_data('stylish_result.txt'),
            'stylish'
        ),
        (
            get_path_to_test_data('file1_nested.json'),
            get_path_to_test_data('file2_nested.json'),
            get_path_to_test_data('plain_result_nested.txt'),
            'plain'
        ),
        (
            get_path_to_test_data('file1.yml'),
            get_path_to_test_data('file2.yaml'),
            get_path_to_test_data('stylish_result.txt'),
            'stylish'
        ),
        (
            get_path_to_test_data('file1_nested.yml'),
            get_path_to_test_data('file2_nested.yml'),
            get_path_to_test_data('json_result_nested.txt'),
            'json'
        ),
        (
            get_path_to_test_data('file1.json'),
            get_path_to_test_data('file2.yaml'),
            get_path_to_test_data('stylish_result.txt'),
            'stylish'
        ),
        (
            get_path_to_test_data('file1_nested.json'),
            get_path_to_test_data('file2_nested.yml'),
            get_path_to_test_data('stylish_result_nested.txt'),
            'stylish'
        ),
        (
            get_path_to_test_data('file1_nested.json'),
            get_path_to_test_data('file2_nested.yml'),
            get_path_to_test_data('stylish_result_nested.txt'),
            'stylish'
        )
    ]
)
def test_generate_diff(first_file_path, second_file_path, expected, format_):
    with open(expected) as f:
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
