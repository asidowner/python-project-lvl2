import pytest
from gendiff.generate_diff import generate_diff
from gendiff.utils.exception import NotSupportedFormatError, NotSupportedFileSuffixError


def test_generate_diff_json(first_file_json, second_file_json, stylish_expected):
    assert stylish_expected == generate_diff(first_file_json, second_file_json, 'stylish')


def test_generate_diff_json_rec(first_file_rec_json, second_file_rec_json, stylish_rec_expected):
    assert stylish_rec_expected == generate_diff(first_file_rec_json, second_file_rec_json, 'stylish')


def test_generate_diff_yaml(first_file_yaml, second_file_yaml, stylish_expected):
    assert stylish_expected == generate_diff(first_file_yaml, second_file_yaml, 'stylish')


def test_generate_diff_yaml_rec(first_file_rec_yaml, second_file_rec_yaml, plain_rec_expected):
    assert plain_rec_expected == generate_diff(first_file_rec_yaml, second_file_rec_yaml, 'plain')


def test_generate_diff_as_json(first_file_rec_yaml, second_file_rec_json, json_rec_expected):
    assert json_rec_expected == generate_diff(first_file_rec_yaml, second_file_rec_json, 'json')


def test_unknown_format(first_file_json, second_file_yaml):
    with pytest.raises(NotSupportedFormatError) as errmsg:
        generate_diff(first_file_json, second_file_yaml, 'asdsdg')

        assert 'Unknown format, try gendiff -h' == str(errmsg.value)


def test_bad_path(second_file_yaml):
    wrong_path = 'asd/asdvzxcv/asf'
    with pytest.raises(FileNotFoundError) as errmsg:
        generate_diff('asd/asdvzxcv/asf', second_file_yaml, 'stylish')

        assert f'Check your file path: {wrong_path}' == str(errmsg.value)


def test_bad_suffix(wrong_suffix, second_file_yaml):
    with pytest.raises(NotSupportedFileSuffixError):
        generate_diff(wrong_suffix, second_file_yaml, 'stylish')
