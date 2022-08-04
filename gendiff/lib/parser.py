import json
import yaml
from gendiff.utils.exception import NotSupportedFileSuffixError

SUPPORTED_SUFFIX = ('.json', '.yml', '.yaml')


def parse_file(file_data: str, file_suffix: str):
    if file_suffix not in SUPPORTED_SUFFIX:
        raise NotSupportedFileSuffixError(f'Support only: {SUPPORTED_SUFFIX}')

    if file_suffix == '.json':
        return json.loads(file_data)
    elif file_suffix in ('.yml', '.yaml'):
        return yaml.full_load(file_data)
