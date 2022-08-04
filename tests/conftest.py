import os
import pytest


@pytest.fixture
def first_file_json():
    return os.path.join('tests', 'fixtures', 'file1.json')


@pytest.fixture
def second_file_json():
    return os.path.join('tests', 'fixtures', 'file2.json')


@pytest.fixture
def first_file_rec_json():
    return os.path.join('tests', 'fixtures', 'file1_rec.json')


@pytest.fixture
def wrong_suffix():
    return os.path.join('tests', 'fixtures', 'file1_rec.txt')


@pytest.fixture
def second_file_rec_json():
    return os.path.join('tests', 'fixtures', 'file2_rec.json')


@pytest.fixture
def first_file_yaml():
    return os.path.join('tests', 'fixtures', 'file1.yml')


@pytest.fixture
def second_file_yaml():
    return os.path.join('tests', 'fixtures', 'file2.yaml')


@pytest.fixture
def first_file_rec_yaml():
    return os.path.join('tests', 'fixtures', 'file1_rec.yml')


@pytest.fixture
def second_file_rec_yaml():
    return os.path.join('tests', 'fixtures', 'file2_rec.yml')


@pytest.fixture
def stylish_rec_expected():
    with open(os.path.join('tests', 'fixtures', 'stylish_result_rec.txt')) as f:
        return f.read()


@pytest.fixture
def stylish_expected():
    with open(os.path.join('tests', 'fixtures', 'stylish_result.txt')) as f:
        return f.read()


@pytest.fixture
def plain_rec_expected():
    with open(os.path.join('tests', 'fixtures', 'plain_result_rec.txt')) as f:
        return f.read()


@pytest.fixture
def json_rec_expected():
    with open(os.path.join('tests', 'fixtures', 'json_result_rec.txt')) as f:
        return f.read()
