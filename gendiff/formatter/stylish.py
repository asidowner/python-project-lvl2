_STYLISH_KEY_VALUE_PATTERN: str = '\n{replacer}{change} {key}: {value}'
_STYLISH_OBJECT_PATTERN: str = '{{{body}\n{replacer}}}'


def formatter(diff_list: list, level: int = 1, replacer='  ') -> str:
    formatted_lines: list = []
    for diff_line in diff_list:
        key = diff_line.get('key')
        children = diff_line.get('children')

        if children:
            formatted_lines.append(
                {
                    'replacer': replacer * level,
                    'key': key,
                    'value': formatter(children, level + 2, replacer)
                }
            )
        else:
            change_status = diff_line.get('change_status')
            old_value = diff_line.get('old_value')
            new_value = diff_line.get('new_value')

            if change_status in ('removed', 'changed'):
                formatted_lines.append(
                    {
                        'replacer': replacer * level,
                        'change': '-',
                        'key': key,
                        'value': _format_value(old_value, level + 1, replacer)
                    }
                )
            if change_status in ('added', 'changed'):
                formatted_lines.append(
                    {
                        'replacer': replacer * level,
                        'change': '+',
                        'key': key,
                        'value': _format_value(new_value, level + 1, replacer)
                    }
                )
            if change_status == 'unchanged':
                formatted_lines.append(
                    {
                        'replacer': replacer * level,
                        'key': key,
                        'value': _format_value(new_value, level + 1, replacer)
                    }
                )

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
