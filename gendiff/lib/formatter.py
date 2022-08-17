from gendiff.utils.exception import NotSupportedFormatError
import gendiff.formatter.stylish_formatter as stylish_formatter
import gendiff.formatter.plain_formatter as plain_formatter
import gendiff.formatter.json_formatter as json_formatter

_FORMATTERS = {
    'stylish': stylish_formatter.get_formatted_data,
    'plain': plain_formatter.get_formatted_data,
    'json': json_formatter.get_formatted_data
}


def format_result(diff: list, format_: str) -> str:
    format_diff = _FORMATTERS.get(format_)

    if format_diff is None:
        raise NotSupportedFormatError('Unknown format, try gendiff -h')

    return format_diff(diff)
