import json
import os
import pathlib
from gendiff.utils.Exception import NotSupportFileSuffix

_SUPPORTED_SUFFIX = ('.json',)


def parse_file(file_path):
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f'Check your file path: {file_path}')

    file_suffix = pathlib.Path(file_path).suffix

    if file_suffix not in _SUPPORTED_SUFFIX:
        raise NotSupportFileSuffix(f'Support only: {_SUPPORTED_SUFFIX}')

    if file_suffix == '.json':
        return json.load(open(file_path))
