from gendiff.lib.diff import diff
from tests.fixtures.diff_expected import diff_expected


def test_diff(first_data_from_json_file, second_data_from_json_file):
    assert diff_expected == diff(first_data_from_json_file,
                                 second_data_from_json_file)
