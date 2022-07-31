import pytest
from gendiff.generate_diff import generate_diff
from gendiff.utils.Exception import NotSupportFormat, NotSupportFileSuffix


def test_generate_diff_json(data):
    json_data = data.get('json')
    expected_path = json_data.get('expected')
    file1 = json_data.get('file1')
    file2 = json_data.get('file2')
    format_ = json_data.get('format')
    with open(expected_path) as f:
        expected = f.read()

    assert expected == generate_diff(file1, file2, format_)


def test_generate_diff_json_rec(data):
    json_data = data.get('json')
    expected_path = json_data.get('expected_rec')
    file1 = json_data.get('file1_rec')
    file2 = json_data.get('file2_rec')
    format_ = json_data.get('format')
    with open(expected_path) as f:
        expected = f.read()

    assert expected == generate_diff(file1, file2, format_)


def test_generate_diff_yaml(data):
    yaml_data = data.get('yaml')
    expected_path = yaml_data.get('expected')
    file1 = yaml_data.get('file1')
    file2 = yaml_data.get('file2')
    format_ = yaml_data.get('format')
    with open(expected_path) as f:
        expected = f.read()

    assert expected == generate_diff(file1, file2, format_)


def test_generate_diff_yaml_rec(data):
    yaml_data = data.get('yaml')
    expected_path = yaml_data.get('expected_rec_plain')
    file1 = yaml_data.get('file1_rec')
    file2 = yaml_data.get('file2_rec')
    format_ = 'plain'
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
