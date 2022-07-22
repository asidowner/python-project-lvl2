import json
from gendiff.format_message import format_message


def generate_diff(first_file_path: str,
                  second_file_path: str,
                  format_: str) -> str:

    first_file_data: dict = json.load(open(first_file_path))
    second_file_data: dict = json.load(open(second_file_path))

    keys_set: set = set(first_file_data.keys())
    keys_set.update(set(second_file_data.keys()))

    def get_change_status(first_value: any, second_value: any) -> str:
        if first_value is None and second_value is not None:
            return 'added'
        elif first_value is not None and second_value is None:
            return 'removed'
        elif first_value == second_value:
            return 'unchanged'
        else:
            return 'changed'

    diff: list = [
        {
            'key': key,
            'old_value': first_file_data.get(key),
            'new_value': second_file_data.get(key),
            'change_status': get_change_status(first_file_data.get(key),
                                               second_file_data.get(key))
        }
        for key in keys_set
    ]
    diff.sort(key=lambda x: x.get('key'))
    return format_message(diff, format_)
