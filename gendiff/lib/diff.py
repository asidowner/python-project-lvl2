def diff(first_data: any, second_data: any) -> dict or list:
    keys_set: set = set(first_data.keys())
    keys_set.update(set(second_data.keys()))

    result: list = [
        _get_diff_by_key(key, first_data, second_data)
        for key in keys_set
    ]
    result.sort(key=lambda x: x.get('key'))

    return result


def _get_diff_by_key(key: str, first_data: dict, second_data: dict):
    old_value = _get_formatted_value(key, first_data)
    new_value = _get_formatted_value(key, second_data)
    change_status = _get_change_status(old_value, new_value)

    if isinstance(old_value, dict) and isinstance(new_value, dict):
        return {
            'key': key,
            'children': diff(first_data=old_value, second_data=new_value)
        }
    else:
        return {
            'key': key,
            'change_status': change_status,
            'old_value': old_value,
            'new_value': new_value
        }


def _get_formatted_value(key_: str, data: dict):
    if key_ in data:
        value = data.get(key_)
        return 'null' if value is None else value
    else:
        return None


def _get_change_status(old_value: any = None,
                       new_value: any = None) -> str:
    if old_value is None and new_value is not None:
        return 'added'
    elif old_value is not None and new_value is None:
        return 'removed'
    elif old_value == new_value:
        return 'unchanged'
    else:
        return 'changed'
