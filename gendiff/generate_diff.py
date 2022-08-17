from gendiff.lib.formatter import format_result
from gendiff.lib.parser import parse_file
from gendiff.lib.diff import diff
from gendiff.lib.file_reader import get_data_from_file


def generate_diff(first_file_path: str,
                  second_file_path: str,
                  format_: str = 'stylish') -> str:
    first_file, first_file_suffix = get_data_from_file(first_file_path)
    second_file, second_file_suffix = get_data_from_file(second_file_path)

    first_file_data = parse_file(first_file, first_file_suffix)
    second_file_data = parse_file(second_file, second_file_suffix)

    result = diff(first_file_data, second_file_data)

    return format_result(result, format_)
