_STYLISH_KEY_VALUE_PATTERN: str = '\n{replacer}{change} {key}: {value}'
_STYLISH_OBJECT_PATTERN: str = '{{{body}\n{replacer}}}'


def formatter(diff_list: list, level: int = 1, replacer='  ') -> str:
    formatted_lines: list = []

    for diff_line in diff_list:
        formatted_lines.extend(_format_line(diff_line, level, replacer))

    body: str = ''.join(list(
        map(
            lambda item: _STYLISH_KEY_VALUE_PATTERN.format(
                replacer=item.get('replacer'),
                change=item.get('change', ' '),
                key=item.get('key'),
                value=item.get('value')
            ),
            formatted_lines
        )
    ))

    result_replacer = '' if level == 1 else replacer * (level - 1)
    result: str = _STYLISH_OBJECT_PATTERN.format(body=body,
                                                 replacer=result_replacer)
    return result


def _format_line(line, level: int, replacer: str) -> list:
    result = []
    key = line.get('key')
    children = line.get('children')

    if children:
        result.append(
            {
                'replacer': replacer * level,
                'key': key,
                'value': formatter(children, level + 2, replacer)
            }
        )
    else:
        change_status = line.get('change_status')
        old_value = line.get('old_value')
        new_value = line.get('new_value')

        if change_status in ('removed', 'changed'):
            result.append(
                {
                    'replacer': replacer * level,
                    'change': '-',
                    'key': key,
                    'value': _format_value(old_value, level + 1, replacer)
                }
            )
        if change_status in ('added', 'changed'):
            result.append(
                {
                    'replacer': replacer * level,
                    'change': '+',
                    'key': key,
                    'value': _format_value(new_value, level + 1, replacer)
                }
            )
        if change_status == 'unchanged':
            result.append(
                {
                    'replacer': replacer * level,
                    'key': key,
                    'value': _format_value(new_value, level + 1, replacer)
                }
            )

    return result


def _format_value(value_, level: int, replacer: str) -> str:
    if isinstance(value_, dict):
        list_ = [
            _STYLISH_KEY_VALUE_PATTERN.format(
                replacer=replacer * (level + 1),
                change=' ',
                key=k,
                value=_format_value(v, level + 2, replacer)
            )
            for k, v in value_.items()
        ]
        result = ''.join(list_)
        return _STYLISH_OBJECT_PATTERN.format(body=result,
                                              replacer=replacer * level)
    else:
        return str(value_).replace('True', 'true').replace('False', 'false')
