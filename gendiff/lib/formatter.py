from gendiff.utils.Exception import NotSupportFormat
import gendiff.formatter.stylish as stylish

_FORMATTERS = {
    'stylish': stylish.formatter
}


def format_result(diff: list, format_: str) -> str:
    format_diff = _FORMATTERS.get(format_)

    if format_diff is None:
        raise NotSupportFormat('Unknown format, try gendiff -h')

    return format_diff(diff)
