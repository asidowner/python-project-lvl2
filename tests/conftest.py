import os
import pytest


@pytest.fixture
def data():
    return {
        'json': {
            'file1': os.path.join('tests', 'fixtures', 'file1.json'),
            'file2': os.path.join('tests', 'fixtures', 'file2.json'),
            'file1_rec': os.path.join('tests', 'fixtures', 'file1_rec.json'),
            'file2_rec': os.path.join('tests', 'fixtures', 'file2_rec.json'),
            'wrong_path': os.path.join('tests', 'fixtures', 'wrong_path'),
            'expected': os.path.join('tests', 'fixtures', 'stylish_result.txt'),
            'expected_rec': os.path.join('tests', 'fixtures', 'stylish_result_rec.txt'),
            'format': 'stylish'
        },
        'yaml': {
            'file1': os.path.join('tests', 'fixtures', 'file1.yml'),
            'file2': os.path.join('tests', 'fixtures', 'file2.yaml'),
            'file1_rec': os.path.join('tests', 'fixtures', 'file1_rec.yml'),
            'file2_rec': os.path.join('tests', 'fixtures', 'file2_rec.yml'),
            'wrong_path': os.path.join('tests', 'fixtures', 'wrong_path'),
            'expected': os.path.join('tests', 'fixtures', 'stylish_result.txt'),
            'expected_rec': os.path.join('tests', 'fixtures', 'stylish_result_rec.txt'),
            'expected_rec_plain': os.path.join('tests', 'fixtures', 'plain_result_rec.txt'),
            'format': 'stylish'
        }
    }