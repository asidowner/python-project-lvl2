from gendiff.format_message import format_message
from gendiff.parse_file import parse_file


def generate_diff(first_file_path: str,
                  second_file_path: str,
                  format_: str) -> str:
    first_file_data: dict = parse_file(first_file_path)
    second_file_data: dict = parse_file(second_file_path)

    keys_set: set = set(first_file_data.keys())
    keys_set.update(set(second_file_data.keys()))

    diff: list = [
        _get_diff_by_key(key, first_file_data, second_file_data)
        for key in keys_set
    ]
    diff.sort(key=lambda x: x.get('key'))
    return format_message(diff, format_)


def _get_change_status(first_value: any = None, second_value: any = None) -> str:
    if first_value is None and second_value is not None:
        return 'added'
    elif first_value is not None and second_value is None:
        return 'removed'
    elif first_value == second_value:
        return 'unchanged'
    else:
        return 'changed'


def _get_diff_by_key(key: str, first_data: dict, second_data: dict) -> dict:
    def format_value(value: bool or None = None):
        if value is not None:
            return str(value).replace('False', 'false') \
                .replace('True', 'true')

    first_value = format_value(first_data.get(key))
    second_value = format_value(second_data.get(key))

    return {
        'key': key,
        'old_value': first_value,
        'new_value': second_value,
        'change_status': _get_change_status(first_value,
                                            second_value)
    }
