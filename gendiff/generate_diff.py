from gendiff.lib.formatter import format_result
from gendiff.lib.parser import parse_file
from gendiff.lib.diff import diff


def generate_diff(first_file_path: str,
                  second_file_path: str,
                  format_: str) -> str:
    first_file_data: dict = parse_file(first_file_path)
    second_file_data: dict = parse_file(second_file_path)

    result = diff(first_file_data, second_file_data)

    return format_result(result, format_)
