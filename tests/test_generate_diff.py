import os
import pytest
from gendiff.generate_diff import generate_diff
from gendiff.utils.Exception import NotSupportFormat, NotSupportFileSuffix


@pytest.fixture
def data():
    return {
        'json': {
            'file1': os.path.join('tests', 'fixtures', 'file1.json'),
            'file2': os.path.join('tests', 'fixtures', 'file2.json'),
            'wrong_path': os.path.join('tests', 'fixtures', 'wrong_path'),
            'expected': os.path.join('tests', 'fixtures', 'stylish_result_json.txt'),
            'format': 'stylish'
        }
    }


def test_generate_diff(data):
    json_data = data.get('json')
    expected_path = json_data.get('expected')
    file1 = json_data.get('file1')
    file2 = json_data.get('file2')
    format_ = json_data.get('format')
    with open(expected_path) as f:
        expected = f.read()

    assert expected == generate_diff(file1, file2, format_)


def test_unknown_format(data):
    json_data = data.get('json')
    file1 = json_data.get('file1')
    file2 = json_data.get('file2')

    with pytest.raises(NotSupportFormat) as errmsg:
        generate_diff(file1, file2, 'asdsdg')

        assert 'Unknown format, try gendiff -h' == str(errmsg.value)


def test_bad_path(data):
    json_data = data.get('json')
    file1 = json_data.get('wrong_path')
    file2 = json_data.get('file2')
    format_ = json_data.get('format')

    with pytest.raises(FileNotFoundError) as errmsg:
        generate_diff(file1, file2, format_)

        assert f'Check your file path: {file1}' == str(errmsg.value)


def test_bad_suffix(data):
    json_data = data.get('json')
    file1 = json_data.get('expected')
    file2 = json_data.get('file2')
    format_ = json_data.get('format')

    with pytest.raises(NotSupportFileSuffix) as errmsg:
        generate_diff(file1, file2, format_)