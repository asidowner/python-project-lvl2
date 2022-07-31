import json
import os

import pytest

from gendiff.lib.diff import diff
from tests.fixtures.diff_expected import diff_expected


@pytest.fixture
def data_diff():
    return {
        'json': {
            'file1_rec': os.path.join('tests', 'fixtures', 'file1_rec.json'),
            'file2_rec': os.path.join('tests', 'fixtures', 'file2_rec.json'),
        }
    }


def test_diff(data_diff):
    data1 = json.load(open(data_diff.get('json').get('file1_rec'), encoding='utf8'))
    data2 = json.load(open(data_diff.get('json').get('file2_rec'), encoding='utf8'))
    assert diff_expected == diff(data1, data2)
