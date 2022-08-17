import json
import os
import pytest


def get_path_to_test_data(name: str) -> str:
    return os.path.join('tests', 'fixtures', name)


@pytest.fixture
def first_data_from_json_file():
    with open(get_path_to_test_data('file1_nested.json'),
              encoding='utf8') as f:
        return json.loads(f.read())


@pytest.fixture
def second_data_from_json_file():
    with open(get_path_to_test_data('file2_nested.json'),
              encoding='utf8') as f:
        return json.loads(f.read())
