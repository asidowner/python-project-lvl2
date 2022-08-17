_PLAIN_PATTERNS: dict = {
    'removed': "Property '{key}' was removed",
    'added': "Property '{key}' was added with value: {new_value}",
    'changed': "Property '{key}' was updated. From {old_value} to {new_value}"
}


def get_formatted_data(diff_list: list) -> str:
    result = []
    for diff_item in diff_list:
        result.extend(_format_line(diff_item))

    return '\n'.join(result)


def _format_line(line, parent_key=None) -> list:
    result = []
    key = line.get('key')
    children = line.get('children')

    parent_key = key if not parent_key else '.'.join([parent_key, key])

    if children:
        for child in children:
            result.extend(_format_line(child, parent_key))
    else:
        change_status = line.get('change_status')
        old_value = line.get('old_value')
        new_value = line.get('new_value')

        if change_status != 'unchanged':
            pattern = _PLAIN_PATTERNS.get(change_status)
            result.append(
                pattern.format(key=parent_key,
                               old_value=_format_value(old_value),
                               new_value=_format_value(new_value))
            )

    return result


def _format_value(value):
    if isinstance(value, dict):
        return '[complex value]'
    elif isinstance(value, bool):
        return 'true' if value else 'false'
    elif isinstance(value, str) and value != 'null':
        return f"'{value}'"
    else:
        return value
