_FORMAT_PATTERNS = {
    'stylish': {
        'main': '{{{result}\n}}',
        'unchanged': '\n    {key}: {old_value}',
        'changed': '\n  - {key}: {old_value}'
                   '\n  + {key}: {new_value}',
        'added': '\n  + {key}: {new_value}',
        'removed': '\n  - {key}: {old_value}'
    }
}


def format_message(diff: list, format_: str) -> str:
    pattern = _FORMAT_PATTERNS.get(format_)
    main_pattern: str = pattern.get('main')

    lines = [
        _get_formatted_line(pattern, line_data)
        for line_data in diff
    ]

    result = ''.join(lines)

    return main_pattern.format(result=result)


def _get_formatted_line(pattern_: dict, line_data: dict) -> str:
    key: str = line_data.get('key')
    change_status: str = line_data.get('change_status')
    old_value: any = line_data.get('old_value')
    new_value: any = line_data.get('new_value')

    line_pattern: str = pattern_.get(change_status)

    return line_pattern.format(key=key,
                               old_value=old_value,
                               new_value=new_value)
