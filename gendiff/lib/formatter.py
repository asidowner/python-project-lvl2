from gendiff.utils.Exception import NotSupportFormat
import gendiff.formatter.stylish_formatter as stylish_formatter
import gendiff.formatter.plain_formatter as plain_formatter
import gendiff.formatter.json_formatter as json_formatter

_FORMATTERS = {
    'stylish': stylish_formatter.formatter,
    'plain': plain_formatter.formatter,
    'json': json_formatter.formatter
}


def format_result(diff: list, format_: str) -> str:
    format_diff = _FORMATTERS.get(format_)

    if format_diff is None:
        raise NotSupportFormat('Unknown format, try gendiff -h')

    return format_diff(diff)
